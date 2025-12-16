from PIL import Image

origImg = Image.open("skate.jpg")
origRast = origImg.load()

# waterMarkImg = Image.new("RGBA", (origImg.width, origImg.height))
waterMarkImg = Image.open("watermark.png")
waterMarkRast = waterMarkImg.load()
# waterMarkImg.save("watermark.png")

for x in range(origImg.width):
    for y in range(origImg.height):
        pixWM = waterMarkRast[x,y]
        pixOI = origRast[x,y]
        
        color = [255, 255, 255]
        a = .5

        if(pixWM[3] != 0):
            pixNew = (int((1-a)*pixOI[0] + a * color[0]), int((1-a)*pixOI[1] + a * color[1]), int((1-a)*pixOI[2] + a * color[2]))
            origRast[x,y] = pixNew


origImg.save("marked.png")