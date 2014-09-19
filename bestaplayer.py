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
                for car in line:
                    if car != '0':
                        return 2
            return 1
test = BestaPlayer('grille.txt')
test.displayGrid()