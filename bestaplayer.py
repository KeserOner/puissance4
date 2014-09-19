__author__ = 'besta'


class BestaPlayer:
    def __init__(self, fichier):
        self.grille = [['0' for x in xrange(7)] for y in xrange(6)]
        self.fichier = fichier
        self.best_hit = 0

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

