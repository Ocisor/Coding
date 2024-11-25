def insertionSort(data):
    for i in range(1,len(data)): #Iterate through each element. Starting at 1 bcs the first item is "already sorted".
        temp = data[i] #Sets the piece of data that needs to be sorted to the variable temp.
        checkPos = i-1 #Checking the position before the piece of data being re-inserted. checkPos ---> Check Position
        while checkPos >= 0 and temp < data[i]: #Checking that the checkPos is still within bounds and if should switch.
            data[checkPos + 1] = data[checkPos] # Moving each piece of data forward one.
            checkPos -= 1
        


#[4,5,3,7]
#Use index 0 as a key. Check index key + 1.
#If     
#