from io import TextIOWrapper
import constants

# Add File parameter headers
def addNewHeader(name:str, value:str, fp:TextIOWrapper, sc:bool = True) -> int:
    if sc:
        return fp.write(name + value + ';' + constants.NEWLINE)
    return fp.write(name + value + constants.NEWLINE)

# Add a blank line to the file
def addBlankLine(fp:TextIOWrapper) -> int:
    return fp.write(constants.NEWLINE)

# write a single value to the file
def writeSingleAddress(fp: TextIOWrapper, addr: int, value: int) -> int:
    return fp.write(constants.TAB + str(addr) + constants.COLON + str(value) + ';' + constants.NEWLINE)

# Write a dictionary containing address, value as key , value pair in the dictionary
def writeDicttoMifFile(fp: TextIOWrapper, data:dict[int, int]):
    for key, value in data.items():
        writeSingleAddress(fp=fp, addr=key, value=value)

# write headers to the file
def writeHeaders(fp: TextIOWrapper, dataWidth: int, dataDepth:int):
    addNewHeader(fp=fp, name=constants.WIDTH, value=str(dataWidth))
    addNewHeader(fp=fp, name=constants.DEPTH, value=str(dataDepth))
    addBlankLine(fp=fp)
    addNewHeader(fp=fp, name=constants.ADDR_RADIX, value=constants.UNS)
    addNewHeader(fp=fp, name=constants.DATA_RADIX, value=constants.UNS)
    addBlankLine(fp=fp)
    return 

# write dtavalues to the file
def writeData(fp:TextIOWrapper, data:dict[int, int]):
    addNewHeader(fp= fp, name=constants.CONTENT_BEGIN, value=constants.BLANK, sc= False)
    writeDicttoMifFile(fp=fp, data=data)
    addNewHeader(fp=fp, name=constants.END, value="")

# Write values
def writeMifFile(dataWidth:int, dataDepth:int, data:dict[int, int], filepath:str):
    with open(filepath, 'w') as mifFile:
        print("File Opened Successfully")
        writeHeaders(fp=mifFile, dataDepth=dataDepth, dataWidth=dataWidth)
        writeData(fp=mifFile, data=data)


if __name__ == '__main__':
    dataDict = {}
    for i in range(256):
        dataDict[i] = (i + 1) % 256
    writeMifFile(dataWidth=8, dataDepth=256, data=dataDict, filepath="red.mif")

