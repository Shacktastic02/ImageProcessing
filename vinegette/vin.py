from PIL import Image
import math


origImage = Image.open("./cat3.jpg")
origRast = origImage.load()

center = (origImage.width/2, origImage.height/2)

vinStartDist = max(origImage.width/2, origImage.height/2)

vinImage = Image.new("RGB", (origImage.width, origImage.height))
vinRast = vinImage.load()

for x in range(origImage.width):
    for y in range(origImage.height):
        pix = origRast[x,y]
        r, g, b = pix

        dist = math.sqrt(((x - center[0])**2)+((y - center[1])**2))

        diff = dist - vinStartDist
        scale = 255 * (.005 * diff)
        if(dist >= vinStartDist):

            vinRast[x,y] = (int(r - scale), int(g - scale), int(b - scale))
        else:
            vinRast[x,y] = pix

vinImage.save("./vin3.png")

