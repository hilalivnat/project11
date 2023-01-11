######################################################################
# FILE: boggle.py
# WRITERS: Michal_Caduri, michal.caduri, 213088735
# Hila_Livnat, hilalivnat, 324862028
# EXERCISE: intro2cs1 ex11 2023
# DESCRIPTION: A program defines the class BoggleGame
# and runs a boggle game
######################################################################
######################################################################
# imports:
from game_model import GameModel
from game_gui import GameGui
######################################################################


class BoggleGame:    
    def __init__(self):
        self._game_model = GameModel()
        self._game_gui = GameGui()
    
    def start_new_game(self):
        board = self._game_model.get_board()
        self._game_gui.create_board(board, self._game_model.do_letter_clicked)   
        self._game_gui.run()


if __name__ == "__main__":
    boggle_game = BoggleGame()
    boggle_game.start_new_game()




