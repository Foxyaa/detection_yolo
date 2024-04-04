# Download-Google-Images
Code to mass download images from Google Images using JavaScript Console Window and python script.

Code derived from: https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/

Steps to perform:
- Query your intended Google search
- Scroll down through images until they become unrelated to your query or until you've passed enough images for your dataset
- Right click and hit "Inspect" and then navigate to "Console" tab
- One by one enter the lines from console.js into the console window and run them
- Move urls.txt from Downloads folder to Download-Google-Images folder
- Create an "images" folder where your images will be downloaded
- Run follwing two python commands as follows:
```bash
pip install -r requirements.txt
python download_images.py --urls urls.txt --output images
```

You should now have all your images inside your images folder!

Примечение:
- Использовалось это видео как руководство https://www.youtube.com/watch?v=EGQyDla8JNU
- Я добавила свои скрипты check.py для асинхронного способа удалять изображения, которые не содержат голубые пиксели, check_azure обычный, пользовалась им, тоже работает. Способ корявый, вручную надежнее
- В console.js работает определенный момент, который запускается из консоли разработчика в браузере. В яндексе ничего менять в коде не надо тогда
- remove_dublicate.py для проверки хэшей, удалять должен дубликаты, но смысла в нем как мне кажется нет. Ни разу дубликаты не встретил из браузера. Минус в том, что изображения бывают сжатые и растянутые, он их дубликатами не считает
- urls2.txt это пример файла, который скачивается из браузера. Содержит ссылки на изображения, которые надо скачать
