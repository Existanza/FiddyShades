# written for Python version 3.4.1
__author__ = 'Deca'
# import argparse
import encode
import decode


def init():
    """Reads the image path from the command line."""
    # parser = argparse.ArgumentParser(description='Load the path.')
    # parser.add_argument(dest='filename')
    # args = parser.parse_args()
    # print(args.filename)
    # file_name = args.filename
    print("Input the name of the file (with its extension) to encode/decode.")
    print("Remember to put it into the program's directory first.")
    file_name = input()
    if file_name[-4:] == '.txt':
        encode.load_text(file_name)
    else:
        decode.load_image(file_name)


init()