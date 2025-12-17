from PIL import Image
import math

def GausBlur(img):
    gausBlur = Image.new("RGB", (img.width, img.height))
    gausRast = gausBlur.load()
    tempImg = img.copy()
    tempRast = tempImg.load()
    origRast = img.load()

    
    kSize = 13
    halfSize = kSize // 2
    strength = 50.0

    kernel = Generate1DKernel(kSize, strength)

    # horizontal pass
    for y in range(img.height):
        for x in range(img.width):
            rSum = 0
            gSum = 0
            bSum = 0
            for i in range(-halfSize, halfSize+1):
                #get the pixelinfo
                currentX = clamp(x + i, 0, img.width-1)
                pixel = origRast[currentX, y]
                r,g,b = pixel

                #adjust the rgb to blur
                rSum += r * kernel[i+halfSize]
                gSum += g * kernel[i+halfSize]
                bSum += b * kernel[i+halfSize]


            tempRast[x,y] = (int(rSum), int(gSum), int(bSum))

    # vertical pass
    for x in range(img.width):
        for y in range(img.height):
            rSum = 0
            gSum = 0
            bSum = 0
            for i in range(-halfSize, halfSize+1):
                #get the pixelinfo
                currentY = clamp(y + i, 0, img.height-1)
                pixel = tempRast[x, currentY]
                r,g,b = pixel
                #adjust the rgb to blur
                rSum += r * kernel[i+halfSize]
                gSum += g * kernel[i+halfSize]
                bSum += b * kernel[i+halfSize]

            gausRast[x,y] = (int(rSum), int(gSum), int(bSum))


    return gausBlur

def Generate1DKernel(size, sigma):

    halfSize = size//2
    kernel = []

    sum = 0

    #generate the values
    for i in range(size):   
            x = i-halfSize
            kernel.append(math.exp(-(x**2) / (2 * sigma**2)))
            sum += kernel[i]

    #normalize them
    for i in range(size):
         kernel[i] /= sum
    
    return kernel

def clamp(i, low, high):
     if i < low:
          return low
     elif i > high:
          return high
     else:
          return i
     


