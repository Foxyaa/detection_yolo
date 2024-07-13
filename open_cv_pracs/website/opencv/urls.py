from django.urls import path
from .views import *

urlpatterns = [
    path('', image_list, name='image_list'),
    #path('upload_image/', upload_image, name='upload_image'),
    path('media_files/<int:id>', media_file_YOLO_opencv, name='media_file_YOLO_opencv'),
    path('video_filter/', video_filter, name='video_filter.url'),
    path('post/',UploadImg.as_view(), name='add')
]