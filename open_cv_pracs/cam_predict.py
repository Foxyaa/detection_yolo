from ultralytics import YOLO
import cv2

score = 0

model = YOLO('detect_pet.pt')

def stream_rgb_video():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        res_img = model(source=frame, show=False, conf=0.5)
        anno_frm = res_img.plot()
        score = res_img.boxes.length()
        img_bytes = cv2.imencode('.jpg', anno_frm)[1].tobytes()
        cv2.waitKey(24)
        print(score + "   " + img_bytes)

# model = YOLO('../detect_pet.pt')
# score = 0
# def stream_rgb_video():
#     """
#     res_img = model(source=1, show=True, conf=0.5)
#     img_bytes = cv2.imencode('.jpg', res_img)[1].tobytes()
#     cv2.waitKey(24)
#     yield (b'--frame\r\n'b'Content-type: image/jpg\r\n\r\n' + img_bytes + b'\r\n')
#     """
#     cam = cv2.VideoCapture(1)
#     while cam.isOpened():
#         ret, frame = cam.read()
#         res_img = model(source=frame, show=False, conf=0.7)
#         anno_frm = res_img[0].plot()
#         score = res_img.boxes.length()
#         img_bytes = cv2.imencode('.jpg', anno_frm)[1].tobytes()
#         cv2.waitKey(24)
#         yield (b'--frame\r\n'b'Content-type: image/jpg\r\n\r\n' + img_bytes + b'\r\n'
#         b'--frame\r\n'b'Content-type: text/plain\r\n\r\n' + str(score).encode() + b'\r\n')






# def stream_image():
#     img = cv2.imread('media/ph.jpg')
#     rgb = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     image_bytes = cv2.imencode(".jpg", rgb)[1].tobytes()
#     yield (b'--frame\r\n'b'Content-type: image/jpg\r\n\r\n' + image_bytes + b'\r\n')
#
#
# def image_filter(request):
#     return StreamingHttpResponse(stream_image(), content_type='multipart/x-mixed-replace; boundary=frame')

# html
# <h2>Список изображений</h2>
# {% for img in images %}
# <div>
#     <li><a href="{% url 'filter.url' id_img %}">{{ img.title }}</a></li>
# </div>
# {% endfor %}