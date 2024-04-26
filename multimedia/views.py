from django.http import JsonResponse
from .forms import MediaFileForm
from .models import MediaFile
from .tasks import process_media_files
from django.contrib.auth.decorators import login_required
from celery import current_app
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import MediaFile
from django.contrib.auth.decorators import login_required
from .tasks import process_media_files
from celery import current_app

# @login_required
# def file_upload_view(request):
#     if request.method == 'POST':
#         form = MediaFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             media_file = form.save(commit=False)
#             media_file.user = request.user
#             media_file.status = 'processing'
#             media_file.save()
#             task = process_media_files.delay(media_file.id)  # Assuming this task processes the file
#             media_file.task_id = task.id
#             media_file.save()
#             return JsonResponse({'task_id': task.id, 'status': media_file.status})
#         else:
#             return JsonResponse({'error': 'Upload failed', 'errors': form.errors.as_json()}, status=400)
#     else:
#         form = MediaFileForm()
#         return render(request, 'multimedia/upload_media.html', {'form': form})
#
# @login_required
# def cancel_task_view(request, task_id):
#     try:
#         media_file = MediaFile.objects.get(id=task_id, user=request.user)
#         if media_file.task_id:
#             current_app.control.revoke(media_file.task_id, terminate=True)
#             media_file.status = 'canceled'
#             media_file.save()
#             return JsonResponse({'message': 'Task canceled'})
#     except MediaFile.DoesNotExist:
#         return JsonResponse({'error': 'Task not found'}, status=404)

# from django.shortcuts import render
# from django.http import JsonResponse
# from .forms import MediaFileForm
# from .models import MediaFile
# from django.contrib.auth.decorators import login_required
# from celery import current_app
#
# @login_required
# def file_upload_view(request):
#     if request.method == 'POST':
#         form = MediaFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             media_file = form.save(commit=False)
#             media_file.user = request.user
#             media_file.status = 'processing'
#             media_file.save()
#             # 假设这是一个异步任务
#             task = process_media_files.delay(media_file.id)  # 修改为你的实际任务处理函数
#             media_file.task_id = task.id
#             media_file.save()
#             return JsonResponse({'task_id': task.id, 'status': media_file.status})
#         else:
#             return JsonResponse({'error': 'Upload failed', 'errors': form.errors.as_json()}, status=400)
#     else:
#         form = MediaFileForm()
#         return render(request, 'multimedia/upload_media.html', {'form': form})
from django.shortcuts import render
from django.http import JsonResponse
from .forms import MediaFileForm
from .models import MediaFile
from django.contrib.auth.decorators import login_required
from .tasks import process_media_files
from django.conf import settings

@login_required
def file_upload_view(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            media_file = form.save(commit=False)
            media_file.user = request.user
            media_file.status = 'processing'
            media_file.save()
            task = process_media_files.delay(media_file.id)
            media_file.task_id = task.id
            media_file.save()
            return JsonResponse({'task_id': task.id, 'status': media_file.status})
        else:
            return JsonResponse({'error': 'Upload failed', 'errors': form.errors.as_json()}, status=400)
    else:
        form = MediaFileForm()
        return render(request, 'multimedia/upload_media.html', {'form': form})

@login_required
def cancel_task_view(request, task_id):
    try:
        media_file = MediaFile.objects.get(task_id=task_id, user=request.user)
        if media_file:
            current_app.control.revoke(media_file.task_id, terminate=True)
            media_file.status = 'canceled'
            media_file.save()
            return JsonResponse({'message': 'Task canceled', 'status': 'canceled'})
    except MediaFile.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import MediaFile

# @login_required
# def task_status_view(request, task_id):
#     try:
#         media_file = MediaFile.objects.get(task_id=task_id)
#         if media_file.status == 'completed':
#             return JsonResponse({'status': media_file.status, 'processed_video_url': media_file.processed_video.url})
#         else:
#             return JsonResponse({'status': media_file.status})
#     except MediaFile.DoesNotExist:
#         return JsonResponse({'error': 'Task not found'}, status=404)
@login_required
def task_status_view(request, task_id):
    try:
        media_file = MediaFile.objects.get(task_id=task_id)
        if media_file.status == 'completed':
            print(f"MEDIA_URL: {settings.MEDIA_URL}")
            print(f"media_file: {str(media_file.processed_video)}")
            video_url = str(media_file.processed_video)
            return JsonResponse({'status': media_file.status, 'video_url': video_url})
        else:
            return JsonResponse({'status': media_file.status})
    except MediaFile.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)
