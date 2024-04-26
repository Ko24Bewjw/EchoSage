# -*- coding: utf-8 -*-
# @Time : 17:23 2024/4/22
# @Author : Allen-wan
# @File : tasks.py
# @Software : PyCharm
# tasks.py
from celery import shared_task
from .models import MediaFile
from .video_utils import process_media  # 导入视频处理函数

# tasks.py
from celery import shared_task
from django.conf import settings
from .models import MediaFile
from .video_utils import process_media  # 导入视频处理函数
import os


# @shared_task
# def process_media_files(media_file_id):
#     media_file = MediaFile.objects.get(id=media_file_id)
#     video_path = media_file.video_file.path
#     audio_path = media_file.audio_file.path
#
#     # 构建输出文件路径
#     output_filename = os.path.basename(video_path).replace('.mp4', '_processed.mp4')
#     output_path = os.path.join(settings.MEDIA_ROOT, 'processed_videos', output_filename)
#
#     result_path = process_media(video_path, audio_path, output_path)
#     if result_path:
#         # 保存相对于 MEDIA_ROOT 的路径
#         media_file.processed_video = os.path.join('processed_videos', output_filename)
#         media_file.status = 'completed'
#     else:
#         media_file.status = 'error'
#     media_file.save()

from celery import shared_task
from django.conf import settings
from .models import MediaFile
from .video_utils import process_media  # Import video processing function
import os


# @shared_task
# def process_media_files(media_file_id):
#     media_file = MediaFile.objects.get(id=media_file_id)
#     video_path = media_file.video_file.path
#     audio_path = media_file.audio_file.path
#
#     # Ensure the directory for processed videos exists
#     output_dir = os.path.join(settings.MEDIA_ROOT, 'processed_videos')
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)  # Create the directory if it does not exist
#
#     # Build the output file path
#     output_filename = os.path.basename(video_path).replace('.mp4', '_processed.mp4')
#     output_path = os.path.join(output_dir, output_filename)
#
#     result_path = process_media(video_path, audio_path, output_path)
#     if result_path:
#         # Save the relative path to MEDIA_ROOT
#         media_file.processed_video = os.path.join('processed_videos', output_filename)
#         media_file.status = 'completed'
#     else:
#         media_file.status = 'error'
#     media_file.save()

# @shared_task
# def process_media_files(media_file_id):
#     media_file = MediaFile.objects.get(id=media_file_id)
#     video_path = media_file.video_file.path
#     audio_path = media_file.audio_file.path
#     output_path = video_path.replace('.mp4', '_processed.mp4')
#     result_path = process_media(video_path, audio_path, output_path)
#     if result_path:
#         media_file.processed_video = result_path
#         media_file.status = 'completed'
#     else:
#         media_file.status = 'error'
#     media_file.save()
from celery import shared_task
from .models import MediaFile
from .video_utils import process_media
import os
from django.conf import settings


@shared_task
def process_media_files(media_file_id):
    media_file = MediaFile.objects.get(id=media_file_id)
    video_path = media_file.video_file.path
    audio_path = media_file.audio_file.path
    output_filename = os.path.basename(video_path).replace('.mp4', '_processed.mp4')
    output_path = os.path.join(settings.MEDIA_ROOT, output_filename)

    result_path = process_media(video_path, audio_path, output_path)
    if result_path:
        media_file.processed_video = os.path.join(settings.MEDIA_URL, output_filename)
        media_file.status = 'completed'
    else:
        media_file.status = 'error'
    media_file.save()
