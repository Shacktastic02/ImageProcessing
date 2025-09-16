from PIL import Image
import numpy as np

origImage = Image.open("./tiger.jpg")
origRaster = origImage.load()

finalImage = Image.new("RGB", (origImage.width, origImage.height))
finalRaster = finalImage.load()

vFlipMatrix = np.array([[1, 0, 0],
                        [0, 1, origImage.height],
                        [0, 0, 1]])

for x in range(origImage.width):
    for y in range(origImage.height):
        pix = origRaster[x,y]

        vec = np.array([x,y,1])

        result = vFlipMatrix @ vec

        xp = result[0]
        yp = result[1]

        finalRaster[xp, yp] = pix

finalImage.save("./vert_flip.jpg")