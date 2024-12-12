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
        self.data = [day(int(input(f"Day {i} temp: ")),int(input(f"Night {i} temp: "))) for i in range(len)]
        self.len = len
        self.avrg = [0,0]
    
    def findAvg(self):
        for i in range(2):
            for j in range(self.len):
                self.avrg[i] += self.data[i].reValue(i)
            self.avrg[i] /= self.len
        return self.avrg
    
June = month(3)
print(June.findAvg())
    
