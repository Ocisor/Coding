def GetStart(location, FNstring): #location is the number of the word in the string "ANT BEAR SAND" for the word BEAR, location is 2.
    sCount = 0 # Space Count
    cCount = 0 # Charactar Count
    checked = False
    for char in FNstring:
        if char == " ":
            sCount += 1
        if sCount > location:
            checked = True
        