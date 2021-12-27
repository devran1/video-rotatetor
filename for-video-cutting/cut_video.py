
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("vid.mp4", 0, 3, targetname="test.mp4")