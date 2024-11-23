#Linked lists are made up of nodes. These contain two dataPoints each. A value and a pointer to the next node
class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer
    
    def updatePointer(self,newLocation):
        self.pointer = newLocation
    
    def updateData(self,newData):
        self.data = newData

class LinkedList:
    def __init__(self, length):
        self.length = length
        self.list = [Node("",(i+1)) for i in range(self.length)]

    def appendNode(self):
        pass

