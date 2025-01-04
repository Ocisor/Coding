class parcel():
    def __init__(self):
        self.dims = [0,0,0]
        self.inputDims()
        #dims is an array [x, y, z]
        self.weight = 0
        self.reinput = False #Allows one chance for data to be reinput before rejection
    
    def inputDims(self):
        for i in range(3):
            self.dims[i] = input(f"Please input dimension {i+1}")
        self.checkDims()

    def checkDims(self): #Dims is short for dimensions
        self.totalDims = 0
        for i in range(3):
            if self.dims[i] > 80 or self.dims[i] <= 0:
                self.dims[i] = int(input(f"Value no.{i+1} is out of bounds. Please reinput: "))
            self.totalDims += self.dims[i]
        if self.totalDims > 200 and not self.reinput:
            print("Total dimensions over 200. Reinput incase of user error")
            self.inputDims()
        if self.reinput:
            print("Parcel Rejected")
            del self
        

        
    




ParcelOne = parcel([x, y, z], weight) #Variables are placeholders as of now for demonstration purposes.