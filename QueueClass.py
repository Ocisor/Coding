#Queues require data to be en-queued and de-queued.
#Create a queue as a class and pass in data.

class Queue:
    def __init__(self, size):
        self.size = size
        self.data = ["" for i in range(self.size)]
        self.pointer = 0

    def DisplayQueue(self):
        print(self.data)

    def enQueue(self, nData): #nData is newData
        if self.pointer < self.size:
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
            for i in range(self.size):
                if (i+1) < self.size:
                    self.data[i] = self.data[i+1]
            self.pointer -= 1
        else:
            print("Queue is empty.")

q = Queue(3)
while True:
    a = input("E or D: ")
    if a.upper() == "E":
        q.enQueue(input("What data do you want to queue? "))
    elif a.upper() == "D":
        q.deQueue()