import os
import re

folder_path = 'D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure_download\\train'
"""
# Получаем список файлов в папке
file_list = os.listdir(folder_path)

# Сортируем список файлов
file_list.sort()

# Создаем шаблон для новых имен файлов
new_name_pattern = r'^.*\.jpg\s$'
d = {}

# Перебираем файлы и переименовываем их
for i, file_name in enumerate(file_list, start=892):
    # Формируем новое имя файла
    new_file_name = re.sub(new_name_pattern, f'{i:08}.jpg', file_name)
    print(new_file_name)
    d[file_name] = new_file_name
    
    # Полный путь к текущему файлу
    old_file_path = os.path.join(folder_path, file_name)
    
    # Полный путь к новому файлу
    new_file_path = os.path.join(folder_path, new_file_name)
    
    # Переименовываем файл
    os.rename(old_file_path, new_file_path)

# Открываем файл и заменяем все названия внутри файла
with open('D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure_download\\train\\_annotations.txt', 'r+') as file:
    content = file.readlines()
    new_content = []
    for line in content:
        line = line.strip()
        if any(file_name in line for file_name in file_list):
            new_content.append(line)
    file.seek(0)
    file.write('\n'.join(new_content))
    file.truncate()
"""
directory = 'D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure'
existing_files = os.listdir(directory)
files = os.listdir(folder_path)
used_numbers = set()

# Поиск уже используемых номеров
for file in existing_files:
    if file.endswith(".jpg"):
        file_name = file.split(".")[0]
        try:
            number = int(file_name)
            used_numbers.add(number)
        except ValueError:
            pass

# Переименование файлов
for i in range(1, len(existing_files) + 1):
    if files[i-1].endswith(".jpg"):
        if i not in used_numbers:
            new_file_name = f"{i:08}.jpg"
            new_file_path = os.path.join(folder_path, new_file_name)

            print(f"Переименовываю файл {files[i-1]} в {new_file_name}")
            os.rename(os.path.join(folder_path, files[i-1]), new_file_path)
            with open('D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure_download\\train\\_anno.txt', 'r+') as annotations_file:
                content = annotations_file.read()
                content = content.replace(files[i-1], new_file_name)
                annotations_file.seek(0)
                annotations_file.write(content)
                annotations_file.truncate()
print("Скрипт завершен.")