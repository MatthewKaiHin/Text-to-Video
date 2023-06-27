from text_to_video import Video

# run the script
if __name__ == "__main__":
    # set up config for input and output
    input_data = './static/sample_input.json'
    output_dir = './static/video'
    output_name = 'demo_video.mp4'

    # generate video
    video = Video(input_data, output_dir, output_name)
    video.video_generator()
