from boggle_board_randomizer import *
from ex11_utils import *
import copy
from ex11_helper import open_words_file, word_in_path
class GameModel:
    WORDS_DICT = open_words_file("boggle_dict.txt")

    def __init__(self):
        self.__board = randomize_board()
        self.__score = 0
        self.__words_dict = GameModel.WORDS_DICT
        self.__last_clicked = None
        self.__current_path = []

    def __str__(self):
        return "\n".join(str(line) for line in self.__board)

    def new_game(self):
        """ This method initialize a new game"""
        self.__board = randomize_board()
        self.__words_dict = GameModel.WORDS_DICT
        self.__score = 0
        self.__current_path = []


    def clear_choice(self):
        """ This method clears the current path choice"""
        self.__current_path = []
    def check_next_step_valid(self, cell):
        return cell in valid_next_steps(cell, 4, 4)

    def _check_word_in_path(self):
        """ This method checks if the current cose path is a word in the words dictionary"""
        word_in_current_path = word_in_path(self.__board, self.__current_path)
        if word_in_current_path in self.__words_dict:
            self.__words_dict.remove(word_in_current_path)
            points = len(self.__current_path) ** 2
            self.__score += points
            self.clear_choice()
            return word_in_current_path
        return False

    def _do_letter_cell_clicked(self, clicked_cell):
        self.__current_path.append(clicked_cell)
        return self._check_word_in_path()

    def get_board(self):
        """
        :return: Copy of the game's board
        """
        return copy.deepcopy(self.__board)

    def get_score(self):
        """
        :return: The current score
        """
        return self.__score

if __name__ == "__main__":

# c = randomize_board()
# print("\n".join(str(line)for line in c))
# path = [(0,0),(0,1),(0,2),(0,3),(1,0)]
# print(check_path_valid(c, 4, 4 ,path))