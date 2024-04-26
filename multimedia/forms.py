# -*- coding: utf-8 -*-
# @Time : 17:22 2024/4/22
# @Author : Allen-wan
# @File : forms.py
# @Software : PyChar

from django import forms
from .models import MediaFile

class MediaFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['audio_file', 'video_file']

