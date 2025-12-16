from PIL import Image

image = Image.open("small.png")
raster = image.load()
print(f"size: {image.width} x {image.height}, total pixels: {image.width * image.height}")

# for x in range(image.width):
#     for y in range(image.height):

#         raster[x,y] = (255, 255, 255)

# image.save("./make.png")

def to_format(image):
    string = "cat\n"
    string += f"{image.width}\n"
    string += f"{image.height}\n"
    return""

def from_format():
    return

print(to_format(image))