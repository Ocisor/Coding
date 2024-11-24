#Linked lists are made up of nodes. These contain two dataPoints each. A value and a pointer to the next node
class Node: # Initialising the Node class
    def __init__(self, data, pointer):
        #Taking in the parameters for the data stored in the node and the location of the next node.
        self.data = data
        self.pointer = pointer
    
    def uPoint(self,newLocation): #uPoint stands for update Pointer
        self.pointer = newLocation
    
    def uData(self,newData): # uData stands for update Data
        self.data = newData

    def dis(self): #Displays attributes
        print(f"Data is: {self.data}\nPointer is: {self.pointer}")

class LinkedList:
    def __init__(self, length):
        #Initialising the linked lit with parameter for length. Creates a list of Node objects.
        self.length = length
        self.list = [Node("",(i+1)) for i in range(self.length)]

    def appendNode(self):
        self.templist = [Node("",i+1) for i in range(self.length + 1)]
        for j in range(self.length):
            self.list[j] = self.templist[j]
        self.length += 1
        self.list = self.templist
        
    def display(self):
        for object in self.list:
            print(f"Data is: {object.data}\nPointer is: {object.pointer}")
        print("display complete")

l1 = LinkedList(3)
l1.display()
l1.appendNode()
l1.display()