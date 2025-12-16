from PIL import Image

img = Image.new("RGB", (400,400))
rast = img.load()

for x in range(img.width):
    for y in range(img.height):
        
        
        rast[x,y] = (200, 0, 200)
        
img.save('./placeHolder.png')