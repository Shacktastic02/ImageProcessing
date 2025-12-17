from PIL  import Image

def Invert(img):
    inverted = img.copy()
    invRast =inverted.load()
    origRast = img.load()

    for y in range(img.height):
        for x in range(img.width):
            pix = origRast[x,y]

            r,g,b = pix

            r = 255 - r
            g = 255 - g
            b = 255 - b

            invRast[x,y] = (r,g,b)
    
    return inverted

# temp = Image.open("./frog.jpg")
# temp = Invert(temp)
# temp.save("./temp.png")