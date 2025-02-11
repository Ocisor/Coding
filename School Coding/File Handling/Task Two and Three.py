l = [["Josh", 50], ["Joe", 60], ["Jim", 55]]
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
            set.append(line[:(len(line)-1)])
        else:
            set.append(line[:(len(line)-1)])
            fileContents.append(set)
            print(f"{set[0]} has {set[1]} marks.")
        count += 1
    
    return fileContents

fileContents = display(path)