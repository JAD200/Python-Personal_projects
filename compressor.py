import os
# *  Image compressor Pillow
from PIL import Image
# *   Size formatter
from humanize import naturalsize

download_folder = "../../../../Downloads/"
#   Folders for the files
pictures_folder = "../../../../Pictures/"

if __name__ == '__main__':
    try:
        for filename in os.listdir(download_folder):
            name, extension = os.path.splitext(download_folder + filename)

            if extension in ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG']:
                # Opens, moves and compresses the image
                picture = Image.open(download_folder + filename)
                picture.save(pictures_folder + 'compressed_' + filename, optimize=True, quality=60)
                # Saves the original size
                original_size = os.stat(download_folder + filename).st_size
                # Removes the old picture
                os.remove(download_folder + filename)
                # Saves the compressed size
                compressed_size = os.stat(
                    pictures_folder + 'compressed_' + filename).st_size
                print(
                    f'{name}: {extension} | Tamaño reducido: {naturalsize(original_size)} a {naturalsize(compressed_size)}')
            else:
                print('\nNo se encontraron imágenes\n')
                break
    except ValueError:
        print(f'Se desconoce la extensión {extension}')
