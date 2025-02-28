class Node():
    def __init__(self, element, left = None, right = None):
        self.content = element
        self.left = left
        self.right = right
    
    def details(self):
        print(self.content)
        print(f"Left: {self.left}")
        print(f"Right: {self.right}")

class BinaryTree():
    def __init__(self, rootValue):
        self.root = Node(rootValue)
    
    def display(self):
        pass

    def addNode(self, element):
        pass
    
    def findNextLoc(self, root): #Recursive
        if root.left == None:
            return root.left
        elif root.right == None:
            return root.right
        else:
            self.findNextLoc(root.left)

b1 = BinaryTree(10)
print(b1.findNextLoc)