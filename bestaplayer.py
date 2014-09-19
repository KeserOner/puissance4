__author__ = 'besta'

class BestaPlayer :

    def __init__(self, fichier):
        self.grille = [['0' for x in xrange(7)] for y in xrange(6)]
        self.fichier = fichier
        self.best_hit = 0

    def updateGrid(self):
        """
        Implements function to update the grid to alter n-1
        round values

        """

