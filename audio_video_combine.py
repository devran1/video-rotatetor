#!/usr/bin/env python3


from moviepy.editor import *
import cv2

def audio_video_combine(video_name):

    rot_vid="rotated-" + video_name
    rotated_video=f"./rotated_video/{rot_vid}"

    audio=f"./audios/{video_name}.mp3"

    final_file=f"final-{video_name}"


    cap = cv2.VideoCapture(f"./v/{video_name}")

    fps = cap.get(cv2.CAP_PROP_FPS)


    my_clip = VideoFileClip(rotated_video)

    audio_background = AudioFileClip(audio)

    final_clip = my_clip.set_audio(audio_background)

    final_clip.write_videofile(final_file,fps=fps)

