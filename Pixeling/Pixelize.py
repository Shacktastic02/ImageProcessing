from PIL import Image
import SuperPixel




# Based on algorith from this paper: https://gfx.cs.princeton.edu/pubs/Gerstner_2012_PIA/Gerstner_2012_PIA_small.pdf

#-----------------------------------------------Main Loop----------------------------------------------------------#
def Pixelize(img):
    pixeled = img.copy()
    pixRast = pixeled.load
    origRast = img.load()

    ########################################### INITIALIZE #########################################################

    # Get input dimensions
    inWidth = img.width
    inHeight = img.height

    # Set super pixels to a regular grid based on output size

        # output size is arbitrary
    outWidth = inWidth // 2
    outHeight = inHeight // 2

        #There will be one super pixel per pixel in the output image
    superPixels = []

    for y in range(outHeight):
        for x in range(outWidth):

            sP = new SuperPixel()



    # Assign input pixels to nearest super pixel based on position

    # Initialize palatte to have one color (mean color)

    # Associate each super pixel with this color

    # Initialize temp

    # Loop until Temp is down
        
        # Refine super pixels based on pallate

        # Update Palate

        # If palatte converged

            # Reduce temp

            # expand palatte if not at max

            # Post Process
    
    # Saturate pallate

    # Produce final image

    ########################################################################################################## end #


#--------------------------------------------Functions-------------------------------------------------------------#

######################################### REFINE SUPERPIXELS #######################################################

def RefineSuperPixels(superPixels, inImg, palatte):

    # Interate modified SLIC from paper

        # Measure distance to each super pixel (position AND color)
    
    # Adjust super pixel centers

    # Smooth colors

    return superPixels

############################################################################################################# end ##
########################################## REFINE PALATTE ##########################################################

def RefinePalatte(superPixels, palatte, T):
    
    assignments = []
    # Compute color probabilities

    # Assign each super pixel to color

    # update each palatte color as weighted averages of super pixel colors

    return palatte, assignments

############################################################################################################## end #
########################################## EXPAND PALATTE ##########################################################

def ExpandPalatte(palatte):
    
    newPalatte = []

    # For each color

        # Check if clusters should split

        # Else dont split them

    return newPalatte

############################################################################################################## end #
########################################### POST PROCESS ###########################################################

def PostProcess(superPixels, palette):
    
    # Spatial clean up
    pass

############################################################################################################## end #
######################################## SATURATE PALATTE ##########################################################

def SaturatePalatte(palatte):
    #for each color
        #adjust
    return palatte

############################################################################################################## end #