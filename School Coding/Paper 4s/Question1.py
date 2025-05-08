class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

linkedList = [node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2), node(0,6), node(0,8), node(56,3), node(0,9), node(0,-1)] 
startPointer = 0
emptyList = 5

def outputNodes(array, start):
    next = start
    for i in range(len(array)):
        print(array[next].data)
        next = array[next].nextNode

outputNodes(linkedList, startPointer)

def addNode(array, start, empty):
    pass