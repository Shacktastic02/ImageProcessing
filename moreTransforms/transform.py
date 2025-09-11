from PIL import Image
import numpy as np
import math


origImage = Image.open("./jelly.png")
origRaster = origImage.load()

w = origImage.width
h = origImage.height

horizTran = ["horizontalFlip", (w,h), np.array([[-1, 0, w-1],
                                                [0, 1, 0],
                                                [0, 0, 1]])]

translate = ["translate", (w,h), np.array([[1, 0, 100],
                                          [0, 1, -200],
                                          [0 ,0 ,0]])]

scaleUp = ["scaleUp", (w*2, h*2), np.array([[2, 0, 0],
                                            [0, 2, 0],
                                            [0, 0, 1]])]

rads = math.radians(45)

rotation = ["rotation", (w,h), np.array([[math.cos(rads), -math.sin(rads), 0],
                                         [math.sin(rads), math.cos(rads), 0],
                                         [0, 0, 1]])]

transforms = [horizTran, translate, scaleUp]

for name, size, matrix in transforms:
    newImage = Image.new("RGB", size)
    newRaster = newImage.load()
    
    invMatrix = np.linalg(matrix)

    for x in range(w):
        for y in range(h):
            # pix = origRaster[x,y]

            vec = np.array([x, y, 1])

            result = invMatrix @ vec

            xp = result[0]
            yp = result[1]

            if 0 <= xp < w and 0 <= yp < h:
                newRaster[x, y] = origRaster[xp, yp]

    newImage.save(name+".png")