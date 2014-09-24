__author__ = 'besta'


class BestaPlayer:

    def __init__(self, fichier):
        self.fichier = fichier
        self.grille = self.getFirstGrid()
        self.best_hit = 0
        self.player = self.whichPlayer()

    def getFirstGrid(self):
        """
        Implements function to get the first grid.

        :return: the grid.
        """
        li = []
        with open(self.fichier, 'r') as fi:
            for line in fi.readlines():
                li.append(line)
        return li

    def updateGrid(self):
        """
        Implements function to update the grid to alter n-1
        round values

        """
        with open(self.fichier, 'r') as fi:
            for line in fi.readlines():
                i = 0
                for car in line:
                    j = 0
                    if car != '\n':
                        self.grille[i][j] = car
                        j += 1
                    i += 1

    def displayGrid(self):
        """
        Implements function to display the current grid of play.

        """
        for line in self.grille:
            print ' '.join(line) + '\n'

    def whichPlayer(self):
        """
        Implement function to check if we are first or second player.

        """
        with open(self.fichier, 'r') as fi:
            for line in fi.readlines():
                for car in line[:len(line) - 1]:
                    if car != '0':
                        return 2
            return 1

    def grilleEmpty(self):
        """
        Implement function to check if the grid is empty.

        """
        for line in self.grille:
            for car in line[:len(line) - 1]:
                if car != '0':
                    return False
        return True

    def checkLines(self, player, inARow):
        """
        Implements function to check the current lines setup to evaluate best combinaison.

        :param player: check for your numbers (your player number) or those of your opponent.
        :param inARow: how many tokens in a row (3 or 2).
        :return: true or false

        """
        count = 0
        flag = False
        for line_number, line in enumerate(self.grille):
            count = 0
            for car in line[:len(line) - 1]:
                if int(car) == player and not flag:
                    count = 1
                    flag = True
                elif int(car) == player and flag:
                    count += 1
                    if count == inARow:
                        return True, line_number
                else:
                    count = 0
        return False, 0

    def changeColumnInLines(self):
        """
        Implements function to transform columns in lines to make tests eaiser.
        :return: a reverse matrice
        """
        column = []
        for x in xrange(7):
            col = ''
            for y in xrange(6):
                col += self.grille[y][x]
            column.append(col)
        return column

    def checkColumn(self, player, inARow):
        """
        Implements function to check the current columns setup to evaluate best combinaison.

        :param player: check for your numbers (your player number) or those of your opponent.
        :param inARow: how many tokens in a row (3 or 2).
        :return: true or false

        """

        column = self.changeColumnInLines()
        count = 0
        flag = False
        for col_number, line in enumerate(column):
            count = 0
            for car in line:
                if int(car) == player and not flag:
                    count = 1
                    flag = True
                elif int(car) == player and flag:
                    count += 1
                    if count == inARow:
                        return True, col_number
                else:
                    count = 0
        return False, 0

    def decideColumn(self):
        """
        Implements main function : to decide what is the better hit to do.

        :return: an int, representing the column where we play
        """

        if self.grilleEmpty():
            return 3



test = BestaPlayer('grille.txt')
print test.checkColumn(test.player, 3)