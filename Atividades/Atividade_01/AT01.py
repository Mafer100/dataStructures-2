import sys
import arraySorting as sort

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Debug Flags
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
debugMsg        = False
debugFastFile   = True
debugInputName  = "test.txt"
debugOutputName = "output.txt"
# End
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Error and Debug handling
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
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
    sort.debugMsg = True
# End

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Main Function
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def main(input,output):
    if debugMsg:
        print("[DEBUG]: Input name:",input)
        print("[DEBUG]: Output name:",output)
        
    inFile  = open(input,"r")
    outFile = open(output,"w")
    
    arraySize = inFile.readline()
    arraySize = arraySize.strip()
    
    if arraySize == '':
        print("[ERROR]: Empty File!")
        exit()
    
    if not arraySize.isdecimal():
        print("[ERROR]: The first line of the file is not a number!")
        exit()
    else:
        arraySize = int(arraySize)

    arrayOrder = inFile.readline()    
    arrayOrder = arrayOrder.strip()
    arrayOrder = arrayOrder.lower()
     
    if not (arrayOrder == 'c' or arrayOrder == 'd' or arrayOrder == 'r'):
        print("[ERROR]: The second line is not any of the possible options!")
        exit()
    # All files open, just need to make things happen...
    
    # generate array
    arrayToSort = sort.arrayGenerate(arraySize,arrayOrder)
    outFile.writelines(["[INFO]: The generated array is: ",str(arrayToSort),"\n\n"])
    
    print("[INFO]: Sorting arrays...")
    
    if len(arrayToSort) >= 5000:
        print("[INFO]: If array is too large,this may take a while!")
    
    # sort array
    insertionSorted,insertionComparisons,insertionTimer = sort.insertionSort(arrayToSort) 
    selectionSorted,selectionComparisons,selectionTimer = sort.selectionSort(arrayToSort)
    bubbleSorted,bubbleComparisons,bubbleTimer = sort.bubbleSort(arrayToSort)
    mergeSorted,mergeComparisons,mergeTimer = sort.mergeSort(arrayToSort)
    quickSorted,quickComparisons,quickTimer = sort.quickSort(arrayToSort)
    heapSorted,heapComparisons,heapTimer = sort.heapSort(arrayToSort)
    treeSorted,treeComparisons,treeTimer = sort.treeSort(arrayToSort)
    
    # write to output file
    outFile.writelines(["[Insertion Sort]: ",str(insertionSorted)," | ",str(insertionComparisons)," comparisons | ",str(insertionTimer)," ms\n"],)
    outFile.writelines(["[Selection Sort]: ",str(selectionSorted)," | ",str(selectionComparisons)," comparisons | ",str(selectionTimer)," ms\n"],)
    outFile.writelines(["[Bubble Sort]:    ",str(bubbleSorted)," | ",str(bubbleComparisons)," comparisons | ",str(bubbleTimer)," ms\n"],)
    outFile.writelines(["[Merge Sort]:     ",str(mergeSorted)," | ",str(mergeComparisons)," comparisons | ",str(mergeTimer)," ms\n"],)
    outFile.writelines(["[Quick Sort]:     ",str(quickSorted)," | ",str(quickComparisons)," comparisons | ",str(quickTimer)," ms\n"],)
    outFile.writelines(["[Heap Sort]:      ",str(heapSorted)," | ",str(heapComparisons)," comparisons | ",str(heapTimer)," ms\n"],)
    outFile.writelines(["[Tree Sort]:      ",str(treeSorted)," | ",str(treeComparisons)," comparisons | ",str(treeTimer)," ms\n"],)
    
    # Close files 
    inFile.close()
    outFile.close()
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

if __name__ == '__main__':
    if debugFastFile:
        main(debugInputName,debugOutputName)
    else:
        main(inputFile,outputFile)