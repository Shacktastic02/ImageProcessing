from PIL import Image

image = Image.open("./eagle.jpg")
rast = image.load()

frames = []

max_frames = 5

for i in range(max_frames):
    frame = Image.new("RGB", (image.width, image.height))
    fRast = frame.load()

    for x in range (image.width):
        for y in range (image.height):
            p = rast[x,y]

            r = p[0]
            g = p[1]
            b = p[2]

            v = int(r*.2 + g*.7 + b*.1)

            fRast[x,y] = (
                int((1-i/max_frames*r)+(i/max_frames)*v),
                int((1-i/max_frames*g)+(i/max_frames)*v),
                int((1-i/max_frames*b)+(i/max_frames)*v),
            )

            # if(i==0):
            #     fRast[x,y] = (v, v, v)
            # else:
            #     fRast[x,y] = (r,g,b)
            
    frames.append(frame)

frames[0].save(
    "animation.png",
    save_all = True,
    append_images = frames[1:],
    duration = 500
)