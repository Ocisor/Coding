l = [["Rachel", 0], ["Jake", 90], ["Henrik", 89], ["Sam", 100]]
path = "namesAndMarks.txt"
f = open(path, "w")
for entry in l:
    for col in entry:
        f.write(str(col) + "\n")
f.close()

def display(path):
    count = 0
    f = open(path, "r")
    fileContents = []
    for line in f:
        if count % 2 == 0:
            set = []
            set.append(line[:(len(line)-1)])      #      :(len(line)-1)       This strips the \n from the end of the string.
        else:
            set.append(line[:(len(line)-1)])
            fileContents.append(set)
            print(f"{set[0]} has {set[1]} marks.")
        count += 1
    f.close()
    return fileContents

fileContents = display(path)

class Pupil():
    def __init__(self, path, nameLoc):
        self._mark = None
        self._fPath = path
        file = open(path, "r")
        f = file.readlines()
        self._name = f[nameLoc]
        self._name = self._name[:(len(self._name)-1)]
        self._mark = f[nameLoc + 1]
        self._mark = self._mark[:(len(self._name)-1)]

        file.close()
    
    def getName(self):
        return self._name
    def getMark(self):
        return self._mark
    
    def dispDetails(self):
        print(f"{self._name} has {self._mark}")

class Class():
    def __init__(self, path):
        self._path = path
        self._students = [Pupil(self._path, i) for i in range(0, self.sizeOfFile(), 2)]
    
    def sizeOfFile(self):
        f = open(self._path, "r")
        lines = 0
        for line in f:
            lines +=1
        f.close()
        return lines

    def studentDetails(self):
        for student in self._students:
            student.dispDetails()

class1 = Class(path)
class1.studentDetails()
print(class1._students)