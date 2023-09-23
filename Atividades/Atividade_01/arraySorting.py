#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Current Implementation of sort types
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# A função deve aceitar somente um array e retorna-lo ordenado
# quem deve lidar com os casos de ordenamento é o programa...

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Imports
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# only for arraygenerate LOL
import numpy as np
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Debug Flags
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
debugMsg    = False
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
        print("[INFO]: Array generated: ",arrayReturn)
        
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
        
    if debugMsg:
        print("[INFO][insertionSort]: Array sorted: ",arrayToSort)
        
    return arrayToSort
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
     
    for index in range(len(arrayToSort)):
        currentMinIndex = index
        for currentPos in range(currentMinIndex,len(arrayToSort)):
            if arrayToSort[currentPos] < arrayToSort[currentMinIndex]:
                currentMinIndex = currentPos
        # swap positions
        (arrayToSort[index],arrayToSort[currentMinIndex]) = (arrayToSort[currentMinIndex],arrayToSort[index])
        
    if debugMsg:
        print("[INFO][selectionSort]: Array sorted: ",arrayToSort)

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
        print("[ERROR][bubbleSort]: Invalid array size!")
        print("[ERROR][bubbleSort]: Exiting program!")
        exit()
        
    arrayToSort = array.copy()
    
    # Verify if array changed positions after a iteration, if not changed the array is sorted
    # this is done to achieve a better optimization
    isChanged = True
     
    while isChanged == True:
        isChanged = False
        print(arrayToSort)
        for index in range(len(arrayToSort) - 1):
            if arrayToSort[index] > arrayToSort[index + 1]:
                arrayToSort[index],arrayToSort[index + 1] = arrayToSort[index + 1],arrayToSort[index]
                isChanged = True
                
    if debugMsg:
        print("[INFO][bubbleSort]: Array sorted: ",arrayToSort)
    
    return arrayToSort
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# mergeSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Função recursiva!!

def mergeSort(array):
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
    
    if debugMsg:
        print("[INFO][mergeSort]: Returning array: ",arrayReturn)
    
    return arrayReturn
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# quickSort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# TODO:Implement random pivot and last element quick sort

def quickSort(array,start=None,end=None):
    # the function not change the original array
    # the sorted array is passed by return 
    # verify if array size is valid
    
    #check if is the first iteration
    if start == None or end == None:
        if len(array) <= 0:
            print("[ERROR][quickSort]: Invalid array size!")
            print("[ERROR][quickSort]: Exiting program!")
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
        
    if debugMsg:
        print("[INFO][quickSort]: Returning array: ",arrayToSort)
            
    return arrayToSort
    
    
    
def quickSortAux(array,startPos,endPos):
    # AKA partition function
   
    pivotVal  = array[startPos]
    leftSide  = startPos + 1
    rightSide = endPos
    
    
    # for some reason this need a "do-while"
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

    # swap
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

    if debugMsg:
        print("[INFO][heapSort]: Array sorted: ",arrayToSort)
        
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
    
    def insert(self,value):
        self.__insertAux(self.root,value)
            
    def __insertAux(self,node,value):
        if node == None:
            newNode = treeNode(value)
            return newNode
        
        if node.value == None:
            node.value = value
        elif value < node.value:
            node.left = self.__insertAux(node.left,value)
        elif value >= node.value:
            node.right = self.__insertAux(node.right,value)
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
    
    binaryTree.arrayInsert(array)
    
    arrayReturn = binaryTree.inOrderRet()
    
    # destroy tree
    del binaryTree
    
    if debugMsg:
        print("[INFO][heapSort]: Array sorted: ",arrayReturn)
        
    return arrayReturn

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Burst Sort
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Infelizmente não achei nenhum artigo confiável de alguma implementação
# que não seja em string, deveria ser uma variação do radix sort com 
# quick sort , enfim tudo o que achei fala sobre como lidar com strings

# é muito util para array que possuem muitos elementos "iguais"