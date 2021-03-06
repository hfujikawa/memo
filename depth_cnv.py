# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 07:46:17 2017
https://stackoverflow.com/questions/32323922/how-to-convert-a-24-color-bmp-image-to-16-color-bmp-in-python
https://stackoverflow.com/questions/1065945/how-to-reduce-color-palette-with-pil
@author: hfuji
"""

#import cv2
import numpy as np
from PIL import Image

colors =[(255,0,0), (255,127,0), (255,255,0), (127,2550,0),
         (0,255,0),(0,255,127), (0,255,2255), (0,127,255),
         (0,0,255), (127,0,255),(255,0,255), (255,0,127)]

height = 300
width = 300
img = np.zeros([height, width, 3], dtype=np.uint8)
row_size = height / len(colors)
for i in range(len(colors)):
    img[i*row_size:i*row_size+row_size, :] = colors[i]

img24Color = Image.fromarray(img)
img8Color = img24Color.convert('P', palette=Image.ADAPTIVE, colors=8)
img8Color.save('img8Color.png')
