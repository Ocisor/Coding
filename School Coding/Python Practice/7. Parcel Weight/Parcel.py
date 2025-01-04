class parcel():
    def __init__(self):
        self.dims = [0,0,0]
        #dims is an array [x, y, z]
        self.weight = 0
    
    def inputDims(self):


    def checkDims(self): #Dims is short for dimensions
        self.totalDims = 0
        for i in range(3):
            if self.dims[i] > 80 or self.dims[i] <= 0:
                self.dims[i] = int(input(f"Value no.{i+1} is out of bounds. Please reinput: "))
            self.totalDims += self.dims[i]
        if self.totalDims > 200:


        
    




ParcelOne = parcel([x, y, z], weight) #Variables are placeholders as of now for demonstration purposes.