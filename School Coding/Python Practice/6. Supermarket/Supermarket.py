#Declaring Data Structures and setting up charities
totals = []
for i in range(3):
    totals.append([input(f"Input Charity no.{i+1} "),0])

#Function for each user to donate and see the options
def donationSystem(charities):
    choice = -2

    #Displaying candidates
    print("\n\nCandidate options are:")
    for i in range(3):
        print(f"{i+1}. {charities[i]}")
    while choice < 0 or choice > 3:    
        choice = int(input("As a number 1-3 what is your choice? ")) - 1 #Inputting and validating charity choice.
    bill = int(input("What is your shopping bill? "))
    donation = bill * 0.01
    print(charities)
    charities[choice][1] += donation
    print(f"Donated {charities[choice][1]} to {charities[choice][0]}.") #Summary of users action

    for i in range(3):
        print(f"Total for {charities[i][0]} is {charities[i][1]}.") #Totals

    return charities


while True:
    totals = donationSystem(totals) 