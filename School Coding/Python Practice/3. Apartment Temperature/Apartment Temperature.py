#Initialising variables for the program to run
maxTemp = 0.0
minTemp = 99.0
outOfRange = 0

def dataCheck(data):#Checks data's ranges
  if data < 36:
    print("Temperature too low!")
    return(1)
  elif data > 37.5:
    print("Temperature too high")
    return(1)
  else:
    print("Good temps.")
    return(0)

for i in range(0,17): #Checks 17 values
  dataStore = input("Input data")
  #Checking and setting max and min temperatures
  if dataStore > maxTemp:
    maxTemp = dataStore
  if dataStore < minTemp:
    minTemp = dataStore

  outOfRange = outOfRange + dataCheck(dataStore)

range = maxTemp-minTemp #Calculating range

#Printing summary of data
print("Max, min and range of temps are:")
print(f"{maxTemp}\n{minTemp}\n{range}")

if outOfRange > 2:
  print("The room's temperature went beyond the acceptable range more than three times.")
if range > 1:
  print("The room's temperature varies too much. ")