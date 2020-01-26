#encode image in directory to b64 and then pass to classifier
from io import BytesIO
from PIL import Image
import argparse
import base64
import sys
import os

parser2 = argparse.ArgumentParser()
parser2.add_argument(
    "input_file",
    help = "Path to the input image file"
)
args2 = parser2.parse_args()

image_data = open(args2.input_file, 'rb').read()
b64_data = base64.encodebytes(image_data)

filename = 'b64string.txt'
with open(filename, 'wb') as file_object:
    file_object.write(b64_data)

b64_strdata = ""
with open(filename) as file_object:
    b64_strdata = file_object.read().rstrip()
b64_bytdata = base64.b64decode(b64_strdata)#.encode('ascii') #encode str into bytes
pic_data = BytesIO(b64_bytdata)
img = Image.open(pic_data)
img.save('pic.jpeg', "JPEG")
print(b64_strdata)
