from PIL import Image
import numpy as np


image = Image.open("./duck.jpg")
raster = image.load()

array = np.empty((image.height, image.width))

for y in range(image.height):
    for x in range(image.width):
        r, g, b, *_ = raster[x,y]
        k = (r + b+ b)//3
        array[y,x] = k

four = np.fft.fft2(array)

amount = 1500

for y in range(image.height):
    for x in range(image.width):
        f = four[y,x]

        xDiff = abs(x - image.width/2)
        yDiff = abs(y - image.height/2)

        if(xDiff < amount or yDiff < amount):
            four[y,x] = 0



shifted = np.fft.fftshift(four)

mag = np.log(np.abs(shifted)+1)
normed = mag / mag.max() *255

invert = np.fft.ifft2(four)
abs_inv = np.abs(invert)

Image.fromarray(array.astype(np.uint8)).save("./freq.png")
Image.fromarray(normed.astype(np.uint8)).save("./four.png")
Image.fromarray(abs_inv.astype(np.uint8)).save("./inv.png")