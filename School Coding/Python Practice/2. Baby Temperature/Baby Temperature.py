maxTemp = 0.0
minTemp = 99.0
outOfRange = 0

def dataCheck(data):
  if data < 36:
    print("Temperature too low!")
    return(1)
  elif data > 37.5:
    print("Temperature too high")
    return(1)
  else:
    print("Good temps.")
    return(0)

for i in range(0,17):
  dataStore = input("Input data")

  if dataStore > maxTemp:
    maxTemp = dataStore
  if dataStore < minTemp:
    minTemp = dataStore

  outOfRange = outOfRange + dataCheck(dataStore)

range = maxTemp-minTemp

print("Max, min and range of temps are:")
print(f"{maxTemp}\n{minTemp}\n{range}")

if outOfRange > 2:
  print("The baby's temperature went beyond the acceptable range more than three times.")
if range > 1:
  print("The baby's temperature varies too much. ")