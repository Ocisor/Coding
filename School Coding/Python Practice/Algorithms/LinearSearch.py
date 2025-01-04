dataSet = ["Sam","Bob"]  #Empty but any data can be put in 

def linSearch(searchTerm, data):
    for i in range(len(data)):
        if data[i] == searchTerm:
            return i
    return -1

print(linSearch("Sam", dataSet))


#Returns position of the search term