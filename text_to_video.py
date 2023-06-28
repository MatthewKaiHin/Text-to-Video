from moviepy.editor import *
import pyttsx3
import json

"""
Read me:
This script is used to generate video from image and text, and tested in Windows 10.
If there is more than one image, you should manually seprate the text into paragraphs. Each paragraph of text will be converted to audio clip and combined with corresponding image.
Images should be stored in the folder named 'image'. The image path and text should be stored in JSON file. 
The script will generate audio clips that only support Cantonese. Please make sure you have Cantonese voice installed in your windows system.
The granerated audio clips and video will be stored in the folder named 'audio' and 'video' respectively.
Every time you run this script, the audio folder will be cleared before and after video generation.
The video will be supported in mp4 format with 24 fps and aac audio codec.
"""

# set up text to speech engine
class Audio():
    def __init__(self, input_text, output_audio_path):
        self.input_text = input_text
        self.output_audio_path = output_audio_path

        self.engine = self.tts_engine()
        
    # select cantonese voice
    def select_cantonese(self, voices):
        language = 'Microsoft Tracy Desktop - Chinese(Traditional, HongKong SAR)'
        for voice in voices:
            if voice.name == language:
                return voice.id
        # if no cantonese voice found, raise error message
        raise Exception('No Cantonese voice found.')
            
    # set up text-to-speech engine
    def tts_engine(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', self.select_cantonese(voices))
        engine.setProperty('rate', 220)
        engine.setProperty('volume', 1)
        return engine

    # generate text-to-speech audio and save to audio folder
    def tts_generator(self):
        self.engine.save_to_file(self.input_text, self.output_audio_path)
        self.engine.runAndWait()
        return self.output_audio_path
    

# set up image and audio clip
class Image():
    def __init__(self, input_text, image_path, audio_path, fadein):
        self.input_text = input_text
        self.image_path = image_path
        self.audio_path = audio_path
        self.fadein = fadein

        self.audio = self.audio_clip_generator()

    # generate audio clip
    def audio_clip_generator(self):
        audio = Audio(self.input_text, self.audio_path).tts_generator()
        audio_clip = AudioFileClip(audio)
        return audio_clip
            
    # generate image clip and combine with audio clip
    def image_clip_generator(self):
        image = (ImageClip(self.image_path)
                      .resize((1024, 1532))
                      .fadein(self.fadein)
                      .set_audio(self.audio)
                      .set_duration(self.audio.duration))
        return image
    

# combine all clips into one video
class Video():
    def __init__(self, input_file_path, output_dir, output_video_name):
        self.input_file_path = input_file_path
        self.output_dir = output_dir
        self.output_video_name = output_video_name

        self.clips = self.input_to_clip()
    
    # remove existing audio files in audio folder
    def remove_audio_files(self):
        if os.path.exists('./static/audio'):
            for file in os.listdir('./static/audio'):
                os.remove(os.path.join('./static/audio', file))

    # read json file and generate clips
    def input_to_clip(self):
        # read json file
        with open(self.input_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            clips = []
            # clear existing audio files in audio folder before video generation
            self.remove_audio_files()
            # generate clips following the order of json file
            for index, content in enumerate(data['contents']):
                if 'paragraph' and 'image' and 'fadein' in content:
                    text = content['paragraph']
                    fadein = content['fadein']
                    image_path = f'./static/image/{content["image"]}'
                    audio_path = f'./static/audio/audio_{index}.mp3'
                    clips.append(Image(text, image_path, audio_path, fadein)
                                    .image_clip_generator())                                       
        return clips

    # combine all clips into one video
    def video_generator(self):
        video = concatenate_videoclips(self.clips)
        output_path = os.path.join(self.output_dir, self.output_video_name)
        video.write_videofile(output_path, fps=24, audio_codec='aac')

        # clear existing audio files in audio folder after video generation
        self.remove_audio_files()