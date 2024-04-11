import os
files = os.listdir('D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure_download\\train')


with open("D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure_download\\train\\_annotations.txt", "r") as f:
    lines = f.readlines()

with open("D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure_download\\train\\_anno.txt", "w") as f:
    for line in lines:
        for file in files:
            if file in line:
                f.write(line)
                files.remove(file)
