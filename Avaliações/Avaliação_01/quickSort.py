def quickSortFirst(array,start=None,end=None):
    
    if start == None or end == None:
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
        quickSortFirst(arrayToSort,start,pivot-1)
        quickSortFirst(arrayToSort,pivot+1,end)
            
    return arrayToSort
    
def quickSortLast(array,start=None,end=None):

    if start == None or end == None:
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
        pivot = quickSortAuxLast(arrayToSort,start,end)
        quickSortLast(arrayToSort,start,pivot-1)
        quickSortLast(arrayToSort,pivot+1,end)
            
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

def quickSortAuxLast(array,startPos,endPos):
    pivotVal = array[endPos]
    left = startPos
    
    for index in range(startPos,len(array)):
        if array[index] < pivotVal:
            array[index],array[left] = array[left],array[index]
            left += 1
    
    array[left],array[endPos] = array[endPos],array[left]
    
    return left

def QuickSort(array, pivotChoice = "f"):
    
    if pivotChoice == "f":
        result = quickSortFirst(array)
        return result
        
    elif pivotChoice == "l":
        result = quickSortLast(array)
        return result
        
    else:
        print("[Error]: Invalid pivot choice")