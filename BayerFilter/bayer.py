
from PIL import Image


image = Image.open("./frog.jpg")
raster = image.load()

for x in range(image.width):
    for y in range(image.height):
        pixel = raster[x,y]

        r, g, b = pixel

        if x % 2 != y % 2:
            k = g
        else:
            if (y % 2 == 0):
                k = r
            else:
                k = b

        #concept
        # if(x % 2 == 0):
        #     if (y % 2 == 0):
        #         k = r
        #     else:
        #         k = g
        # else:
        #     if(x % 2 == 0):
        #         k = g
        #     else:
        #         k = b

        raster[x,y] = (k, k, k)



imageRGB = Image.new("RGB", (image.width, image.height))
rasterRGB = imageRGB.load()

#create RBG filter image

for x in range(image.width):
    for y in range(image.height):
        pixel = raster[x,y]

        k = pixel[0]

        out = (k, 0, 0)
        if( x%2 != y%2):
            out =(0, k, 0)
        else:
            if( x % 2 == 0):
                out = (k, 0, 0)
            else:
                out = (k, 0, 0)

        raster[x, y] = out

imageRGB.save("./frog_bayer_RGB")

imageSmall = Image.new("RGB", (image.width//2, image.height//2))
rasterSmall = imageSmall.load()

for x in range(image.width):
    for y in range(image.height):
        upperLeft = (x*2, y*2)

        rPixel = rasterRGB[upperLeft[0], upperLeft[1]]
        gPixel1 = rasterRGB[upperLeft[0]+1, upperLeft[1]]
        gPixel2 = rasterRGB[upperLeft[0], upperLeft[1]+1]
        bPixel = rasterRGB[upperLeft[0]+1, upperLeft[1]+1]

        rasterSmall[x,y] = (rPixel[0], gPixel1[0])



image.save("./frog_bayer.png")

