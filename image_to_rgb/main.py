from PIL import Image
# Sanitize pixel value for pretty print
def getValToWrite(pixel):
    if pixel < 10:
        valToWrite = "  "+str(pixel)
    elif pixel < 100:
        valToWrite = " "+str(pixel)
    else:
        valToWrite = str(pixel)
    
    return valToWrite+" "

# Separate red, green, blue pixel values into separate files
def loadPixels():
    # Open Image file
    myImage = Image.open("./emojiforfpgaresized.jpg", 'r')
    imageHeight = myImage.size[0]
    imageWidth = myImage.size[0]

    # Open the pixel files
    redFile = open('red.txt', 'w')
    greenFile = open('green.txt', 'w')
    blueFile = open('blue.txt', 'w')

    # Gather pixels on separate lists
    redPixels = list(myImage.getdata(band=0))
    greenPixels = list(myImage.getdata(band=1))
    bluePixels = list(myImage.getdata(band=2))

    # Write pixel values to files
    for  i in range(imageHeight * imageWidth):
        if i % imageWidth == 0:
            redFile.write("\n")
            greenFile.write("\n")
            blueFile.write("\n")
        redFile.write(getValToWrite(redPixels[i]))
        greenFile.write(getValToWrite(greenPixels[i]))
        blueFile.write(getValToWrite(bluePixels[i]))

    # Close pixel files
    redFile.close()
    greenFile.close()
    blueFile.close()
    return

if __name__ == '__main__':
    loadPixels()

    