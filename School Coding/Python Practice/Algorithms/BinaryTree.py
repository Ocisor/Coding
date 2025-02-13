class Node():
    def __init__(self, element, index, left, right):
        self.content = element
        self.index = index
        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self):
        self.tree = [None]
    
    def addNode(self, element):
        pass