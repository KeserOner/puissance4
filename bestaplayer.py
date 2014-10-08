__author__ = 'besta'


class BestaPlayer:

    def __init__(self, fichier, player):
        self.fichier = fichier
        self.grille = self.getFirstGrid()
        self.best_hit = 0
        self.players = player

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
            for car_pos, car in enumerate(line[:len(line) - 1]):
                if int(car) == player and not flag:
                    count = 1
                    flag = True
                elif int(car) == player and flag:
                    count += 1
                    if count == inARow:
                        if car_pos - inARow >= 0 and self.canPlayLine(line_number, car_pos - inARow):
                            return True, car_pos - inARow
                        if car_pos + 1 <= 6 and self.canPlayLine(line_number, car_pos + 1):
                            return True, car_pos + 1
                else:
                    count = 0
        return False, 0

    def canPlayLine(self, line, col):
        """
        Function to check if we can fill the line with a token.
        :param line: which line
        :param col: which column
        :return: true or false
        """
        if line == 5:
            return self.grille[line][col] == '0'
        else:
            return self.grille[line][col] == '0' and self.grille[line + 1][col] != '0'

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

    def checkColumns(self, player, inARow):
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
            for car_pos, car in enumerate(line):
                if int(car) == player and not flag:
                    count = 1
                    flag = True
                elif int(car) == player and flag:
                    count += 1
                    if count == inARow and car_pos - inARow >= 0 and self.grille[car_pos - inARow][col_number] == '0':
                        return True, col_number
                else:
                    count = 0
        return False, 0

    def checkDiagonalLeftToRight(self, player, inARow):
        """
        Implements function to check the current diagonal to evaluate best combinaison.

        :param player: check for your numbers or opponent ones.
        :param inARow:  how many tokens in a row (3 or 2).
        :return:
        """

        x = 3
        flag = False
        while x < 6:
            count = 0
            x_int = x
            y_int = 0
            while x_int >= 0:
                if int(self.grille[x_int][y_int]) == player and not flag:
                    count = 1
                    flag = True
                elif int(self.grille[x_int][y_int]) == player and flag:
                    count += 1
                    if count == inARow and y_int + 1 <= 6 and x_int - 1 >= 0 and self.grille[x_int][y_int + 1] != '0':
                        return True, y_int + 1
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
                if int(self.grille[x_int][y_int]) == player and not flag:
                    count = 1
                    flag = True
                elif int(self.grille[x_int][y_int]) == player and flag:
                    count += 1
                    if count == inARow and y_int + 1 <= 6 and x_int - 1 >= 0 and self.grille[x_int][y + 1] != '0':
                        return True, y_int + 1
                else:
                    count = 0
                    flage = False
                x_int -= 1
                y_int += 1
            y += 1

        return False, 0

    def checkDiagonalRightToLeft(self, player, inARow):
        """
        Implements function to check the current diagonal to evaluate best combinaison.

        :param player: check for your numbers or opponent ones.
        :param inARow:  how many tokens in a row (3 or 2).
        :return:
        """

        x = 3
        flag = False
        while x < 6:
            count = 0
            x_int = x
            y_int = 6
            while x_int >= 0:
                if int(self.grille[x_int][y_int]) == player and not flag:
                    count = 1
                    flag = True
                elif int(self.grille[x_int][y_int]) == player and flag:
                    count += 1
                    if count == inARow and y_int - 1 >= 0 and x_int - 1 >= 0 and self.grille[x_int][y_int - 1] != '0':
                        return True, y_int - 1
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
                if int(self.grille[x_int][y_int]) == player and not flag:
                    count = 1
                    flag = True
                elif int(self.grille[x_int][y_int]) == player and flag:
                    count += 1
                    if count == inARow and y_int - 1 >= 0 and x_int - 1 >= 0 and self.grille[x_int][y - 1] != '0':
                        return True, y_int - 1
                else:
                    count = 0
                    flage = False
                x_int -= 1
                y_int -= 1
            y -= 1

        return False, 0

    def checkDiagonals(self, player, inARow):
        """
        Calls two diagonal functional.
        :return: an int, representing the column where to play or 0 and False if there is no pattern search.
        """
        check = self.checkDiagonalLeftToRight(player, inARow)
        if check[0]:
            return check
        else:
            return self.checkDiagonalRightToLeft(player, inARow)

    def playSomeColumn(self, player, inARow):
        """
        Call all function for a player and a number of tokens given.
        :param player: which player
        :param inARow: how many token
        :return: true or false (col number if true)
        """
        methods = {'checklines': self.checkLines, 'checkcolumn': self.checkColumns, 'checkdiagonal': self.checkDiagonals}
        for key, function in methods.items():
            which_col = function(player, inARow)
            if which_col[0]:
                return which_col
        return False, 0

    def findFirstColumnEmpty(self):
        """
        Implements function to get the first column where a slot remain.
        :return: the column
        """
        for col in xrange(7):
            if self.grille[0][col] == '0':
                return col
        return -1

    def decideColumn(self):
        """
        Implements main function : to decide what is the better hit to do.

        :return: an int, representing the column where we play
        """
        if self.grilleEmpty():
            return 3

        li_sequence = [3, 2, 1]
        li_players = [self.players[0], self.players[1]]
        for sequence in li_sequence:
            for player in li_players:
                choosen_col = self.playSomeColumn(player, sequence)
                if choosen_col[0]:
                    return choosen_col[1]

        return self.findFirstColumnEmpty()
