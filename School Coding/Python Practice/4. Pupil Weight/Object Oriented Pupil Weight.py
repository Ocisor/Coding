class pupil():
    def __init__(self, weight, name, diff):
        self.diff = diff
        self.weight = weight
        self.name = name
    
    def returnName(self):
        return self.name
    def returnWeight(self):
        return self.weight
    def returnDiff(self):
        return self.diff
    
    def updName(self):
        self.name = input("Current name is invalid. Please input an appropriate one.")
    def updWeight(self):
        self.weight = int(input("Current Weight is invalid. Please input an appropriate one."))


class students():
    def __init__(self, size):
        self.size = size
        self.students = [pupil(-1,"",0) for i in range(self.size)]
    
    def inputData(self,pupilIndex):
        while self.students[pupilIndex].returnName() == "":
            self.students[pupilIndex].updName()
        while self.students[pupilIndex].returnWeight() < 0 or self.students[pupilIndex].returnWeight() > 150:
            self.students[pupilIndex].updWeight()
    
    def populatePupilRecords(self):
        for i in range(self.size):
            self.inputData(i)
    
    def calcDiff(self):
        for i in range(self.size):
            finalWeight = input("Final Weight")
            self.students[i].diff = abs(self.students[i].returnName() - finalWeight)
        
    def outCome(self, pupilID):
        if self.students[pupilID].diff > 2.5:
            print("Change beyond 2.5kg.")