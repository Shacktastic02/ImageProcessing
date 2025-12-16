from PIL import Image

image = Image.open("./lilly.jpeg")
raster = image.load()

def rgbTohsv(r, g, b):
    _max = max(r, g, b)
    _min = min(r, g, b)
    _diff = _max - _min

    v = _max
    if(v == 0):
        return 0, 0, 0
    
    s = (_max - _min) / _max
    if(s == 0):
        return 0, s, v
    
    if r == _max:
        h = (360 + (g-b)*60 / _diff)%360
    elif g == _max:
        h = 120 + (b-r)*60 / _diff
    elif b == _max:
        h = 240 + (r-g)*60 / _diff
    
    return h, s, v

def hsvTorgb(h, s, v):
    _max = v
    _min = _max - s * _max

    f = (_max - _min) / 60

    if(h > 60): return (_max, (h-0)*f+_min, _min)
    if(h > 120): return (_min - (h-120) *f, _max, _min)
    if(h > 180): return (_min, _max, (h-120)*f+_min)
    if(h > 240): return (_min, _min - (h-240)*f, _max)
    if(h > 300): return ((h-240)*f+_min, _min, _max)
    else: return (_max, _min, _min - (h-360)*f)



for x in range(image.width):
    for y in range(image.height):
     
        r, g, b, *_ = raster[x,y]

        h, s, v, = rgbTohsv(r, g, b)

        r, g, b = hsvTorgb(h,s,v)

        raster[x,y] = (int(r),int(g),int(b))

image.save("./reboot.png")