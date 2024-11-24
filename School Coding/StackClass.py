#Stacks require data to be pushed and popped. Data is not actually overwritten, but the top location is changed.
#Create a stack as a class. Pass in its size. 

class Stack:
    def __init__(self, size):
        self.size = size
        self.data = ["" for i in range(self.size)]
        self.top = 0 # A pointer for the top of the stack.
    
    def DisplayStack(self):
        print(self.data)
    
    def Push(self, pData): # (pData is pushed Data)
        if self.top < self.size:
            self.data[self.top] = pData
            self.top += 1
            self.DisplayStack()
        else:
            print("Stack is full. Cannot Push.")
    
    def Pop(self):
        if self.top > 0:
            self.top -= 1
            print(f"Popped value {self.data[self.top]}")
            self.DisplayStack()
        else:
            print("Stack is empty. Cannot Pop.")

            