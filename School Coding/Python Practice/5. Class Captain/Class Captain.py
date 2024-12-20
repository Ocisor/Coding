def ChooseCandidate(candidateNumber, numberOfVotes):

    #Declaring and empty list to store candidate's names in
    candidates = [["",0]]
    choice = 0
    voteNumber = numberOfVotes
    tie = False
    mostVotes = 0

    #Inputting Candidate Names
    for i in range(candidateNumber):
        candidates[i][0] = input(f"Who is candidate number {i + 1}")

    #Displaying and Choosing Candidates.
    while choice != -1 and voteNumber < 30:
        print("\n\n\nThe candidates are: ")
        for i in range(candidateNumber):
            print(f"{i+1}. {candidates[i]}")
        choice = input("Who is your vote? \n(enter the number not the name)")
        if choice == -1:
            print("Voting ended.")
        elif choice <= numberOfVotes and choice > -1:
            candidates[choice][1] += 1
            voteNumber += 1
        else:
            print("Invalid vote, vote rejected.")
            voteNumber += 1
    
    #Displaying final standings
    for i in range(1, (numberOfVotes-1)):
        if candidates[mostVotes][1] < candidates[i][1]:
            mostVotes = i
        elif candidates[mostVotes][1] == candidates[i][1]:
            tie = True
    if not tie:
        print(f"New class captain is: {candidates[mostVotes][0]}.")
    else:
        print("No clear winner.")