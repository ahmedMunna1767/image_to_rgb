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

# Write Pixel Values to file
def writeToFile(imageWidth, file, pixels):
    for i, pixel in enumerate(pixels):
        if i % imageWidth == 0:
            file.write('\n')
        file.write(getValToWrite(pixel=pixel))
    return

# Separate red, green, blue pixel values into separate files
def loadPixels():
    # Open Image file
    with Image.open("./assests/emojiforfpgaresized.jpg", 'r') as myImage:
        imageWidth = myImage.size[0]
        redPixels = list(myImage.getdata(band=0))
        greenPixels = list(myImage.getdata(band=1))
        bluePixels = list(myImage.getdata(band=2))

    # Write all the red values
    with open('red.txt', 'w') as redFile:
        writeToFile(imageWidth=imageWidth, file=redFile, pixels=redPixels)

    # Write all the green values
    with open('green.txt', 'w') as greenFile:
        writeToFile(imageWidth=imageWidth, file=greenFile, pixels=greenPixels)

    # Write all the blue values
    with open('blue.txt', 'w') as blueFile:
        writeToFile(imageWidth=imageWidth, file=blueFile, pixels=bluePixels)
        
    return

if __name__ == '__main__':
    loadPixels()

    