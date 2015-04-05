# written for Python version 3.4.1
__author__ = 'Deca'
from PIL import Image
import os
import math
from datetime import datetime


def load_text(filename):
    """Reads the text file to be encoded into an image."""
    print("Opening " + filename + ".")
    try:
        # f = open(filename, 'r')
        try:
            f = open(filename, 'r')
            text = f.read()
        except UnicodeDecodeError:
            f = open(filename, 'r', encoding='utf-8')
            text = f.read()
        f.close()
        print("Encoding " + filename + ".")
        create_image(text)
    except IOError:
        print('Failed to open/save the file.')


def create_image(text):
    """Creates a new image to encode the text into."""
    x = math.ceil(math.sqrt(len(text)))
    y = math.ceil(math.sqrt(len(text)))
    im = Image.new("RGB", (x, y), (32, 255, 255))
    encode(im, text)


def encode(im, text):
    """Encodes the text file into an image."""
    pixels = im.load()
    for i in range(len(text)):
        pix = ord(text[i])
        if pix == 8211 or pix == 8212:
            pix = 45
        if pix == 8216 or pix == 8217 or pix == 8218:
            pix = 96
        if pix == 8220 or pix == 8221 or pix == 8222:
            pix = 34
        pixels[int(i / math.ceil(math.sqrt(len(text)))), i % math.ceil(math.sqrt(len(text)))] = (pix, 255, 255)
        # ch = chr(pix)
        print(str(pix), end=' ')
        # print(str(pix) + ' ' + ch)
        # try:
        #     print(ch, end='')
        # except UnicodeEncodeError:
        #     print('?', end='')
    print('Image encoded successfully, trying to save it.')
    save_image(im)


def save_image(im):
    """Saves the image, with date as the file name."""
    path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Hidden') + '\\'
    if not os.path.exists(path):
        os.makedirs(path)
    date = str(datetime.now())
    path += date
    path = path.replace(':', '-')
    path = path.replace('.', '-')
    path += '.bmp'
    path = path[:1] + ':' + path[2:]
    im.save(path)
    print('Image successfully saved as ' + path)