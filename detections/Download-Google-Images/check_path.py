import os

# Путь к текстовому файлу
file_path = r"D:\projects\detections\Download-Google-Images\imgfordifcolor\azure_download\train\_annotations.txt"

# Создаем временный файл
temp_file = "D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure_download\\train\\_temp_annotations.txt"

# Список для хранения существующих файлов
existing_files = []

# Проверяем, существует ли каждый файл, указанный в текстовом файле
with open(file_path, "r") as file:
    for line in file:
        file_name = line.split(" ")[0]
        if os.path.isfile(file_name):
            existing_files.append(file_name)
            print(file_name)
print(existing_files)
# Записываем только строки, содержащие существующие файлы, во временный файл
with open(file_path, "r") as file, open(temp_file, "w") as temp:
    for line in file:
        file_name = line.split(" ")[0]
        if file_name in existing_files:
            temp.write(line)