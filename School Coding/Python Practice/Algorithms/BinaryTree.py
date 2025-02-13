class Node():
    def __init__(self, element, left = None, right = None):
        self.content = element
        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self, rootValue):
        self.root = Node(rootValue)
    
    def addNode(self, element):
        pass