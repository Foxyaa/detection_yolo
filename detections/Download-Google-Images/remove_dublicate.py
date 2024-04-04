from imutils import paths
import numpy as np
import argparse
import cv2
import os

def dhash(image, hashSize=8):
	# преобразование изображения в оттенки серого и изменение размера изображения в оттенках серого,
	# добавление одного столбца (ширина), чтобы вычислить горизонтальный градиент
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	resized = cv2.resize(gray, (hashSize + 1, hashSize))
	# вычисление (относительного) горизонтального градиента между соседними пикселями столбцов изображения
	diff = resized[:, 1:] > resized[:, :-1]
	# преобразование отличающихся изображений в хэш
	return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

# создание анализатора аргументов
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
 help="путь к датасету")
ap.add_argument("-r", "--remove", type=int, default=-1,
 help="выполнять пробный запуск")
args = vars(ap.parse_args())

# найдите пути ко всем изображениям в нашем каталоге входных данных и
# затем инициализируем наш словарь хэшей
print("[INFO] computing image hashes...")
imagePaths = list(paths.list_images(args["dataset"]))
hashes = {}
# перебираем пути к нашим изображениям
for imagePath in imagePaths:
	# загрузите входное изображение и вычислите хэш
	image = cv2.imread(imagePath)
	h = dhash(image)
	# захватите все пути к изображениям с этим хэшем, добавьте текущее изображение
	# путь к нему и сохранение списка обратно в словаре хэшей
	p = hashes.get(h, [])
	p.append(imagePath)
	hashes[h] = p
	
for (h, hashedPaths) in hashes.items():
	if len(hashedPaths) > 1:
		# проверка на пробный запуск
		if args["remove"] <= 0:
			montage = None
			for p in hashedPaths:
				# загрузить входное изображение и изменить его размер до фиксированной ширины и высоты
				image = cv2.imread(p)
				image = cv2.resize(image, (150, 150))
				if montage is None:
					montage = image
				else:
					montage = np.hstack([montage, image])
			print("[INFO] hash: {}".format(h))
			cv2.imshow("Montage", montage)
			cv2.waitKey(0)
		else:
			# перебор всех путей к изображениям с одинаковым хэшем, за исключением первого изображения в списке (поскольку мы хотим сохранить
			# одно, и только одно, дублирующееся изображение)
			for p in hashedPaths[1:]:
				os.remove(p)