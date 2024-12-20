def donationSystem():
    
    #Declaring Data Structures
    charities = []
    choice = 0

    for i in range(3):
        charities.append([input(f"Input Charity no.{i+1} "),0])

    print("\n\nCandidate options are:")
    for i in range(3):
        print(f"{i+1}. {charities[i]}")
    choice = input("What is your choice?")
    bill = input("What is your shopping bill?")
    donation = bill * 0.01

    charities[choice][1] += donation
    print(f"Donated {charities[choice][1]} to {charities[choice][1]}.")

    for i in range(3):
        print(f"Total for {charities[i][0]} is {charities[choice][1]}.")

donationSystem()