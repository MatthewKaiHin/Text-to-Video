# Text-to-Video
This script is used to generate video from text.
The output is a video file with the name specified in the script.

The script is run by: `python app.py`

The script is tested on `Windows 10`.

### **Libraries used**:
* moviepy for video generation
* pyttsx3 for text-to-speech
* json for reading json file

Before running the script, please install the libraries by: `pip install requirements.txt`

## **Input format**:
The input is a json file with the following format:
```
{
    "video": [
        {
            "paragraph": "This is the first sentence. This is the second sentence.",
            "image": "./static/image/1.jpg",
            "fadein": 2
        },
        {
            "paragraph": "This is the third sentence. This is the fourth sentence.",
            "image": "./static/image/2.jpg",
            "fadein": 2
        }
    ]
}
```

## **Set up**:
1. Create a folder named "static" in the same directory as this script.
2. Create a folder named "image", "audio" and "video" in the "static" folder.
3. Upload the images in the "image" folder.
4. Create a json file with the format specified above and upload it in the "static" folder.
5. Change the input_data, output_dir and output_name in the script to the correct path and name.
6. Run the script.

* image folder: 
> The path to the image
* audio folder: 
> The path to the audio that is generated from the text. The audio should be removed after the video is generated. The script will also clean up the audio folder before generating the video.
* video folder: 
> The path to the video that is generated from the image and audio. The video will be saved in the video folder.
