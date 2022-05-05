import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import Image

im = Image.open('image.jpg')
# using Image.ADAPTIVE to avoid dithering
out = im.convert('P', palette=Image.ADAPTIVE, colors=5)


