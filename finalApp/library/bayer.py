
from PIL import Image

#create mosaiced bayer filter image
def BayerFilter(img):
    mosaic = img.copy()
    mosaicRast = mosaic.load()

    for y in range(mosaic.height):
        for x in range(mosaic.width):
            pix = mosaicRast[x,y]
            r,g,b = pix
            k = 0
            if(x%2 != y%2):
                k = g
            else:
                if(x%2 == 0):
                    k = r
                else:
                    k = b
            mosaicRast[x,y] = (k,k,k)

    for y in range(img.height):
        for x in range(img.width):
            pixel = mosaicRast[x,y]

            k = pixel[0]

            out = (k, 0, 0)
            if( x%2 != y%2):
                out =(0, k, 0)
            else:
                if( x % 2 == 0):
                    out = (k, 0, 0)
                else:
                    out = (0, 0, k)

            mosaicRast[x, y] = out

    return mosaic

#simple demosaic
def Demosaic(img):

    deMos = Image.new("RGB", (img.width//2, img.height//2))
    deMosRast = deMos.load()
    origRast = img.load()

    for y in range(deMos.height):
        for x in range(deMos.width):
            upperLeft = (x*2, y*2)

            rPixel = origRast[upperLeft[0], upperLeft[1]]
            gPixel1 = origRast[upperLeft[0]+1, upperLeft[1]]
            gPixel2 = origRast[upperLeft[0], upperLeft[1]+1]
            bPixel = origRast[upperLeft[0]+1, upperLeft[1]+1]

            deMosRast[x,y] = (rPixel[0], (gPixel1[1]+gPixel2[1])//2, bPixel[2])
    return deMos
