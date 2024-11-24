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
        self.tempist = [Node(self.list)]
        
        #Maybe create a new instance of the linked list object. But with an increased length of one.
        #For this reason. The actual variable name shouldnt matter, as it will be changed. But instead,
        #pass in the name you want the linked list to have as a parameter.

l1 = LinkedList(3)
