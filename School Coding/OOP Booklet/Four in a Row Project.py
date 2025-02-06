class Game():
    def __init__(self):
        b = Board(7, 6)
        p1 = Player(input("What is your name? "), 'X')
        p2 = Player(input("What is your name? "), 'O')
        while True:
            b.display()
            p1.makeMove(b)
            b.display()
            p2.makeMove(b)

class Board():
    def __init__(self, columns, rows):
        self._columns = columns
        self._rows = rows
        self._board = [['+' for i in range(self._columns)] for i in range(self._rows)]
        #self._board = [['+','O','+','+','+','+','+'],['+','O','+','+','+','+','+'],['+','O','+','+','+','+','+'],['+','O','+','+','+','+','+'],['+','O','+','+','+','+','+'],['+','O','+','+','+','+','+']]

    def stripBoard(self, line):
        strippedLine = '  '.join(line)
        return strippedLine

    def display(self):
        for line in self._board:
            print(f"|{self.stripBoard(line)}|")
    
    def columnFull(self, colIndex):
        tempCol = []
        for i in range(self._rows):
            tempCol.append(self._board[i][colIndex])
        if '+' not in tempCol:
            return True
        return False

    def boardFull(self):
        full = True
        for i in range(self._rows):
            if '+' in self._board[i]:
                full = False
        return full
    
    def getWidth(self):
        return self._columns
    def getHeight(self):
        return self._rows
    
    def addToken(self, pID):
        success = False
        if self.boardFull():
            success = True
        while not success:
            choice = int(input("Which column do you want to place your token in? (zero indexed)"))
            if not self.columnFull(choice):
                for i in range(self.getHeight()-1, -1, -1):
                    if not success and self._board[i][choice] == '+':
                        self._board[i][choice] = pID
                        success = True
            if not success:
                print("Cannot place here. Try again.")

            
            

class Player():
    def __init__(self, name, pID):
        self._name = name
        self._pID = pID
        print(f"{name}, your token is: {self._pID}.")
    
    def getName(self):
        return self._name
    def getID(self):
        return self._pID
    
    def makeMove(self, board):
        board.addToken(self._pID)


g = Game()
