import cv2
import os

def check_azure_color(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Проверка каждого пикселя в изображении
    for row in image:
        for pixel in row:
            # Проверяем, находится ли пиксель в диапазоне подходящего голубого цвета
            if pixel[0] >= 165 and pixel[1] >= 174 and pixel[2] >= 198 and pixel[0] <= 198 and pixel[1] <= 224 and pixel[2] <= 228:
                return True

    return False

# Путь к папке с изображениями
folder_path = r"D:\projects\detections\Download-Google-Images\images\color\azure"

# Получение списка файлов в папке
image_files = os.listdir(folder_path)

# Обработка каждого изображения в папке
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    if not check_azure_color(image_path):
        print("DELETE ",image_path)
        os.remove(image_path)
