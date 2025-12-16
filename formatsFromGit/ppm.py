from PIL import Image

image = Image.open("./zebra.jpg")
raster = image.load()

string = "P6\n"
string += f"{image.width}\n"
string += f"{image.height}\n"
string += "256\n"

for y in range(image.height):
    for x in range(image.width):
        pix = raster[x,y]

        r = pix[0]
        g = pix[1]
        b = pix[2]
        string += r.to_bytes().decode("latin-1")
        string += g.to_bytes().decode("latin-1")
        string += b.to_bytes().decode("latin-1")
    # string += "\n"

with open("out.ppm", "w") as f:
    f.write(string)


lines = string.split("\n")
assert lines[0] == "P6"
width = int(lines[1])
height = int(lines[2])
_ = int(lines[3])

remainingString = string[len(lines[0])+len(lines[1])+len(lines[2])+len(lines[2])+4]


# rasterLines = lines[4:]


ppmImage = Image.new("RGB", (width, height))
ppmRaster = ppmImage.load()

for y in range(height):
    # line = rasterLines[y]
    # rgbTriples = line.split()
    for x in range(width):
        ind = (y*width+x)*3
        r = int(remainingString[ind+0].encode("latin-1"))
        g = int(remainingString[ind+1].encode("latin-1"))
        b = int(remainingString[ind+2].encode("latin-1"))
        ppmRaster[x,y] = (r,g,b)
