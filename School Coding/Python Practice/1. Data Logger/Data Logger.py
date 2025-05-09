#Importing libraries to automatically fill out the arrays.
import random

#Initialising an array of empty values.
tempsDay = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
tempsNight = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]


#Function to check if a value is an integer.
def notInt(entry):
  try:
    int(entry)
    return False
  except ValueError:
    return True


def autoRecordTemps(tempsDay, tempsNight): #Automatically fill out the arrays with data for convenience
  for index in range (29):
    tempsDay[index] = random.randint(15,26)
    tempsNight[index] = random.randint(5,tempsDay[index])


def recordTemps(tempsDay, tempsNight): #Manual option to record temps
  for index in range (29):
    tempsDay[index] = input(f"What were the midday temperatures for day {index}\n")
    tempsNight[index] = input(f"What were the midnight temperatures for day {index}\n")


def validateTemps(tempsDay, tempsNight): #Validation of each index of the array AFTER entry
  for index in range (29):
    while notInt(tempsDay[index]):
      tempsDay[index] = input(f"Invalid midday data-type on day {index}. Re-input\n")
    while notInt(tempsNight[index]):
      tempsNight[index] = input(f"Invalid midnight data-type on day {index}. Re-input\n")

  for index in range (29):
    while tempsDay[index] > 40 or tempsDay[index] < -50:
      tempsDay[index] = input(f"Data outside of expected range. Please re-input.\n")
    while tempsNight[index] > 40 or tempsNight[index] < -50:
      tempsNight[index] = input(f"Data outside of expected range. Please re-input.\n")


def averageTemps(tempsDay, tempsNight): #Averages the temps of both day and night
  dayAv,nightAv = 0,0
  for index in range (29):
    dayAv += tempsDay[index]
    nightAv += tempsNight[index]
  dayAv = round(dayAv/30)
  nightAv = round(nightAv/30)

  print(f"The midday average this month was {dayAv}.")
  print(f"The midnight average this month was {nightAv}.")


#Test code to make the program run. Not necessary.
while True:
  entryType = input("Manual data entry? (y/n)\n")
  if entryType == "y" or entryType == "n":
    break
  print("Invalid response. \n(Respond with y or n.)")

if entryType == "y":
  recordTemps(tempsDay, tempsNight)
else:
  autoRecordTemps(tempsDay, tempsNight)

validateTemps(tempsDay, tempsNight)
averageTemps(tempsDay, tempsNight)