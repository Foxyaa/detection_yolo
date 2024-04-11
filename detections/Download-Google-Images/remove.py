import os
"""
files = os.listdir('D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure')
for file in files:
    if not file.endswith('.jpg'):
        os.remove(os.path.join('D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure', file))
"""
files = os.listdir('D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure_download\\train')
for file in files:
    if not file.endswith('.jpg'):
        os.remove(os.path.join('D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure_download\\train', file))