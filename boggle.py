######################################################################
# FILE: boggle.py
# WRITERS: Michal_Caduri, michal.caduri
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
    """A class that defines and controls boggle game """
    def __init__(self):
        """Initialize a new boggle game"""
        self._game_model = GameModel()
        self._game_gui = GameGui()
    
    def create_new_game(self):
        """ This method combines the game model and GUI"""
        self._game_model.new_game()
        board = self._game_model.get_board()

        self._game_gui.create_board(
            board, self._game_model.do_letter_clicked,
            self._game_model.clear_choice)

        self._game_gui.start_game()
    
    def start_new_game(self):
        """ This method runs the boggle game"""
        self._game_gui.init_gui(self.create_new_game)  
        self._game_gui.run()


if __name__ == "__main__":
    boggle_game = BoggleGame()
    boggle_game.start_new_game()




