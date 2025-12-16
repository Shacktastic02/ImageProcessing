from PIL import Image

img = Image.new("RGBA", (400,400))
rast = img.load()

for x in range(img.width):
    for y in range(img.height):
        
        
        rast[x,y] = (0, 0, 0, 0)
        
img.save('./placeHolder.png')