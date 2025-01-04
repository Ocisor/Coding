class room:
    def __init__(self):
        self.temperatures = []
        self.outOfBounds = 0

    
    def returnName(self):
        return self._name
    def returnAge(self):
        return self._age
    def getOlder(self):
        return self._age + 1
    
    def takeTemperature(self, newTemp):
        while newTemp > 45 or newTemp < 30:
            print("Eroneous input.")
            newTemp = int(input("Please re-input temperature: "))
        self.temperatures.append(newTemp)
        if newTemp < 21.5:
            print("Temperature too low!")
            self.outOfBounds += 1
        elif newTemp > 24.5:
            print("Temperature too high")
            self.outOfBounds += 1
        else:
            print("Good temps.")
    
    def extremes(self):
        max = 30
        min = 45
        for temp in self.temperatures:
            if temp > max:
                max = temp
            if temp < min:
                min = temp
        print("The max temperature was: ", max)
        print("The min temperature was: ", min)
        print(f"The range was {max-min}.")

    def bounds(self):
        print(f"The room has been beyond the extremes {self.outOfBounds} many times")
        self.extremes()