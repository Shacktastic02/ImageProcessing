from PIL import Image

image = Image.new("RGB", (1,1))
raster = image.load()

for x in range(image.width):
    for y in range(image.height):

        raster[x,y] = (255, 255, 255)

image.save("./make.png")