# Text-to-Video (Cantonese)
This script is used to generate video from image and text, and tested in `Windows 11`.

If there is more than one image, you should manually seprate the text into paragraphs. Each paragraph of text will be converted to audio clip and combined with corresponding image.

Images should be stored in the folder named `image`. The image path and text should be stored in `JSON` file. The script will generate audio clips that only support **Cantonese**. **Please make sure you have Cantonese voice installed in your windows system**. The granerated audio clips and video will be stored in the folder named `audio` and `video` respectively. Every time you run this script, the audio folder will be cleared before and after video generation. The video will be supported in `mp4` format with `24 fps` and `aac audio codec`.

***
The script is run by: `python app.py`

Before running the script, please install the libraries by: `pip install requirements.txt`

Libraries used:
* moviepy for video generation
* pyttsx3 for text-to-speech
* json for reading json file

## **Input format**:
The input is a json file with the following format:
```
{
    "contents": [
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
1. Create a folder named `static` in the same directory as this script.
2. Create a folder named `image`, `audio` and `video` in the `static` folder.
3. Upload the images in the `image` folder.
4. Create a json file with the format specified above and upload it in the "static" folder.
5. Change the input_data, output_dir and output_name in the script to the correct path and name.
6. Run the script.

|Folder|Description|
|:----------|:-------------------|
|image|The path to the image|
|audio|The path to the audio that is generated from the text. The audio should be removed after the video is generated. The script will also clean up the audio folder before generating the video.|
|video|The path to the video that is generated from the image and audio. The video will be saved in the video folder.|
