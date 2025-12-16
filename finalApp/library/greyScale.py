
from PIL import Image

def GreyScale(img):
    greyImg = Image.new("RGB", (img.width, img.height))
    origRaster = img.load()
    greyRast = greyImg.load()

    for y in range(img.height):
        for x in range(img.width):
            pixel = origRaster[x,y]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            
            k = r*.2 + g*.7 + b*.1
            k = int(k)
            greyRast[x,y] = (k, k, k)

    return greyImg