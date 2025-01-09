class Account:
    def __init__(self, number, password, balance):
        #Acc is short for Account
        self.__accNumber = number
        self.__accPass = password
        self.__accBalance = balance



    def getNumber(self):
        return self.__accNumber
    def checkPassword(self, password):
        if self.__accPass == password:
            return True
        return False
    def getBalance(self):
        return self.__accBalance
    def setBalance(self, newBalance):
        self.__accBalance = newBalance

class Bank:
    def __init__(self, numberOfAccounts):
        self.__data = []
        self.__latestAccount = -1

    def accIndex(self, number):
        for i in range(len(self.__data)):
            if self.__data[i].getNumber() == number:
                return i
        return None

    def login(self):
        givenNum = int(input("Input Account Number: "))
        givenPass = input("Input Password: ")
        if self.__data:
            for i in range(len(self.__data)):
                if self.__data[i].getNumber() == givenNum:
                    if self.__data[i].checkPassword(givenPass):
                        return givenNum
        else:
            print("Error No Accounts!")

    def deposit(self, number):
        depositAmount = float(input("Input deposit amount: "))
        #Could throw an error if accIndex returned None. But won't because this can only be accessed while logged in.
        currentBalance = self.__data[self.accIndex(number)].getBalance()
        self.__data[self.accIndex(number)].setBalance(currentBalance + depositAmount)
    
    def withdraw(self, number):
        withdrawalAmount = float(input("Input withdrawal amount: "))
        currentBalance = self.__data[self.accIndex(number)].getBalance()
        self.__data[self.accIndex(number)].setBalance(currentBalance - withdrawalAmount)
    
    def checkBalance(self, number):
        print(f"You have £{self.__data[self.accIndex(number)].getBalance()} in your account.")

    def addAccount(self):
        if self.__latestAccount == -1:
            self.__data.append(Account(0,input("Please input a password: "), 0))
            print(f"Your bank number is 0.")
            self.__latestAccount += 1
        else:
            self.__data.append(Account((self.__latestAccount + 1),input("Please input a password: "), 0))
            print(f"Your bank number is {self.__latestAccount + 1}")
            self.__latestAccount += 1
    
    def main():
        bank = Bank()
        loggedIn = False
        quitting = False
        while not loggedIn and not quitting:
            response = input("Do you have an account? (y/n/quit): ")
            if response == "y":
                account = bank.login()
                if account != -1:
                    loggedIn = True
            elif response == "n":
                bank.addAccount()
            elif response == "quit":
                quitting = True
            
        while not quitting:
            option = str(input("Press 1 to check your balance\nPress 2 to deposit money\nPress 3 to withdraw money\nPress 4 to exit: "))
            match option:
                case "1":
                    bank.checkBalance(account)
                case "2":
                    bank.deposit(account)
                    bank.checkBalance(account)
                case "3":
                    bank.withdraw(account)
                    bank.checkBalance(account)
                case "4":
                    quitting = True
                case _:
                    print("Invalid option selected.")
    if __name__ == "__main__":
        main()