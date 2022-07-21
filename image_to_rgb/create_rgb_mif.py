from PIL import Image
import write_mif_file as mifWriter

def createPixelColorArray(imagePath:str): 
    with Image.open(imagePath, 'r') as myImage:
        redPixels = list(myImage.getdata(band=0))
        greenPixels = list(myImage.getdata(band=1))
        bluePixels = list(myImage.getdata(band=2))
    
    return redPixels, greenPixels, bluePixels

def convertListToDict(pixelArray: list[int]):
    pixelDict = {}
    for i, val in enumerate(pixelArray):
        pixelDict[i] = val

    return pixelDict

def generateMifs(pixelArray: list[int], fileName:str):
    pixelDict = convertListToDict(pixelArray=pixelArray)
    mifWriter.writeMifFile(dataWidth=8, dataDepth=len(pixelArray), data=pixelDict, filepath=fileName)

def createMifFileFromImage(imagePath:str):
    redPixels, greenPixels, bluePixels = createPixelColorArray(imagePath=imagePath)
    generateMifs(pixelArray=redPixels, fileName="red.mif")
    generateMifs(pixelArray=greenPixels, fileName="green.mif")
    generateMifs(pixelArray=bluePixels, fileName="blue.mif")

if __name__ == '__main__':
    createMifFileFromImage(imagePath="./assests/emojiforfpgaresized.jpg")
