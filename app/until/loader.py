from app import config
import os


def load_img(filename, content):
    with open(config.IMG_HOLDER_PATH / filename, 'wb') as new_file:
        new_file.write(content)


def remove_img(filename):
    os.remove(config.IMG_HOLDER_PATH / filename)
