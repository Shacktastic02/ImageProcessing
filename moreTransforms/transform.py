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

rotMatrix = ["rotation", (w,h), np.array([[math.cos(rads), -math.sin(rads), 0],
                                         [math.sin(rads), math.cos(rads), 0],
                                         [0, 0, 1]])]

corners = [np.array([0, 0, 1]), np.array([w, 0, 1]), np.array([w, h, 1]), np.array([0, h, 1])]

rotCorners = [rotMatrix @ corner for corner in corners]

xs = [rotCorner[0] for rotCorner in rotCorners]
ys = [rotCorner[1] for rotCorner in rotCorners]

newWid = int(max(xs) - min(xs))
newHig = int(max(ys) - min(ys))
newSiz = (newWid, newHig)

upLeft = np.array([1, 0, -w/2],
                  [0, 1, -h/2],
                  [0, 0, 1])

downRight = np.array([1, 0, newWid/2],
                     [0, 1, newHig/2],
                     [0, 0, 1])

centRot = [downRight @ rotMatrix @ upLeft]

rotation = ["rotation", newSiz, centRot]

transforms = [horizTran, translate, scaleUp, rotation]

for name, size, matrix in transforms:
    newImage = Image.new("RGB", size)
    newRaster = newImage.load()
    
    invMatrix = np.linalg.inv(matrix)

    for x in range(w):
        for y in range(h):

            vec = np.array([x, y, 1])

            result = invMatrix @ vec

            xp = result[0]
            yp = result[1]

            if 0 <= xp < w and 0 <= yp < h:
                newRaster[x, y] = origRaster[xp, yp]

    newImage.save(name+".png")