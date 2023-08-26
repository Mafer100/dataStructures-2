#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Current Implementation of sort types
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# A função deve aceitar somente um array e retorna-lo ordenado
# quem deve lidar com os casos de ordenamento é o programa...
# caso necessite que a função realize o ordenamento:
    # mode = str(mode)
    # # mode == c or mode == d 
    # if not mode == "c" and not mode == "d" and not mode == "r":
    #     print("[ERROR]: Invalid mode!")
    #     print("[ERROR]: Exiting program!")
    #     exit()
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Imports
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import numpy as np
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Debug Flags
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
debugMsg = True
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Aux Functions
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Generating Arrays
def arrayGenerate(arraySize,mode):
    
    # need to evaluete if this "if" is really necessary...
    if arraySize < 1:
        print("[ERROR]: Invalid arguments!")
        exit()
        
    if mode == "r":
        arrayReturn = np.random.randint(32000,size=arraySize)
    else:
        arrayReturn = list(range(1,arraySize + 1))
        np.random.shuffle(arrayReturn)
    
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

# def mergeSort():
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# quickSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# def quickSort():

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# heapSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# def heapSort():

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# TODO: Escolher um tipo de ordenamento e implementa-lo
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
