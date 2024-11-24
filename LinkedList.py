#Linked lists are made up of nodes. These contain two dataPoints each. A value and a pointer to the next node
class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer
    
    def updatePointer(self,newLocation):
        self.pointer = newLocation
    
    def updateData(self,newData):
        self.data = newData

    def dis(self):
        print(f"Data is: {self.data}\nPointer is: {self.pointer}")

class LinkedList:
    def __init__(self, length):
        self.length = length
        self.list = [Node("",(i+1)) for i in range(self.length)]

    def appendNode(self):
        self.templist = [Node("",i+1) for i in range(self.length + 1)]
        self.tempist = [Node(self.list)]
        
        #Maybe create a new instance of the linked list object. But with an increased length of one.
        #For this reason. The actual variable name shouldnt matter, as it will be changed. But instead,
        #pass in the name you want the linked list to have as a parameter.

l1 = LinkedList(3)
 