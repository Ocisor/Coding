import random
bubbleList = [random.randint(0,100000) for _ in range(30)]

flag = False
temp = 0
location = 0

while not flag:
  flag = True
  location = 0
  while location < (len(bubbleList)-1):

    if bubbleList[location] > bubbleList[location+1]:
      temp = bubbleList[location+1]
      bubbleList[location+1] = bubbleList[location]
      bubbleList[location] = temp
      flag = False

    location += 1

for i in range (len(bubbleList)):
  print(bubbleList[i])