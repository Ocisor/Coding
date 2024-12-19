stuDiff = []
stuWeights = [
[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],
[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],
[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],
[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],
[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],
[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]
stuNames = []
check = 0.0

for i in range(29):
  stuNames.append(str(input("Input Pupil Name.")))
  stuWeights[i][0] = float(input(f"What is the weight of {stuNames[i]}?\n"))
  while stuWeights[i][0] < 10 and stuWeights[i][0] > 300:
    stuWeights[i][0] = float(input(f"Input value of range. Please re-input.\n"))

for i in range(29):
  stuWeights[i][1] = float(input(f"What is the new weight of {stuNames[i]}?\n"))
  while stuWeights[i][1] < 10 and stuWeights[i][1] > 300:
    stuWeights[i][1] = float(input(f"Input value of range. Please re-input.\n"))
  stuDiff.append(stuWeights[i][0] - stuWeights[i][1])
  print(f"The original weight of {stuNames[i]} was {stuWeights[i][0]}. It has now become {stuWeights[i][1]}.")
  print(f"This means the range was {stuDiff[i]}")
  if stuDiff[i] > 2.5:
    print(f"They had a significant change of {stuDiff[i]}.")