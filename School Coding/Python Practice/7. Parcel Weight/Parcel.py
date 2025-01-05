class parcel():
    def __init__(self, parcelNumber):
        self.parcelNumber = parcelNumber
        #dims is an array [x, y, z]
        self.dims = [0,0,0]
        self.weight = 0
        self.statusCode = 0
        self.status = True
        #Inputting values
        print(f"This is Parcel number {self.parcelNumber}:\n")
        self.inputTotalDims()
        self.inputWeight()
        self.reinputIndivDims = False
        self.reinputTotalDims = False #Allows one chance for dimensions to be reinput before rejection
        self.reinputWeight = False #Allows one chance for weight to be reinput before rejection
    
    def inputDims(self):
        for i in range(3):
            self.dims[i] = input(f"Please input dimension {i+1}")
        self.checkDims()
    
    def inputWeight(self):
        self.weight = int(input("What is the parcel weight?"))
        self.checkWeight()

    def checkDims(self): #Dims is short for dimensions
        self.totalDims = 0
        for i in range(3):
            if self.dims[i] > 80 or self.dims[i] <= 0:
                self.dims[i] = int(input(f"Value no.{i+1} is out of bounds. Please reinput: "))
                self.reinputIndivDims = True
            self.totalDims += self.dims[i]
        if self.totalDims > 200 and not self.reinputTotalDims:
            print("Total dimensions over 200. Reinput incase of user error: ")
            self.reinputTotalDims = True
            self.inputDims()
        if self.totalDims > 200 and self.reinputTotalDims:
            self.statusCode += 1
        for i in range(3):
            if self.dims[i] > 80 or self.dims[i] <= 0 and self.reinputIndivDims:
                self.statusCode += 2
    
    def checkWeight(self):
        if self.weight <= 1 or self.weight >= 10 and not self.reinputWeight:
            print("Weight outide of limit. Please reinput incase of user error: ")
            self.reinputWeight = True
            self.inputWeight()
        if self.weight <= 1 or self.weight >= 10:
            self.statusCode += 4
        self.parcelStatus()

    def parcelStatus(self):
        match self.statusCode:
            case 0:
                print("No issues with parcel.")
            case 1:
                print("One or more dimensions out of bounds.")
            case 2:
                print("Total dimensions exceeds limits.")
            case 3:
                print("Both one or more dimensions out of bounds, and total dimensions exceeding limits.")
            case 4:
                print("Weight out of bounds.")
            case 5:
                print("One or more dimensions out of bounds. One or more dimensions out of bounds.")
            case 6:
                print("One or more dimensions out of bounds. And, total dimensions exceed limits.")
            case 7:
                print("It's all wrong. Idk why you thought you could get this parcel in.")   
        if self.statusCode > 0:
            self.status = False

class consignment():
    def __init__(self,numberOfParcels):
        self.parcelList = [parcel(i) for i in range(numberOfParcels)]
        self.NumOfParcels = numberOfParcels
        self.totalWeight = 0
        self.trimParcelList()
        print(self.sumWeight())
    
    def trimParcelList(self):
        toRemove = []
        j = 0
        for i in range(self.NumOfParcels):
            if not self.parcelList[i].status:
                toRemove.append(i - j)
                j += 1
        for i in range(len(toRemove)):
            del self.parcelList[toRemove[i]]

    def sumWeight(self):
        for i in range(self.NumOfParcels):
            self.totalWeight += self.parcelList[i].weight
        return self.totalWeight





#  ParcelOne = parcel([x, y, z], weight)            Variables are placeholders as of now for demonstration purposes.