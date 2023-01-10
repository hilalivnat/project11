from boggle_board_randomizer import *
from ex11_utils import *
import copy

class GameModel:
    WORDS_DICT: set


    def __init__(self, words_dict):
        self.__board = randomize_board()
        self.__score = 0
        self.__words_dict = words_dict
        self.__last_clicked = None
        self.__current_path = []
        GameModel.WORDS_DICT = words_dict

    def __str__(self):
        return "\n".join(str(line) for line in self.__board)

    def new_game(self):
        self.__board = randomize_board()
        self.__words_dict = GameModel.WORDS_DICT
        self.__score = 0
    def clear_choice(self):
        self.__current_path = []
    def check_next_step_valid(self, cell):
        return cell in valid_next_steps(cell, 4, 4)

    def check_word_in_path(self):
        word_in_current_path = word_in_path(self.__board, self.__current_path)
        if word_in_current_path in self.__words_dict:
            self.__words_dict.remove(word_in_current_path)
            points = len(self.__current_path) ** 2
            self.__score += points
            self.clear_choice()
            return word_in_current_path
        return False

    def _do_letter_cell_clicked(self):

    def get_board(self):
        return copy.deepcopy(self.__board)

    def get_score(self):
        return self.__score

# c = randomize_board()
# print("\n".join(str(line)for line in c))
# path = [(0,0),(0,1),(0,2),(0,3),(1,0)]
# print(check_path_valid(c, 4, 4 ,path))