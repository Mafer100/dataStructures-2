#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Current Implementation of sort types
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# A função deve aceitar somente um array e retorna-lo ordenado
# quem deve lidar com os casos de ordenamento é o programa...

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Imports
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# numpy only for arraygenerate LOL
import numpy as np
# time for timer
import time
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Debug Flags
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
debugMsg    = False
debugTimer  = False
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Auxiliar Functions
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

class timeCounter(object):
    def __init__(self):
        self.initTime  = 0
        self.endTime   = 0
        self.deltaTime = None
        
    def startTimer(self):
        self.initTime = time.perf_counter()
        # seconds to miliseconds
        self.initTime = self.initTime * 1000
        
        return self.initTime
        
    def stopTimer(self):
        self.endTime = time.perf_counter()
        # seconds to miliseconds
        self.endTime = self.endTime * 1000
        
        self.generateDeltaTime()
        
        return self.deltaTime
    
    def generateDeltaTime(self):
        self.deltaTime = self.endTime - self.initTime
        
        # round value
        # use 2 decimal digits for precision
        self.deltaTime = round(self.deltaTime,2)
        
        return self.deltaTime
        
# Generating Arrays
def arrayGenerate(arraySize,mode):
    # need to evaluate if this "if" is really necessary...
    if arraySize < 1:
        print("[ERROR]: Invalid arguments!")
        exit()
        
    timer = timeCounter()
    timer.startTimer()
     
    if mode == "r":
        arrayReturn = np.random.randint(32000,size=arraySize,dtype=int)
        # need this because numpy array are diferent of python arrays... 
        arrayReturn = arrayReturn.tolist()
    else:
        arrayReturn = list(range(1,arraySize + 1))
        if mode == "d":
            arrayReturn.reverse()
        elif mode == "rc" or mode == "rd":
            np.random.shuffle(arrayReturn)
    
    timer.stopTimer()
    
    if debugMsg:
        print("[INFO][arrayGenerate]: Array generated: ",arrayReturn)
        
    if debugTimer:
        print("[INFO][arrayGenerate]: Elapsed time to create array : ",timer.deltaTime,"ms")
        
        
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
        print("[ERROR][insertionSort]: Invalid array size!")
        print("[ERROR][insertionSort]: Exiting program!")
        exit()

    arrayToSort = array.copy()
    insertComparisonCounter = 0
    timer = timeCounter()
    
    timer.startTimer()
    
    #sorting array by insertion
    for index in range(1,len(arrayToSort)):
        currentVal = arrayToSort[index]
        currentPos = index
        # move the value to correct position
        while currentPos > 0 and arrayToSort[currentPos-1] > currentVal:
            insertComparisonCounter += 1
            arrayToSort[currentPos] = arrayToSort[currentPos-1]
            currentPos -= 1
        else:
            # else only for comparisons counter
            insertComparisonCounter += 1
        # set the correct value in the position
        arrayToSort[currentPos] = currentVal
    
    timer.stopTimer()
        
    if debugMsg:
        print("[INFO][insertionSort]: Array sorted: ",arrayToSort)
        
    if debugTimer:
        print("[INFO][insertionSort]: Elapsed time to sort array : ",timer.deltaTime,"ms")
        
    return arrayToSort,insertComparisonCounter,timer.deltaTime
# end

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# selectionSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def selectionSort(array):
    # the function not change the original array
    # the sorted array is passed by return 
    
    # verify array size is valid
    if len(array) < 1:
        print("[ERROR][selectionSort]: Invalid array size!")
        print("[ERROR][selectionSort]: Exiting program!")
        exit()

    arrayToSort = array.copy()
    selectionComparisonCounter = 0
    timer = timeCounter()
    
    # start timer
    timer.startTimer()
     
    for index in range(len(arrayToSort)):
        currentMinIndex = index
        for currentPos in range(currentMinIndex,len(arrayToSort)):
            selectionComparisonCounter += 1
            if arrayToSort[currentPos] < arrayToSort[currentMinIndex]:
                currentMinIndex = currentPos
        # swap positions
        (arrayToSort[index],arrayToSort[currentMinIndex]) = (arrayToSort[currentMinIndex],arrayToSort[index])
        
    timer.stopTimer()
        
    if debugMsg:
        print("[INFO][selectionSort]: Array sorted: ",arrayToSort)
        
    if debugTimer:
        print("[INFO][selectionSort]: Elapsed time to sort array : ",timer.deltaTime,"ms")

    return arrayToSort,selectionComparisonCounter,timer.deltaTime
# end

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# bubbleSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def bubbleSort(array):
    # the function not change the original array
    # the sorted array is passed by return 
    
    # verify array size is valid
    if len(array) < 1:
        print("[ERROR][bubbleSort]: Invalid array size!")
        print("[ERROR][bubbleSort]: Exiting program!")
        exit()
        
    arrayToSort = array.copy()
    bubbleComparisonCounter = 0
    timer = timeCounter()
    
    # Verify if array changed positions after a iteration, if not changed the array is sorted
    # this is done to achieve a better optimization
    
    timer.startTimer()
     
    isChanged = True
    while isChanged == True:
        isChanged = False
        for index in range(len(arrayToSort) - 1):
            bubbleComparisonCounter += 1
            if arrayToSort[index] > arrayToSort[index + 1]:
                arrayToSort[index],arrayToSort[index + 1] = arrayToSort[index + 1],arrayToSort[index]
                isChanged = True
                
    timer.stopTimer()
                
    if debugMsg:
        print("[INFO][bubbleSort]: Array sorted: ",arrayToSort)
        
    if debugTimer:
        print("[INFO][bubbleSort]: Elapsed time to sort array : ",timer.deltaTime,"ms")
    
    return arrayToSort,bubbleComparisonCounter,timer.deltaTime
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# mergeSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Função recursiva!!
# Needed to create a init function because comparison counter

def mergeSort(array):
    # verify array size is valid
    if len(array) < 1:
        print("[ERROR][mergeSort]: Invalid array size!")
        print("[ERROR][mergeSort]: Exiting program!")
        exit()
    
    # init values and create a copy of array
    global mergeComparisonCounter
    mergeComparisonCounter = 0
    arrayToSort = array.copy()
    timer = timeCounter()
    
    # start time before recursion
    timer.startTimer()
    
    result = mergeSortInit(arrayToSort)
    
    timer.stopTimer()
    
    if debugMsg:
        print("[INFO][mergeSort]: Array sorted: ",result)
    
    if debugTimer:
        print("[INFO][mergeSort]: Elapsed time to sort array : ",timer.deltaTime,"ms")
    
    return result,mergeComparisonCounter,timer.deltaTime

def mergeSortInit(array):
    # base case for recursion 
    if len(array) <= 1:
        return(array)
    
    global mergeComparisonCounter
     
    # get the middle of array
    arrayMiddle = len(array) // 2
    
    # go to right and left side recursively
    rightSide = mergeSortInit(array[:arrayMiddle])
    leftSide  = mergeSortInit(array[arrayMiddle:])
    
    return mergeAux(rightSide,leftSide)

# aux merging function
def mergeAux(rightSide,leftSide):
    rightIndex = 0
    leftIndex  = 0
    
    global mergeComparisonCounter
    
    arrayReturn = []
    
    while leftIndex < len(leftSide) and rightIndex < len(rightSide):
        if leftSide[leftIndex] < rightSide[rightIndex]:
            arrayReturn.append(leftSide[leftIndex])
            leftIndex += 1
            mergeComparisonCounter += 1 
        else:
            arrayReturn.append(rightSide[rightIndex])
            rightIndex += 1
            mergeComparisonCounter += 1 

    arrayReturn += rightSide[rightIndex:]
    arrayReturn += leftSide[leftIndex:]
    
    if debugMsg:
        print("[INFO][mergeSort]: Returning array: ",arrayReturn)
    
    return arrayReturn
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# quickSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# TODO:Implement random pivot and last element quick sort
# Needed to create a init function because comparison counter

def quickSort(array):
    if len(array) < 1:
            print("[ERROR][quickSort]: Invalid array size!")
            print("[ERROR][quickSort]: Exiting program!")
            exit()
        
    global quickComparisonCounter
    quickComparisonCounter = 0
    arrayToSort = array.copy()
    timer = timeCounter()
    
    # start time before recursion
    timer.startTimer()   
    
    result = quickSortInit(arrayToSort,0,len(arrayToSort)-1)
    
    timer.stopTimer()
    
    if debugMsg:
        print("[INFO][quickSort]: Array sorted: ",result)
        
    if debugTimer:
        print("[INFO][quickSort]: Elapsed time to sort array : ",timer.deltaTime,"ms")
    
    return result,quickComparisonCounter,timer.deltaTime

def quickSortInit(array,start,end):
    # the function not change the original array
    # the sorted array is passed by return 
    # verify if array size is valid
    
    global quickComparisonCounter
    
    if start < end:
        pivot = quickSortAux(array,start,end)
        quickSortInit(array,start,pivot-1)
        quickSortInit(array,pivot+1,end)
        
    if debugMsg:
        print("[INFO][quickSort]: Returning array: ",array)
            
    return array
    
def quickSortAux(array,startPos,endPos):
    # AKA partition function
   
    pivotVal  = array[startPos]
    leftSide  = startPos + 1
    rightSide = endPos
    
    global quickComparisonCounter
    
    # for some reason this need a "do-while"
    completeFlag = False
    while not completeFlag:
        
        while leftSide <= rightSide and array[leftSide] <= pivotVal:
            leftSide = leftSide + 1
            quickComparisonCounter += 1
        else:
            quickComparisonCounter += 1
    
        while rightSide >= leftSide and array[rightSide] >= pivotVal:
            rightSide = rightSide - 1
            quickComparisonCounter += 1
        else:
            quickComparisonCounter += 1
        
        if leftSide > rightSide:
            completeFlag = True
        else:
            array[leftSide],array[rightSide] = array[rightSide],array[leftSide]

    # swap
    array[startPos],array[rightSide] = array[rightSide],array[startPos]
    
    return rightSide

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# heapSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def heapSort(array):
    
    arrayToSort = array.copy()
    global heapComparisonCounter
    heapComparisonCounter = 0
    timer = timeCounter()
    
    timer.startTimer()
    
    heapSize = len(arrayToSort)
    createMaxHeap(arrayToSort,heapSize)
    
    for pos in range(len(arrayToSort)-1,0,-1):
        # swap
        arrayToSort[0],arrayToSort[pos] = arrayToSort[pos],arrayToSort[0]
        
        heapSize -= 1
        heapify(arrayToSort,0,heapSize)

    timer.stopTimer()
    
    if debugMsg:
        print("[INFO][heapSort]: Array sorted: ",arrayToSort)
        
    if debugTimer:
        print("[INFO][heapSort]: Elapsed time to sort array : ",timer.deltaTime,"ms")
        
    return arrayToSort,heapComparisonCounter,timer.deltaTime

def createMaxHeap(array,heapSize):
    positions = range(len(array)//2,-1,-1)
    
    for pos in positions:
        heapify(array,pos,heapSize)

def heapify(array,pos,heapSize):
    left  = (2*pos) + 1
    right = (2*pos) + 2
    largest = pos
    
    global heapComparisonCounter
    
    heapComparisonCounter += 1
    if left  <= (heapSize -1) and array[left] > array[pos]:
        largest = left
    
    heapComparisonCounter += 1
    if right <= (heapSize -1) and array[right] > array[largest]:
        largest = right
    
    heapComparisonCounter += 1
    if pos != largest:
        # swap
        array[largest],array[pos] = array[pos],array[largest]
        heapify(array,largest,heapSize-1)
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Binary Tree
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Implementação simples de uma arvore binaria de busca para o treeSort.

#    Não foi implementado outras formas de busca ou retornos como pre-ordem
# ou pos-ordem pq não precisa...

# TODO: Terminar funções auxiliares como pre-ordem e pos-ordem e busca na arvore... 
# assim como deletar algum elemento

class treeNode(object):
    def __init__(self,value = None):
        self.value  = value
        self.left   = None
        self.right  = None
        
class bTree(object):
    def __init__(self,rootValue = None):
        self.root = treeNode(rootValue)
        self.comparisonCounter = 0
    
    def insert(self,value):
        self.__insertAux(self.root,value)
            
    def __insertAux(self,node,value):
        if node == None:
            newNode = treeNode(value)
            return newNode
        
        if node.value == None:
            node.value = value
            self.comparisonCounter += 1
        elif value < node.value:
            node.left = self.__insertAux(node.left,value)
            self.comparisonCounter += 1
        elif value >= node.value:
            node.right = self.__insertAux(node.right,value)
            self.comparisonCounter += 1
        else:
            self.comparisonCounter += 1
            
        return node
    
    def inOrderPrint(self):
        global inOrderList
        inOrderList = []
        
        self.__inOrderAux(self.root)
        
        print(inOrderList)
        return inOrderList
        
    def __inOrderAux(self,node):
        global inOrderList
        if node != None:
            self.__inOrderAux(node.left)
            inOrderList.append(node.value)
            self.__inOrderAux(node.right)
            
    def inOrderRet(self):
        global inOrderList
        inOrderList = []
        
        self.__inOrderAux(self.root)
        
        return inOrderList
            
    def arrayInsert(self,array):
        for index in range(len(array)):
            self.insert(array[index])

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Tree Sort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def treeSort(array):
    binaryTree = bTree()
    
    # create and start timer
    timer = timeCounter()
    timer.startTimer()
    
    # insert array in btree
    binaryTree.arrayInsert(array)
    
    arrayReturn = binaryTree.inOrderRet()
    treeComparisonCounter = binaryTree.comparisonCounter
    
    timer.stopTimer()
    
    # destroy tree
    del binaryTree
    
    if debugMsg:
        print("[INFO][treeSort]: Array sorted: ",arrayReturn)
    
    if debugTimer:
        print("[INFO][treeSort]: Elapsed time to sort array : ",timer.deltaTime,"ms")
        
    return arrayReturn,treeComparisonCounter,timer.deltaTime

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Burst Sort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Infelizmente não achei nenhum artigo confiável de alguma implementação
# que não seja em string, deveria ser uma variação do radix sort com 
# quick sort , enfim tudo o que achei fala sobre como lidar com strings

# é muito util para array que possuem muitos elementos "iguais"