#!/usr/bin/python
from PIL import Image
import os, sys

path = input("Enter file path : ")
location_to_save = input("Enter location to save : ")
dirs = os.listdir( path )

def resize(width, height, imageType):
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            rgb_im = im.convert('RGB')
            imResize = rgb_im.resize((width, height), Image.LANCZOS)
            imResize.save(location_to_save +  item , imageType, quality=90)

resize(width=400, height=400, imageType='JPEG')