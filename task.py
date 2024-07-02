import os
from PIL import Image, ImageDraw


def create_album_page(folder_list, output_file, images_per_row=4, padding=100, background_color=(255, 255, 255)):
    image_list = []

    for folder in folder_list:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.lower().endswith('.png'):
                    file_path = os.path.join(root, file)
                    try:
                        image = Image.open(file_path)
                        image_list.append(image)
                    except Exception as e:
                        print(f"Could not process file {file_path}: {e}")

    if image_list:
        # Размер изображений и сетки
        img_width, img_height = image_list[0].size
        num_images = len(image_list)
        num_rows = (num_images + images_per_row - 1) // images_per_row

        # Создание пустого альбомного листа с фоном пастельного цвета
        album_width = images_per_row * (img_width + padding) + padding
        album_height = num_rows * (img_height + padding) + padding
        album_image = Image.new(
            'RGB', (album_width, album_height), background_color)

        # Заполнение альбомного листа изображениями
        for i, img in enumerate(image_list):
            row = i // images_per_row
            col = i % images_per_row
            x_offset = col * (img_width + padding) + padding // 2
            y_offset = row * (img_height + padding) + padding // 2
            album_image.paste(img, (x_offset, y_offset))

        album_image.save(output_file)
        print(f"Successfully created album page: {output_file}")
    else:
        print("No valid images found.")


# Пример использования
folder_list = [
    # r'\test_task\1369_12_Наклейки 3-D_3',
    # r'\test_task\1388_2_Наклейки 3-D_1',
    # r'\test_task\1388_6_Наклейки 3-D_2',
    r'\test_task\1388_12_Наклейки 3-D_3',



]
output_file = r'\test_task\Result.tif'
create_album_page(folder_list, output_file)
