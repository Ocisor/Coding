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

    def display(self): #Displays attributes
        print(f"Data is: {self.data}\nPointer is: {self.pointer}")

class LinkedList:
    def __init__(self, length):
        #Initialising the linked lit with parameter for length. Creates a list of Node objects.
        self.len = length
        self.list = [Node("",(i+1)) for i in range(self.len)]
        self.list[self.len-1].pointer = -1
        self.sPoint = 0 #Declaring start pointer
        self.fPoint = 0 #Declaring free pointer
        #Both start at 0 as fPoint points to the first free node. Which at the start is the same as the sPoint.

    def display(self):
        currentNode = self.sPoint
        for i in range(self.len): #Here i is not actually used. It is simply used to iterate the number of times necessary
            print(f"Current node data is: {self.list[currentNode].data}\nPoints to: {self.list[currentNode].pointer}\n")
            currentNode = self.list[currentNode].pointer




    def updFree(self): #Not going to be called outside of the class. Just used to update the freePointer
        index = 0
        flag = False
        while index < self.len: #Not <= because length of a list is one greater than the last index (zero indexed)
            if self.list[index].data == "":
                self.fPoint = index
                flag = True
            index += 1
        if not flag:
            self.fPoint = -1
    

    def addData(self,data):
        if self.fPoint == -1:
            print("List is full. Remove data or append a new node.")
        else:
            self.list[self.fPoint] = data

'''
    def appendNode(self):
        self.templist = [Node("",i+1) for i in range(self.len + 1)]
        for j in range(self.len):
            self.list[j] = self.templist[j]
        self.len += 1
        self.list = self.templist
'''

l1 = LinkedList(5)
l1.display()