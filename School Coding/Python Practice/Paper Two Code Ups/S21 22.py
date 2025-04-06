def GetStart(location, FNstring): #location is the number of the word in the string "ANT BEAR SAND" for the word BEAR, location is 2.
    sCount = 0 # Space Count
    cCount = 0 # Character Count
    checked = False
    for char in FNstring:
        if not checked:
            if char == " ":
                sCount += 1
                cCount -= 1
            if sCount > location:
                checked = True
            else:
                cCount += 1
    return FNstring[(sCount+cCount)-1]
print(GetStart(2, "Sand Wich"))