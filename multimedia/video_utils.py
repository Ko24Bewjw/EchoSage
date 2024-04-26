# -*- coding: utf-8 -*-
# @Time : 10:18 2024/4/23
# @Author : Allen-wan
# @File : video_utils.py
# @Software : PyCharm
# video_utils.py
from moviepy.editor import VideoFileClip, AudioFileClip

def process_media(video_path, audio_path, output_path):
    try:
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        video = video.set_audio(audio)
        video.write_videofile(output_path, codec='libx264', audio_codec='aac')
        return output_path
    except Exception as e:
        print(f"Error processing media: {str(e)}")
        return None
