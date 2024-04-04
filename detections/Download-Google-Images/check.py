import cv2
import os
import asyncio

async def check_azure_color(image_path):
    image = cv2.imread(image_path)
    for row in image:
        for pixel in row:
            # Проверяем, находится ли пиксель в диапазоне подходящего голубого цвета
            if pixel[0] >= 165 and pixel[1] >= 174 and pixel[2] >= 198 and pixel[0] <= 198 and pixel[1] <= 224 and pixel[2] <= 228:
                return True

    return False

async def process_image(image_file):
    image_path = os.path.join(folder_path, image_file)
    if not await check_azure_color(image_path):
        print("DELETE ", image_path)
        os.remove(image_path)

folder_path = r"D:\projects\detections\Download-Google-Images\images\color\azure"

image_files = os.listdir(folder_path)

# Создание списка задач для обработки каждого изображения
tasks = [process_image(image_file) for image_file in image_files]

# Запуск всех задач асинхронно
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))
