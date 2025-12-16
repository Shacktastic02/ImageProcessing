from PIL import Image
import os

def rg_sim(origImage):
    origRast = origImage.load()

    simImage = Image.new("RGB",(origImage.width, origImage.height))
    simRast = simImage.load()
    for y in range(simImage.height):
        for x in range(simImage.width):
        
            r, g, b, *_ = origRast[x,y]
            r = max(r,g)
            g = max(r, g)
            simRast[x,y] = (r,g,b)
    return simImage

def yb_sim(origImage):
    origRast = origImage.load()
    simImage = Image.new("RGB",(origImage.width, origImage.height))
    simRast = simImage.load()

    for y in range(simImage.height):
        for x in range(simImage.width):
        
            r, g, b, *_ = origRast[x,y]
            b = max(b,g)
            g = max(b, g)
            simRast[x,y] = (r,g,b)
    
    return simImage
