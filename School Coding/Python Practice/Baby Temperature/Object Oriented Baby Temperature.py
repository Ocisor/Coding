class baby:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.temperatures = []
    
    def returnName(self):
        return self._name
    def returnAge(self):
        return self._age
    def getOlder(self):
        return self._age + 1
    
    def takeTemperature(self, newTemp):
        while newTemp > 50 or newTemp < 20:
            print("Eroneous input. (or the baby is dead)")
            newTemp = int(input("Please re-input temperature: "))
        self.temperatures.append(newTemp)
        if newTemp < 36:
            print("Temperature too low!")
            return(1)
        elif newTemp > 37.5:
            print("Temperature too high")
            return(1)
        else:
            print("Good temps.")
            return(0)