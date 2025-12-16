from PIL import Image
import math
import re


name = "temple.jpg"
image = Image.open(name)
raster = image.load()

print("Image info for " + name)

print(image.width, image.height)

print(
    f"Size is {image.width}x{image.height}, which makes {image.width*image.height:,} pixels.")

size = image.width*image.height

print(
    f"At 4 bytes per pixel, that means a file size of approximately {size*4:,} bytes.")

pixel_dictionary = dict()

for x in range(image.width):
    for y in range(image.height):
        pixel = raster[x, y]

        if pixel not in pixel_dictionary:
            pixel_dictionary[pixel] = 0
        pixel_dictionary[pixel] += 1


print(f"This image has {len(pixel_dictionary):,} unique pixels.")

bits = math.log2(len(pixel_dictionary))

print(f"It would take {bits} bits to store the colors as a palette")


def to_ppm(image):
    output = f"P3\n"
    output += f"{image.width}\n"
    output += f"{image.height}\n"
    output += "255\n"
    output += ""

    raster = image.load()

    for y in range(image.height):
      line = ""
      for x in range(image.width):
          r, g, b, *_ = raster[x, y]
          line += f"{r} {g} {b} "
      output += line.rstrip() + "\n"
    return output

          


def from_ppm(string):
    pattern = re.compile(r"^(P3)\s+(\d+)\s(\d+)\s(\d+)\s(.*)", re.DOTALL)
    match = re.search(pattern, string)

    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.group(4))
    # print(match.group(5))

    image = Image.new("RGB", (int(match.group(2)), int(match.group(3))))
    raster = image.load()

    lines = match.group(5).splitlines()

    for y in range(image.height):
        line = lines[y]
        values = line.split()
        for x in range(image.width):
            index = x*3
            raster[x,y] = (int(values[index]), int(values[index+1]), int(values[index+2]))
    
    return image

ppm_string = to_ppm(image)

with open("out.ppm", "w") as f:
    f.write(ppm_string)

ppm_image = from_ppm(ppm_string)

ppm_image.save("ppm.png")

