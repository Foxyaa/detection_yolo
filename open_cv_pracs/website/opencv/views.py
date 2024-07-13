from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.http import StreamingHttpResponse
import cv2
from .forms import ImageForm
from .models import *
from ultralytics import YOLO

model = YOLO('../detect_pet.pt')
score = 0

def media_file_YOLO_opencv(request, id):
    def stream_YOLO(media_file_id):
        media_file = get_object_or_404(UploadingImg, id=media_file_id)
        media_file_path = media_file.media_file.path
        cap = cv2.VideoCapture(media_file_path)
        model = YOLO('../detect_pet.pt')  # load a pretrained model (recommended for training)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = model.predict(frame)
            frame_with_results = results[0].plot()
            ret, jpeg = cv2.imencode('.jpg', frame_with_results)
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
    return StreamingHttpResponse(stream_YOLO(id), content_type='multipart/x-mixed-replace; boundary=frame')

def video_filter(request):
    def stream_rgb_video():
        cam = cv2.VideoCapture(0)
        while cam.isOpened():
            ret, frame = cam.read()
            res_img = model(source=frame, show=False, conf=0.5)
            anno_frm = res_img[0].plot()
            #score = res_img.boxes.length()
            img_bytes = cv2.imencode('.jpg', anno_frm)[1].tobytes()
            cv2.waitKey(24)
            yield (b'--frame\r\n'b'Content-type: image/jpg\r\n\r\n' + img_bytes + b'\r\n')
            #b'--frame\r\n'b'Content-type: text/plain\r\n\r\n' + str(score).encode() + b'\r\n')
    return StreamingHttpResponse(stream_rgb_video(), content_type='multipart/x-mixed-replace; boundary=frame')

def image_list(request):
    images = UploadingImg.objects.all()
    return render(request, 'opencv/image_list.html', {'images': images})


class UploadImg(CreateView):
    img_model = UploadingImg
    img_form = ImageForm
    template_uploading = 'upload_form.html'
# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             img_object = form.instance
#             return render(request, 'opencv/upload_image.html', {'form': form, 'img_obj': img_object})
#     else:
#         form = ImageForm()
#     return render(request, 'opencv/upload_image.html', {'form': form})