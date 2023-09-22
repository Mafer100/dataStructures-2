#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Current Implementation of sort types
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# A função deve aceitar somente um array e retorna-lo ordenado
# quem deve lidar com os casos de ordenamento é o programa...

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Imports
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import numpy as np
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Debug Flags
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
debugMsg    = False
# debubOutput = False
# debugFastFile   = True
# debugInputName  = "test.txt"
# debugOutputName = "output.txt"
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Aux Functions
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Generating Arrays
def arrayGenerate(arraySize,mode):
    
    # need to evaluate if this "if" is really necessary...
    if arraySize < 1:
        print("[ERROR]: Invalid arguments!")
        exit()
        
    if mode == "r":
        arrayReturn = np.random.randint(32000,size=arraySize)
    else:
        arrayReturn = list(range(1,arraySize + 1))
        if mode == "d":
            arrayReturn.reverse()
        elif mode == "rc" or mode == "rd":
            np.random.shuffle(arrayReturn)
    
    if debugMsg:
        print("[INFO]: Array generated:",arrayReturn)
        
    return arrayReturn
# End

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# insertionSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def insertionSort(array):
    # the function not change the original array
    # the sorted array is passed by return 
    
    # verify array size is valid
    if len(array) < 1:
        print("[ERROR]: Invalid array size!")
        print("[ERROR]: Exiting program!")
        exit()

    arrayToSort = array.copy()
    
    # Numbem of comparisions done
    comparisionCounter = 0
    
    #sorting array by insertion
    for index in range(1,len(arrayToSort)):
        currentVal = arrayToSort[index]
        currentPos = index
        # move the value to correct position
        while currentPos > 0 and arrayToSort[currentPos-1] > currentVal:
            arrayToSort[currentPos] = arrayToSort[currentPos-1]
            currentPos -= 1
            comparisionCounter += 1
        # set the correct value in the position
        arrayToSort[currentPos] = currentVal
        
    return arrayToSort,comparisionCounter
# end

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# selectionSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def selectionSort(array):
    # the function not change the original array
    # the sorted array is passed by return 
    
    # verify array size is valid
    if len(array) < 1:
        print("[ERROR]: Invalid array size!")
        print("[ERROR]: Exiting program!")
        exit()

    arrayToSort = array.copy()
    # print("[INFO]: ",arrayToSort)
    
    numIterations,numComparisions = 0,0
    
    for index in range(len(arrayToSort)):
        currentMinIndex = index
        numIterations += 1
        for currentPos in range(currentMinIndex,len(arrayToSort)):
            numComparisions += 1
            if arrayToSort[currentPos] < arrayToSort[currentMinIndex]:
                currentMinIndex = currentPos
        # swap positions
        (arrayToSort[index],arrayToSort[currentMinIndex]) = (arrayToSort[currentMinIndex],arrayToSort[index])
        # print("[INFO]: ",arrayToSort,"|",numIterations)

    # print("[INFO]: ",arrayToSort,"|",numIterations,"|",numComparisions)
    return arrayToSort
# end

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# bubbleSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def bubbleSort(array):
    # the function not change the original array
    # the sorted array is passed by return 
    
    # verify array size is valid
    if len(array) < 1:
        print("[ERROR]: Invalid array size!")
        print("[ERROR]: Exiting program!")
        exit()
        
    arrayToSort = array.copy()
    
    # Verify if array changed positions after a iteration, if not changed the array is sorted
    # this is done to achieve a better optimization
    isChanged = True
    
    # Numbem of comparisions done
    comparisionCounter = 0
    
    while isChanged == True:
        isChanged = False
        print(arrayToSort)
        for index in range(len(arrayToSort) - 1):
            comparisionCounter += 1
            if arrayToSort[index] > arrayToSort[index + 1]:
                arrayToSort[index],arrayToSort[index + 1] = arrayToSort[index + 1],arrayToSort[index]
                isChanged = True
    
    return arrayToSort,comparisionCounter
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# mergeSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Função recursiva!!

def mergeSort(array):
    # verify array size is valid
    # TODO: Verify the behavior of this check
    # if len(array) < 1:
    #     print("[ERROR]: Invalid array size!")
    #     print("[ERROR]: Exiting program!")
    #     exit()
    
    # base case for recursion 
    if len(array) <= 1:
        return(array)
    
    arrayToSort = array.copy()
    
    # get the middle of array
    arrayMiddle = len(arrayToSort) // 2
    
    # go to right and left side recursively
    rightSide = mergeSort(arrayToSort[:arrayMiddle])
    leftSide  = mergeSort(arrayToSort[arrayMiddle:])
    
    return mergeAux(rightSide,leftSide)

# aux merging function
def mergeAux(rightSide,leftSide):
    rightIndex = 0
    leftIndex  = 0
    
    arrayReturn = []
    
    while leftIndex < len(leftSide) and rightIndex < len(rightSide):
        if leftSide[leftIndex] < rightSide[rightIndex]:
            arrayReturn.append(leftSide[leftIndex])
            leftIndex += 1    
        else:
            arrayReturn.append(rightSide[rightIndex])
            rightIndex += 1

    arrayReturn += rightSide[rightIndex:]
    arrayReturn += leftSide[leftIndex:]
    
    return arrayReturn
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# quickSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# TODO:Implement random pivot quick sort

def quickSort(array,start=None,end=None):
    # the function not change the original array
    # the sorted array is passed by return 
    # verify if array size is valid
    
    #check if is the first iteration
    if start == None or end == None:
        # BUG: If the size of array is <= 2, the function doesnt sort correctly
        if len(array) <= 0:
            print("[ERROR]: Invalid array size!")
            print("[ERROR]: Exiting program!")
            exit()
        
        start = 0
        end   = (len(array) - 1)
        
        # if is the first iteration create "arrayToSort"
        # this is because we dont want to change the "original" array
        global arrayToSort
        arrayToSort = array.copy()
        
    if start < end:
        pivot = quickSortAux(arrayToSort,start,end)
        quickSort(arrayToSort,start,pivot-1)
        quickSort(arrayToSort,pivot+1,end)
            
    return arrayToSort
    
    
    
def quickSortAux(array,startPos,endPos):
   
    pivotVal  = array[startPos]
    leftSide  = startPos + 1
    rightSide = endPos
    
    completeFlag = False
    while not completeFlag:
        
        while leftSide <= rightSide and array[leftSide] <= pivotVal:
            leftSide = leftSide + 1
        
        while rightSide >= leftSide and array[rightSide] >= pivotVal:
            rightSide = rightSide - 1
        
        if leftSide > rightSide:
            completeFlag = True
        else:
            array[leftSide],array[rightSide] = array[rightSide],array[leftSide]

    array[startPos],array[rightSide] = array[rightSide],array[startPos]
    
    return rightSide
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# heapSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def heapSort(array):
    arrayToSort = array.copy()
    
    heapSize = len(arrayToSort)
    createMaxHeap(arrayToSort,heapSize)
    
    for pos in range(len(arrayToSort)-1,0,-1):
        # swap
        arrayToSort[0],arrayToSort[pos] = arrayToSort[pos],arrayToSort[0]
        
        heapSize -= 1
        heapify(arrayToSort,0,heapSize)

    return arrayToSort

def createMaxHeap(array,heapSize):
    positions = range(len(array)//2,-1,-1)
    
    for pos in positions:
        heapify(array,pos,heapSize)

def heapify(array,pos,heapSize):
    left  = (2*pos) + 1
    right = (2*pos) + 2
    largest = pos
    
    if left  <= (heapSize -1) and array[left] > array[pos]:
        largest = left
        
    if right <= (heapSize -1) and array[right] > array[largest]:
        largest = right
    
    if pos != largest:
        # swap
        array[largest],array[pos] = array[pos],array[largest]
        heapify(array,largest,heapSize-1)
    
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# TODO: Implementar tree sort e/ou burst sort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-