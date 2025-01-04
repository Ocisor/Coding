#Stacks require data to be pushed and popped. Data is not actually overwritten, but the top location is changed.
#Create a stack as a class. Pass in its size. 

class Stack:
    def __init__(self, size):
        self.size = size
        self.data = ["" for i in range(self.size)]
        self.top = 0 # A pointer for the top of the stack.
    
    #Getter for the data
    def DisplayStack(self):
        print(self.data)
    
    def Push(self, pData): # (pData is pushed Data)
        if self.top < self.size: #Checks there is room
            self.data[self.top] = pData #Adds new data at the top of the stack. Designated by the pointer
            self.top += 1
            self.DisplayStack() #Displaying the updated stack
        else:
            print("Stack is full. Cannot Push.")
    
    def Pop(self):
        if self.top > 0:
            self.top -= 1
            print(f"Popped value {self.data[self.top]}") #Returning the popped value by printing it
            self.DisplayStack() #Displaying the updated stack
        else:
            print("Stack is empty. Cannot Pop.")
