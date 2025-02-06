class Game():
    def __init__(self):
        b = Board(7, 6)
        p1 = Player(input("What is your name? "), 1)
        p2 = Player(input("What is your name? "), 2)

class Board():
    def __init__(self, columns, rows):
        self._columns = columns
        self._rows = rows
        self._board = [['+' for i in range(self._columns)] for i in range(self._rows)]
        self._board = [['+','O','+','+','+','+','+'],['+','O','+','+','+','+','+'],['+','O','+','+','+','+','+'],['+','O','+','+','+','+','+'],['+','O','+','+','+','+','+'],['+','O','+','+','+','+','+']]

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
        for i in range(self.getHeight()):
            if '+' in self._board[i]:
                full = False
        return full
    
    def getWidth(self):
        return self._columns
    def getHeight(self):
        return self._rows
    
    def addToken(self, player):
        pass

class Player():
    def __init__(self, name, pID):
        self._name = name
        self._pID = pID
    
    def getName(self):
        return self._name
    def getID(self):
        return self._pID
    
    def makeMove(self):
        pass


b1 = Board(7,6)
b1.display()
b1.columnFull(1) # REMEMBER IT IS ZERO INDEXED
b1.boardFull()
