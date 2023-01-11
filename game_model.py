######################################################################
# FILE: game_model.py
# WRITERS: Michal_Caduri, michal.caduri, 213088735
# Hila_Livnat, hilalivnat, 324862028
# EXERCISE: intro2cs1 ex11 2023
# DESCRIPTION: A program defines the class GameModel
# that controls the logic of boggle game.
######################################################################
######################################################################
# imports:
from boggle_board_randomizer import *
from ex11_utils import *
import copy
from ex11_helper import open_words_file, word_in_path
######################################################################


class GameModel:
    """ A class that defines and controls
    the logic part of the boggle game"""

    WORDS_DICT: set = open_words_file("boggle_dict.txt")

    def __init__(self):
        """ Initialize new game"""
        self.__board = randomize_board()
        self.__score = 0
        self.__words_dict = GameModel.WORDS_DICT
        self.__found_words = list()
        self.__last_clicked = None
        self.__current_path = []

    # def __str__(self):
    #     return "\n".join(str(line) for line in self.__board)

    def new_game(self) -> None:
        """ This method initialize a new game"""
        self.__board = randomize_board()
        self.__words_dict = GameModel.WORDS_DICT
        self.__score = 0
        self.__current_path = []

    def clear_choice(self) -> None:
        """ This method clears the current path choice"""
        self.__current_path = []

    def check_next_step_valid(self, cell: Cell) -> bool:
        """
        This method checks if a given cell is a valid step from
        the last cell in the game's current chosen path.
        :param cell: The next cell the user wants to add to the current path.
        :return: True if the cell can be chosen, False otherwise.
        """
        if len(self.__current_path) == 0:  # Any cell is valid for starting a new path
            return True
        else:
            # The next lines checks if the given cell is a legal move from the last cell in the path.
            last_cell = self.__current_path[-1]
        return cell in valid_next_steps(last_cell, 4, 4)

    def _check_word_in_path(self) -> Union[str, bool]:
        """
        This method checks if the current chosen path is a word in the words dictionary
        :return: The word in the path, if it is in the words dictionary, False otherwise
        """
        word_in_current_path = word_in_path(self.__board, self.__current_path)
        if word_in_current_path in self.__words_dict:
            # The next line removes the word from the dictionary so that it cannot
            # be selected again in the current round of the game.
            self.__words_dict.remove(word_in_current_path)
            self.__found_words.append(word_in_current_path)
            # The next line increases the score according to the squared length of the path
            points = len(self.__current_path) ** 2
            self.__score += points
            self.clear_choice()  # Resets the current path selection.
            return word_in_current_path
        return False

    def do_letter_clicked(self, clicked_cell: Cell) -> Tuple[Union[str, bool], int]:
        """
        This method add the given cell to the current chosen and checks
        whether this cell has a letter that completes the selected path on
        the board to a word from the word dictionary,
        if so updates the game accordingly.
        :param clicked_cell: A cell that the user clicked on.
        :return: The word in the path, if it is in the words dictionary,
        False otherwise, and the current score.
        """
        print('clicked_cell in do: ', clicked_cell)
        self.__current_path.append(clicked_cell)
        return self._check_word_in_path(), self.get_score()
    
    def get_found_words(self):
        return self.__found_words[:]

    def get_board(self) -> Board:
        """
        :return: Copy of the game's board
        """
        return copy.deepcopy(self.__board)

    def get_score(self) -> int:
        """
        :return: The current score
        """
        return self.__score


if __name__ == "__main__":
    pass

# c = randomize_board()
# print("\n".join(str(line)for line in c))
# path = [(0,0),(0,1),(0,2),(0,3),(1,0)]
# print(check_path_valid(c, 4, 4 ,path))
