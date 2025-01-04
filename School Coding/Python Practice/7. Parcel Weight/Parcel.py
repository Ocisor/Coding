class parcel():
    def __init__(self, dimensions, weight):
        self.dimensions = dimensions
        #dimensions is an array [x, y, z]
        self.weight = weight
    
    def checkDims(self): #Check Dimensions
        for i in range(3):
            if self.dimensions[i] > 80 or self.dimensions[i] <= 0:
                print(f"Value no.{i+1} is out of bounds. Please reinput: ")

ParcelOne = parcel([x, y, z], weight)