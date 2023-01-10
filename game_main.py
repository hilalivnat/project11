from boggle_board_randomizer import *
from ex11_utils import *
import copy

class GameModel:
    _cur_cell: tuple


    def __init__(self, words_dict):
        self.__board = randomize_board()
        self.__score = 0
        self.__words_dict = words_dict
        self.__last_clicked = None

    # def _do_cell_clicked(self, cell):

    def __str__(self):
        return "\n".join(str(line) for line in self.__board)

    def new_game(self):
        self.__board = randomize_board()
        self.__score = 0

    def get_board(self):
        return copy.deepcopy(self.__board)

    def get_score(self):
        return self.__score

# c = randomize_board()
# print("\n".join(str(line)for line in c))
# path = [(0,0),(0,1),(0,2),(0,3),(1,0)]
# print(check_path_valid(c, 4, 4 ,path))