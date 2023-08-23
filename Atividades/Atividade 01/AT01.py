import sys
import arraySorting as sort


# Debug Flags
debugFastFile   = True
debugMsg        = True
debugInputName  = "test.txt"
debugOutputName = "output.txt"
# End

# Verificação de erros
if not debugFastFile and len(sys.argv) == 3:
    inputFile  = sys.argv[1]
    outputFile = sys.argv[2]
elif not debugFastFile and len(sys.argv) != 3:
    print("[ERROR]: Invalid number of arguments!")
    exit()
else:
    print("\n[INFO]: Fast Debug ON")
    print("[INFO]: Disabling arguments file names!")
    print("[INFO]: Input and Output file name are inside the code!\n")
    
if debugMsg:
    print("[INFO]: Degub messages is ON!\n")
# End
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def main(input,output):
    if debugMsg:
        print("[DEBUG]: Input name:",input)
        print("[DEBUG]: Output name:",output)
        
    inFile  = open(input,"r")
    outFile = open(output,"w")
    
    arraySize = inFile.readline()
    arraySize = arraySize.strip()
    
    if not arraySize.isdecimal():
        print("[ERROR]: The first line of the file is not a number!")
        exit()
    else:
        arraySize = int(arraySize)

    orderType = inFile.readline()    
    orderType = orderType.strip()
    orderType = orderType.lower()
     
    if not (orderType == 'c' or orderType == 'd' or orderType == 'r'):
        print("[ERROR]: The second line is not any of the possible options!")
        exit()
    # All files open, just need to make things happen...
    
    # Close files 
    inFile.close()
    outFile.close()
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

if __name__ == '__main__':
    if debugFastFile:
        main(debugInputName,debugOutputName)
    else:
        main(inputFile,outputFile)