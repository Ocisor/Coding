class Queue:
    #Initialising queue length (size) and the data stored within. Along with the pointer.
    def __init__(self, size):
        self.size = size
        self.data = ["" for i in range(self.size)]
        self.pointer = 0

    #Getter for data
    def DisplayQueue(self):
        print(self.data)

    def enQueue(self, nData): #nData is newData
        if self.pointer < self.size:
            #Adds data to the queue.
            self.data[self.pointer] = nData
            self.pointer += 1
            print(f"En-queued data {nData}")
            self.DisplayQueue()
        else:
            print("Queue is full.")

    def deQueue(self):
        if self.pointer != 0: #Checks the queue is not empty.
            print(f"De-queued data {self.data[0]}.")
            self.DisplayQueue()
            #Dequeues initial element
            for i in range(self.size):
                if (i+1) < self.size:
                    self.data[i] = self.data[i+1]
            self.pointer -= 1
        else:
            print("Queue is empty.")
