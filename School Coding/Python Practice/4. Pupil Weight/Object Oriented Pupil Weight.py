class pupil():
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name
    
    def returnName(self):
        return self.name
    def returnWeight(self):
        return self.weight

class students():
    def __init__(self, size):
        self.size = size
        self.students = [pupil(int(input(f"What is the weight of pupil number {i}: ")), str(input(f"What is the name of pupil number {i}: "))) for i in range(self.size)]

