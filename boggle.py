from boggle_board_randomizer import *
from ex11_utils import *
from ex11_helper import *
from game_model import GameModel
from game_gui import GameGui



class BoggleGame:    
    def __init__(self):
        self._game_model = GameModel()
        self._game_gui = GameGui()

    
    def start_new_game(self):
        board = self._game_model.get_board()
        self._game_gui.create_board(board, self._game_model.do_letter_clicked)   
        self._game_gui.run()


if __name__ == "__main__":
    boogle = BoggleGame()
    boogle.start_new_game()




