# written for Python version 3.4.1
__author__ = 'Deca'
from PIL import Image
import os
import sys
from datetime import datetime


def load_image(filename):
    """Decodes the image into the text."""
    print("Opening " + filename + ".")
    try:
        im = Image.open(filename)
        create_text(im)
    except FileNotFoundError:
        print('File not found.')


def create_text(im):
    path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Hidden') + '\\'
    if not os.path.exists(path):
        os.makedirs(path)
    date = str(datetime.now())
    path += date
    path = path.replace(':', '-')
    path = path.replace('.', '-')
    path += '.txt'
    path = path[:1] + ':' + path[2:]
    f = open(path, 'w')
    print('Text file created, trying to decode.')
    save_text(im, f, path)


def save_text(im, f, path):
    pixels = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            tmp_tuple = pixels[i, j]
            # print(tmp_tuple[0], end=' ')
            if i % (int(im.size[0]/10)) == 0 and j == 0 and i > 0:
                print('.', end=' ')
                sys.stdout.flush()
            ch = chr(tmp_tuple[0])
            try:
                f.write(str(ch))
            except UnicodeEncodeError:
                f.write(str('?'))
            del tmp_tuple
    print('')
    print('Decoded successfully to ' + path)