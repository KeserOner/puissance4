__author__ = 'bajai'
import bestaplayer
import os
from time import sleep

class GameMaster:

    def __init__(self, fichier, player):
        self.bot_player = bestaplayer.BestaPlayer(fichier, player)
        self.grid = self.bot_player.grille
        self.fichier = fichier

    def displayGrid(self):
        """
        Implements function to display the current grid of play.

        """
        os.system('clear')
        for line in self.grid:
            print ' '.join(line) + '\n'

    def updateFileFromGrid(self):
        """
        Implements function that update the file after a player give a token.
        """
        with open(self.fichier, 'w') as fi:
            for line in self.grid:
                fi.write(line)

    def playAShot(self, col, player):
        """
        Implements function to play a turn.
        :param col: the column player wanna play in.
        """
        if self.grid[0][col] != '0':
            return False
        elif self.grid[5][col] == '0':
            li = list(self.grid[5])
            li[col] = str(player)
            self.grid[5] = ''.join(li)
            return True
        else:
            for x in xrange(6):
                if self.grid[x][col] != '0':
                    li = list(self.grid[x - 1])
                    li[col] = str(player)
                    self.grid[x - 1] = ''.join(li)
                    return True

    def checkWinDiagonalRightToLeft(self, player):
        """
        Implements function to check if there's a winning antidiagonal.

        :param player: which tokens to check.
        :return:
        """

        x = 3
        flag = False
        while x < 6:
            count = 0
            x_int = x
            y_int = 6
            while x_int >= 0:
                if int(self.grid[x_int][y_int]) == player and not flag:
                    count = 1
                    flag = True
                elif int(self.grid[x_int][y_int]) == player and flag:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
                    flag = False
                x_int -= 1
                y_int -= 1
            x += 1

        y = 5
        flag = False
        while y <= 3:
            count = 0
            x_int = 5
            y_int = y
            while y_int >= 3 and x_int >= 0:
                if int(self.grid[x_int][y_int]) == player and not flag:
                    count = 1
                    flag = True
                elif int(self.grid[x_int][y_int]) == player and flag:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
                    flage = False
                x_int -= 1
                y_int -= 1
            y -= 1

        return False

    def checkWinDiagonalLeftToRight(self, player):
        """
        Implements function to check there is a / winning diagonal.

        :param player: which token to check.
        :return:
        """

        x = 3
        flag = False
        while x < 6:
            count = 0
            x_int = x
            y_int = 0
            while x_int >= 0:
                if int(self.grid[x_int][y_int]) == player and not flag:
                    count = 1
                    flag = True
                elif int(self.grid[x_int][y_int]) == player and flag:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
                    flag = False
                x_int -= 1
                y_int += 1
            x += 1

        y = 1
        flag = False
        while y <= 3:
            count = 0
            x_int = 5
            y_int = y
            while y_int <= 6 and x_int >= 0:
                if int(self.grid[x_int][y_int]) == player and not flag:
                    count = 1
                    flag = True
                elif int(self.grid[x_int][y_int]) == player and flag:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
                    flage = False
                x_int -= 1
                y_int += 1
            y += 1

        return False

    def resetGridFile(self):
        """
        Implements function to reset the file containing grid.
        :return:
        """
        with open(self.fichier, 'w') as fi:
            for x in xrange(6):
                fi.write('0000000\n')

    def checkWinDiagonals(self, player):
        """
        Implements function to check if there's a winning diagonal.
        :param player: which token to check
        :return:
        """
        return self.checkWinDiagonalLeftToRight(player) or self.checkWinDiagonalRightToLeft(player)

    def changeColumnInLines(self):
        """
        Implements function to transform columns in lines to make tests eaiser.
        :return: a reverse matrice
        """
        column = []
        for y in xrange(7):
            col = ''
            for x in xrange(6):
                col += self.grid[x][y]
            column.append(col)
        return column

    def checkWinColumns(self, player):
        """
        Implements function to check if there is a winning column.

        :param player: which token to check.
        :return: true or false

        """

        column = self.changeColumnInLines()
        flag = False
        for line in column:
            count = 0
            for car in line:
                if int(car) == player and not flag:
                    count = 1
                    flag = True
                elif int(car) == player and flag:
                    count += 1
                    if count == 4:
                        return True
                else:
                    flag = False
                    count = 0
        return False

    def checkWinLines(self, player):
        """
        Implements function to check if there is a winning line.

        :param player: which token to check.
        :return: true or false

        """
        flag = False
        for line in self.grid:
            count = 0
            for car in line[:len(line) - 1]:
                if int(car) == player and not flag:
                    count = 1
                    flag = True
                elif int(car) == player and flag:
                    count += 1
                    if count == 4:
                        return True
                else:
                    flag = False
                    count = 0
        return False

    def someoneWinGame(self, player):
        """
        Implement function to check if someone win.
        :param player: token to check
        :return: True or False
        """
        return self.checkWinColumns(player) or self.checkWinDiagonals(player) or self.checkWinLines(player)

    def gridFull(self):
        """
        Implement function to check if the grid is full.
        :return: True or False
        """
        for line in self.grid:
            for car in line:
                if car == '0':
                    return False
        return True

    def playTheGame(self):
        """
        Implements main function of the class
        """
        self.displayGrid()
        player = True
        self.bot_player.players = 2, 1
        while not (self.someoneWinGame(1) or self.someoneWinGame(2)) or self.gridFull():
            if player:
                col = input('Choose a column to play : ')
                while col > 7 or col < 1:
                    col = input('Choose a column (number between 1 and 7')
                col -= 1
                while not self.playAShot(col, 1):
                    col = input('This column is full, choose another one : ')
                player = False

            else:
                col = self.bot_player.decideColumn()
                self.playAShot(col, 2)
                sleep(1)
                player = True
                print 'Bot has played'

            self.updateFileFromGrid()
            self.displayGrid()

        if self.someoneWinGame(1):
            print 'You win !'
        elif self.someoneWinGame(2):
            print 'You loose ...'
        else:
            print 'No winner, no looser !'
        self.resetGridFile()

gm = GameMaster('grille.txt', (2, 1))
gm.playTheGame()
