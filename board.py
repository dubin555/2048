import random
from keypress import _Getch,keypress
import sys

class board(object):

    __SIZE = 4
    __SCORE = 0

    def __init__(self):
        self.boardArray = [[0 for i in range(self.__SIZE)] for j in range(self.__SIZE)]

    def printBoard(self):
        size = self.__SIZE
        for i in range(size):
            print "    ".join(map(lambda x: x if x!= "0" else " ",(str(self.boardArray[i][j]) for j in range(size))))
        print "-------   Score ->",self.__SCORE
    def getEmptyPosition(self):
        res = []
        size = self.__SIZE
        for row in range(size):
            for col in range(size):
                if self.boardArray[row][col] == 0:
                    res.append([row,col])
        return res

    def setNewBoard(self):
        if self.cannotContinue() and self.noRoomToPlace():sys.exit()
        if self.noRoomToPlace() : return
        emptyPosition = self.getEmptyPosition()
        temp = random.randint(0,len(emptyPosition)-1)
        addRowPos,addColPos = emptyPosition[temp]
        newValue = random.choice([2,2,2,4])
        self.boardArray[addRowPos][addColPos] = newValue

    def parserRowHorizontal(self,row,direction):
        length = len(row)
        row = filter(lambda x:x>0,row)
        if direction == "right":
            for i in range(len(row)-1,-1,-1):
                if i-1>=0 and row[i] == row[i-1]:
                    row[i] = row[i]+row[i-1]
                    self.__SCORE += row[i]
                    row[i-1] = 0
            temp = filter(lambda x:x>0,row)
            res = [0]*(length-len(temp))+temp
            return res
        elif direction == "left":
            for i in range(len(row)):
                if i+1<=len(row)-1 and row[i] == row[i+1]:
                    row[i] = row[i]+row[i+1]
                    self.__SCORE += row[i]
                    row[i+1] = 0
            temp = filter(lambda x:x>0,row)
            res = temp+[0]*(length-len(temp))
            return res


    def combinateSameHorizontal(self,direction):
        size = self.__SIZE
        if direction == "left" or direction == "right":
            for row in range(size):
                newRow = self.parserRowHorizontal(self.boardArray[row],direction)
                self.boardArray[row] = newRow
        elif direction == "up" or direction == "down":
            for col in range(size):
                column = [self.boardArray[row][col] for row in range(size)]
                if direction == "up":
                    newCol = self.parserRowHorizontal(column,"left")
                else:
                    newCol = self.parserRowHorizontal(column,"right")
                for row in range(size):
                    self.boardArray[row][col] = newCol[row]

    def noRoomToPlace(self):
        if len(self.getEmptyPosition()) == 0:return True
        else:return False

    def cannotContinue(self):
        size = self.__SIZE
        for row in range(size):
            for col in range(size):
                if col+1 < size and self.boardArray[row][col] == self.boardArray[row][col+1]:
                    return False
                if row+1 < size and self.boardArray[row][col] == self.boardArray[row+1][col]:
                    return False
        return True

if __name__ == "__main__":
    b = board()
    keyboard = keypress()
    while True:
        b.setNewBoard()
        b.printBoard()
        direction = keyboard.get()
        b.combinateSameHorizontal(direction)
        b.printBoard()
