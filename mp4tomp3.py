#!/usr/bin/env python3



#mp4 to mp3 convertion

from moviepy.editor import * 



filename="MOV_0010.mp4"


def mp4_to_mp3(video_name):

    video_path=f"./v/{video_name}"

    mp3_path=f"./audios/{video_name}.mp3"


    mp4_without_frames = AudioFileClip(video_path)     
    mp4_without_frames.write_audiofile(mp3_path)     
    mp4_without_frames.close() # function call mp4_to_mp3("my_mp4_path.mp4", "audio.mp3"
