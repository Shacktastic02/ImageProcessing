def Sepia(img):
    sepia = img.copy()
    sepRast = sepia.load()
    origRast = img.load()

    for y in range(img.height):
        for x in range(img.width):
            pix = origRast[x,y]
            r,g,b = pix
            
            # based off of an algorithm from leware.net/photo/blogSepia.html originally based off of microsoft's

            # These define the differences between R, G, and B
            # you can adjust these to fine tune the resulting sepia to your prefference
            rgGap = 23
            gbGap = 19

            # These adjust ments allow us to keep the pverall luminace of the image the same as the original
            # they're derived from the greyscale equation: k = .3r + .59g + .11b
            # so l is the luminace and we use the adjustments to tint it to sepia like colors
            # final color = (l + ra) * .3 + (l + ga) * .59 + (l + ba) * .11
            rAdjustment = rgGap * .7 - gbGap *.11
            gAdjustment = rAdjustment - rgGap
            bAdjustment = gAdjustment - gbGap

            l = .30*r + .59*g + .11*b
            r = l + rAdjustment
            g = l + gAdjustment
            b = l + bAdjustment


            sepRast[x,y] = (int(r),int(g),int(b))
    
    return sepia

def MSSepia(img):
    sepia = img.copy()
    sepRast = sepia.load()
    origRast = img.load()

    for y in range(img.height):
        for x in range(img.width):
            pix = origRast[x,y]
            r,g,b = pix
            
            # the original microsoft formula

            newR = .393*r + .769*g + .198*b
            newG = .349*r + .686*g + .168*b
            newB = .272*r + .534*g + .131*b


            sepRast[x,y] = (int(newR), int(newG), int(newB))
    
    return sepia
