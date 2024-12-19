classData = ["Anthony", "BEN", "caleb", "Dan", "Bob"]
classSize = len(classData)

#for i in range(classSize):
  #classData.append(input("Input a child's name: "))

def findUser(dataSet, searchTerm):
  for i in dataSet:
    if i.lower() == searchTerm.lower():
      return(dataSet.index(i))

class pupil():
  def __init__(self, name, votes):
    self.name = name.capitalize()
    self.votes = votes
    self.hasVoted = False

  def name(self):
    return(self.name)

  def details(self):
    print(self.name)
    print(self.votes)
    print(self.hasVoted,"\n")

  def vote(self, objs):
    if self.hasVoted:
      print("Vote already submitted.")
    while not self.hasVoted:
      choice = input(f"{self.name}, who do you want to vote for?")
      for i in range(len(objs)):
        if choice.lower() == objs[i].name.lower():
          objs[i].votedFor()

          self.hasVoted = True
      if not self.hasVoted:
        print("Invalid vote. Please try again.")


  def votedFor(self):
    self.votes += 1

  def login(self):
    pass


pupilObjs = [pupil(classData[i],0) for i in range(classSize)]
#pupilObjs[1].vote(pupilObjs)
pupilObjs[findUser(classData, str(input("Enter username: ")))]

for i in range(classSize):
  pupilObjs[i].details()