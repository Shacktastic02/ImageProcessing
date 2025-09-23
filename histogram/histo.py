from PIL import Image

image = Image.open("./eagle.jpg")
rast = image.load()

lvls = [0 for _ in range(256)]

for x in range (image.width):
    for y in range (image.height):
        p = rast[x,y]

        r = p[0]
        g = p[1]
        b = p[2]

        v = int(r*.2 + g*.7 + b*.1)
        lvls[v] +=1

        rast[x,y] = (v, v, v)

image.save("./bw.png")

max_lvl = max(lvls)

histo = Image.new("RGB", (256,256))
histRast = histo.load()

for x in range(256):
    for y in range(256):
        lvl = lvls[x]
        if( (256-y-1) < lvl/max_lvl*256):
            histRast[x,y] = (x, x, x)
        else:
            histRast[x,y] = (100, 100, 255)

histo.save("./hist.png")