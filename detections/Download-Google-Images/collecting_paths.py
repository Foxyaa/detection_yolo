import os
from PIL import Image

directory = "D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure"
# Получение списка файлов
image_files = os.listdir(directory)
#with open("D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure\\paths.txt",'w') as file:
#    for image in image_files:
#        if image.endswith('.jpg'):
#            file.write(image + '\n')


# Iterate through all files in the directory
yolo_lines = []
for file in image_files:
    if file.endswith(".txt"):
        # Check if the corresponding jpg file exists
        file_name = file.split(".")[0]
        image_path = os.path.join(directory, file_name + ".jpg")
        txt_file_path = os.path.join(directory, file)
        if os.path.isfile(image_path):
            image = Image.open(image_path)
            image_width, image_height = image.size
            with open(txt_file_path, 'r') as txt_file:
                txt_data = txt_file.readline().strip().split()
                for line in txt_data:
                    x = float(line[1]) * image_width
                    y = float(line[2]) * image_height
                    x1 = float(line[3]) * image_width
                    y1 = float(line[4]) * image_height
            # Create a YOLO format string
                    yolo_string = f"{file_name}.jpg {x},{y},{x1},{y1},{line[0]}\n"
                    yolo_lines.append(yolo_string)
            # Write the string to the dataset file
            

            #print(f"Created entry for file {file_name}.jpg")
dataset_path = os.path.join(directory, "_annotations.txt")
print(yolo_lines)
with open(dataset_path, 'w') as dataset_file:
    for yolo_line in yolo_lines:
        dataset_file.write(yolo_line)
print("Script completed.")



with open(dataset_path,'r') as dataset, open('D:\\projects\\detections\\Download-Google-Images\\imgfordifcolor\\azure\\anno.txt','a') as new_file:
    for line in dataset:
        elements = line.split()
        new_line = f"{elements[0]} {elements[2]},{elements[3]},{elements[4]},{elements[5]},{elements[1]}\n"
        new_file.write(new_line)

