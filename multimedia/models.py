from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
import uuid
import os

@deconstructible
class PathAndRename(object):
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}_{}_{}.{}'.format(self.prefix, instance.user.id, uuid.uuid4(), ext)
        return os.path.join(self.prefix, filename)

class MediaFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to=PathAndRename('audios'), blank=True, null=True)
    video_file = models.FileField(upload_to=PathAndRename('videos'), blank=True, null=True)
    processed_video = models.FileField(upload_to=PathAndRename('processed_videos'), blank=True, null=True)
    status = models.CharField(max_length=10, default='pending')  # pending, processing, completed, canceled
    task_id = models.CharField(max_length=50, blank=True, null=True)  # Store Celery task ID
