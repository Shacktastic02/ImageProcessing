from PIL import Image
import random
import math

def l1_diff(a,b):
    return(sum(abs(x-y) for x,y in zip(a,b)))

def l2_diff(a,b):
    return( math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2))

def linf_diff(a,b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))

def closest_color(color, color_list):
    return min(color_list, key=lambda option: l1_diff(color, option))

def randColor():
    return tuple(random.randint(0,255) for _ in range(3))

        # goes somewhere idk where
        # if pixel not in color_count:
        #     color_count[pixel] = 0
        # color_count[pixel]+=1

# k means algorithm\
iterations = 5
k = 255
palette = [randColor() for _ in range(10)]

for i in range(iterations):
    closest_color_list = [[] for _ in range(k)]

    for color_count in sorted_color_count:
        closest_palette_color = closest_color(color_count[0], palette)
        closest_index = palette.index(closest_palette_color)
        closest_color_list[closest_index].append(color_count)

    for j in range(k):
        closest_list = closest_color_list[j]
        if len(closest_list) == 0:
            palette[j] = randColor()
        else:
            sums = [0,0,0]
            sum_weights = 0
            for color, count in closest_list:
                sums = [a+b*count for a,b in zip(sums, color)]
                sum_weights += count
            palette[j] = tuple(a//sum_weights for a in sums)


color_count = []

image = Image.open("./hound.jpg")
raster = image.load()

for y in range(image.height):
    for x in range(image.width):
        pixel = raster[x,y]

        
        raster[x,y] = closest_color(pixel, palette)

image.save("./reduced.png")