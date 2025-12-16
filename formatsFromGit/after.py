from PIL import Image
import math

image = Image.open('./zebra.jpg')
print(f"The image is of size {image.width} by {image.height}. That's {(image.width*image.height):,} pixels")
print(f"That's {(image.width*image.height*3):,} bytes")

all_colors = dict()



raster = image.load()

for x in range(image.width):
    for y in range(image.height):
        pixel = raster[x,y]
        
        if pixel not in all_colors:
           all_colors[pixel] = 0
        
# image.save('./bw.png')
print(f"Your image had {len(all_colors)} unique colors.")

# Ideas
# - Store list of unique colors as a list (palette)
#   - For each color, store where it goes on the image

# Save to our format
def to_format(image):
    string = "cat\n"
    string += f"{image.width}\n"
    string += f"{image.height}\n"
    
    all_colors = dict()
    raster = image.load()
    zero_pad_size = 0
    delimiter_size = 0
    
    byte_width = math.ceil(math.log10(image.width*image.height))

    for x in range(image.width):
        for y in range(image.height):
            zero_pad_size += math.ceil(math.log10(image.width*image.height))
            pixel = raster[x,y]
            i = image.width * y + x
            delimiter_size += len(str(i)) + 1
            
            if pixel not in all_colors:
                all_colors[pixel] = []
            all_colors[pixel].append(i)
          
            
    for pixel in all_colors:
        indices = all_colors[pixel]
        indices_string = "".join([str(i).zfill(byte_width) for i in indices])
        
        string += f"{str(pixel[0]).zfill(3)}{str(pixel[1]).zfill(3)}{str(pixel[2]).zfill(3)}{indices_string}\n"
    print("Hidey ho")
    print(zero_pad_size)
    print(delimiter_size)
    
    
    return string

# Read from our format
def from_format(string):
    lines = string.split("\n")
    # print(lines)
    assert lines[0] == "cat"
    width = int(lines[1])
    height = int(lines[2])
    byte_width = math.ceil(math.log10(width*height))
    print(width, height, byte_width)
    
    image = Image.new("RGB", (width, height))
    raster = image.load()

    palette = lines[3:]
    for line in palette:
        if not line: continue
        color_bytes = line[:9]
        location_bytes = line[9:]
        r = int(color_bytes[:3])
        g = int(color_bytes[3:6])
        b = int(color_bytes[6:])
        # print(r, g, b)
        for i in range(0, len(location_bytes), byte_width):
            location_index = location_bytes[i:i+byte_width:]
            index = int(location_index)
            y = math.floor(index/width)
            x = index - y * width
            raster[x,y] = (r, g, b)

    return image
    

# print(to_format(image))
# to_format(image)

with open("out.format", "w") as f:
    f.write(to_format(image))
    
new_image = from_format(to_format(image))
new_image.save("orange_juice.png")
