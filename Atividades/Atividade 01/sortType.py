#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Current Implementation of sort types
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# precisa ordernar em pelo menos 2 formas
#    crescente e decresente
#    
# TODO:
#       Decidir o que pasar para as funções
#       Fazer as funções
#       Fazer as metricas das funções
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Debug Flags
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
debugMsg = True
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# insertionSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def insertionSort(array,mode):
    # the function not change the original array
    # the sorted array is passed by return 
    mode = str(mode)
    
    # mode == c or mode == d 
    if not mode == "c" and not mode == "d" and not mode == "r":
        print("[ERROR]: Invalid mode!")
        print("[ERROR]: Exiting program!")
        exit()
    
    # verify array size is valid
    if len(array) < 1:
        print("[ERROR]: Invalid array size!")
        print("[ERROR]: Exiting program!")
        exit()

    arrayToSort = array.copy()
    
    #sorting array by insertion
    for index in range(1,len(arrayToSort)):
        currentVal = arrayToSort[index]
        currentPos = index
        # move the value to correct position
        while currentPos > 0 and arrayToSort[currentPos-1] > currentVal:
            arrayToSort[currentPos] = arrayToSort[currentPos-1]
            currentPos -= 1
        # set the correct value in the position
        arrayToSort[currentPos] = currentVal
        
    # after sorting check the mode to return...
    if mode == "c" or mode == "r":
        return arrayToSort
    else:
        arrayToSort.reverse()
        return arrayToSort

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# selectionSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# def selectionSort():
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# bubbleSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def bubbleSort(array):
    # the function not change the original array
    # the sorted array is passed by return 
    # mode = str(mode)
    
    # # mode == c or mode == d 
    # if not mode == "c" and not mode == "d" and not mode == "r":
    #     print("[ERROR]: Invalid mode!")
    #     print("[ERROR]: Exiting program!")
    #     exit()
    
    # verify array size is valid
    if len(array) < 1:
        print("[ERROR]: Invalid array size!")
        print("[ERROR]: Exiting program!")
        exit()
    changed = True
    
    arrayToSort = array.copy()
    numComp = 0
    
    while changed == True:
        changed = False
        print(arrayToSort)
        for index in range(len(arrayToSort) - 1):
            if arrayToSort[index] > arrayToSort[index + 1]:
                numComp += 1
                arrayToSort[index],arrayToSort[index + 1] = arrayToSort[index + 1],arrayToSort[index]
                changed = True
    
    return arrayToSort,numComp
    
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
