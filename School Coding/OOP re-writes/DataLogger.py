class day:
    def __init__(self, tDay, tNight):
        self._day = tDay
        self._night = tNight

    def reDay(self): #   reDay == return day
        return(self._day)
    
    def reNight(self):
        return(self._night)
    
class month:
    def __init__(self, len):
        self.data = [day(input(f"Day {i} temp: "),input(f"Night {i} temp: ")) for i in range(len)]
        self.len = len
    
    def average(self):
        pass
