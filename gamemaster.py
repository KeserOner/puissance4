__author__ = 'bajai'
import bestaplayer
import os

class GameMaster:

    def __init__(self, fichier):
        self.bot_player = bestaplayer.BestaPlayer(fichier)
        self.grid = self.bot_player.grille
        self.fichier = fichier

    def displayGrid(self):
        """
        Implements function to display the current grid of play.

        """
        for line in self.grid:
            print ' '.join(line) + '\n\n'
        os.system('clear')

    def updateFileFromGrid(self):
        """
        Implements function that update the file after a player give a token.
        """
        with open(self.fichier, 'w') as fi:
            for line in self.grid:
                fi.write(line + '\n')

    def playAShot(self, col):
        """
        Implements function to play a turn.
        :param col: the column player wanna play in.
        """
        if self.grid[0][col] != '0':
            return False
        elif self.grid[5][col] == '0':
            return 5
        else:
            for x in xrange(6):
                if self.grid[x][col] != '0':
                    return x - 1

