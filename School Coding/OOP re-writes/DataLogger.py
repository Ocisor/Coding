class day:
    def __init__(self, tDay, tNight):
        self._day = tDay
        self._night = tNight

    def reValue(self, time): 
        if time == 0:
            return(self._day)
        else:
            return(self._night)
    
class month:
    def __init__(self, len):
        self.days = [day(int(input(f"Day {i} temp: ")),int(input(f"Night {i} temp: "))) for i in range(len)]
        self.len = len
        self.avrg = [0,0]
        self.max = [self.days[0].reValue(0),self.days[0].reValue(1)]
        self.min = [self.days[0].reValue(0),self.days[0].reValue(1)]
    
    def findAvg(self):
        for i in range(2):
            for j in range(self.len):
                self.avrg[i] += self.days[j].reValue(i)
            self.avrg[i] /= self.len
        return self.avrg
    
    def maxTemp(self):
        for i in range(2):
            for j in range(self.len):
                if self.max[i] < self.days[j].reValue(i):
                    self.max[i] = self.days[j].reValue(i)
        return self.max
    
    def minTemp(self):
        for i in range(2):
            for j in range(self.len):
                if self.min[i] > self.days[j].reValue(i):
                    self.min[i] = self.days[j].reValue(i)
        return self.min

    
June = month(3)
print(June.findAvg())
    
