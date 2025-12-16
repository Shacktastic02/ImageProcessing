from PIL import Image
import math

def Vinegette(img):
    origRast = img.load()

    center = (img.width/2, img.height/2)

    vinStartDist = max(img.width/2, img.height/2)

    vinImage = Image.new("RGB", (img.width, img.height))
    vinRast = vinImage.load()

    for x in range(img.width):
        for y in range(img.height):
            pix = origRast[x,y]
            r, g, b = pix

            dist = math.sqrt(((x - center[0])**2)+((y - center[1])**2))

            diff = dist - vinStartDist
            scale = 255 * (.005 * diff)
            if(dist >= vinStartDist):

                vinRast[x,y] = (int(r - scale), int(g - scale), int(b - scale))
            else:
                vinRast[x,y] = pix

    return vinImage

