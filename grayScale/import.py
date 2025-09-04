from PIL import Image

image = Image.open("./snek.jpg")
raster = image.load()

for x in range(image.width):
    for y in range(image.height):
        pixel = raster[x,y]
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]
        
        if(g < 150):
            k = r*.2 + g*.7 + b*.1
            k = int(k)
            raster[x,y] = (k, k, k)

image.save("./coby.png")