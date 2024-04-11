import cv2
import os
import numpy as np

def check_azure_color(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Создаем новый массив, в котором каждый элемент является результатом логического "и" 
    # между соответствующими элементами массивов blue_range и green_range. Это позволяет одновременно проверить
    # выполнение обоих условий для каждого пикселя изображения
    blue_range = np.logical_and(image[:, :, 0] >= 160, image[:, :, 0] <= 250)
    green_range = np.logical_and(image[:, :, 1] >= 188, image[:, :, 1] <= 255)
    blue_green_range = np.logical_and(blue_range, green_range)
    # Вычисляем процент пикселей, соответствующих условию
    percentage = np.sum(blue_green_range) / (image.shape[0] * image.shape[1]) * 100
    if percentage >= 30:
        print("Image contains blue or azure color")
        return True
    else:
        return False

# Путь к папке с изображениями
folder_path = r"D:\projects\detections\Download-Google-Images\imgfordifcolor\azure_download\valid"

# Получение списка файлов в папке
image_files = os.listdir(folder_path)
print("LIST OF FILES contains ", len(image_files), " files")
# Обработка каждого изображения в папке
total = 0
for image_file in image_files:
    total += 1
    print ("Itteration №", total)
    image_path = os.path.join(folder_path, image_file)
    format_file = os.path.splitext(image_file)[1]
    if format_file != '.jpg': #format_file != '.jpeg': for unix
        print(image_file, " was skipped")
        pass
    elif check_azure_color(image_path) is False:
        print("DELETE ", image_file)
        os.remove(image_path)
