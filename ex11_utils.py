######################################################################
# FILE: ex11_utils.py
# WRITERS: Michal_Caduri, michal.caduri, 213088735
# Hila_Livnat, hilalivnat, 324862028
# EXERCISE: intro2cs1 ex11 2023
# DESCRIPTION: A program defines functions that
# solves boggle games, using backtracking.
######################################################################
######################################################################
# imports:
from typing import List, Tuple, Iterable, Optional, Set, Union, Dict
import copy
######################################################################

#####################
# typing:
#####################

Board = List[List[str]]
Path = List[Tuple[int, int]]
Cell = Tuple[int, int]


#####################
# required functions:
#####################
def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """
    This function checks if a given path is a valid path that
    describes a word that exists in the collection of words.
    :param board: game board
    :param path: A path of coordinates on the game board
    :param words: iterable contains collection of words
    :return: The word in the path, if the path is
    valid and the word exists in the collection of words,
    otherwise return None.
    """
    # The next line creates the word in the path if the path is valid
    word = check_path_valid(board, path)
    if word is not False and word in words:
        return word


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    This function finds and returns all the valid paths of length n
    that describe words in the collection of words.
    :param n: A positive integer, represents the length of the paths that need to be found.
    :param board: Game board
    :param words: Iterable contains collection of words
    :return: A list of all valid paths of length n that
    describe words in the collection of words.
    """
    return find_paths(n, board, words)


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    This function finds and returns all the valid paths that describes words
    in the collection of words that are of length n.
    :param n: A positive integer, represents the
    length of the words to be found.
    :param board: Game board
    :param words: Iterable contains collection of words
    :return: A list of all valid paths describing words
    in the collection of words that are of length n
    """
    return find_paths(n, board, words, True)


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    all_words_paths_list = []
    for one_word in words:
        len_word = len(one_word)
        max_words_path = [[]]
        for row_index in range(len(board)):
            for column_index in range(len(board[row_index])):
                start_point = [(row_index, column_index)]
                current_word = board[row_index][column_index]
                if current_word in one_word:
                    max_path_generator(board, max_words_path, start_point, current_word, one_word)
        if len_word > 1 and len(max_words_path[0]) > 1:
            all_words_paths_list.append(max_words_path[0])
        elif len(max_words_path[0]) == 1:
            all_words_paths_list.append(max_words_path[0])
    return all_words_paths_list


#####################
# helper functions:
#####################

def check_path_valid(board: Board, path: Path) -> Union[str, bool]:
    """
    This function checks that a given path is valid
    :param board: game board
    :param path: path on the board
    :return: the word in the path on the board if the path is valid, False otherwise
    """
    word = ""
    for cell_index in range(len(path)):
        # the next line checks that the cell isn't in the path already
        if path[cell_index] in path[:cell_index]:
            return False
        cell = path[cell_index]
        row_index = cell[0]
        column_index = cell[1]
        # the next line checks that the cell is in board
        if not is_cell_in_board(board, row_index, column_index):
            return False
        # the next lines checks that the cell is a valid next step for the privies cell in the path
        if cell_index > 0:
            last_cell_in_path = path[cell_index - 1]
            if cell not in valid_next_steps(last_cell_in_path, board):
                return False
        word += board[row_index][column_index]
    return word


def valid_next_steps(cell: Cell, board: Board) -> Set[Cell]:
    """
    This function returns all the cells that are in a valid direction for the next step from the given cell.
    :param cell: A tuple representing a cell coordinate
    :param board: Game board
    :return: A set containing all the valid coordinates for a next step from the cell.
    """
    next_steps = set()
    row_index = cell[0]
    column_index = cell[1]
    for row in range(row_index - 1, row_index + 2):
        for column in range(column_index - 1, column_index + 2):
            # the next lines adds the cell in (row, column) to the set if it's in the board
            if is_cell_in_board(board, row, column):
                next_steps.add((row, column))
    next_steps.remove(cell)
    return next_steps


def path_generator(board: Board, path_list: list,
                   path: Path, length: int, word: str,
                   original_words_set: set, words_set: set, by_word_length: bool) -> None:
    """
    This function generates legal paths from one cell
    on the board that contains a word in the words' dictionary,
    so that the length of the word or the path is the desired length.

    :param board: game board
    :param path_list: list
    :param path: a list that contains the first cell in the path
    :param length: the length requested paths / the length of the requested words in the paths
    :param word: the letter in the first cell
    :param original_words_set: a set of all the words in
    dictionary that a current path contains there first letters
    :param words_set: a set of all the words in dictionary
    :param by_word_length: generate paths by word length - False in default
    :return: For searching by word length -
    return a list of all legal paths from a cell on the board that contains a word
    in the given length that is in  the words' dictionary.

    For searching by path length -
    return a list of all legal paths from a cell on the board that
    is in the given length and contains a word in  the words' dictionary.
    """
    # the next lines will run if the function called in the default mode
    if not by_word_length and len(path) == length:
        if word in words_set:
            path_list.append(path)
        return
    # the next lines will run if the function called in "by_word_length" mode
    elif by_word_length and len(word) == length:
        if word in words_set:
            path_list.append(path)
        return
    # the next lines adds a valid next cell to the path and updates the current word
    for one_direction in valid_next_steps(path[-1], board):
        if one_direction not in path:
            prev_word_set = copy.deepcopy(words_set)
            current_word = word + board[one_direction[0]][one_direction[1]]
            words_set = set([set_word for set_word in words_set if current_word in set_word])
            if len(words_set):
                path_generator(board, path_list, path + [one_direction],
                               length, current_word, original_words_set,
                               words_set, by_word_length)
            words_set = prev_word_set


def find_paths(length: int, board: Board, words: Iterable[str], by_word_length=False) -> List[Path]:
    """
    This function finds all the legal paths on the board that
    contains a word in the words' dictionary, so that the length
    of the word or the path is the desired length.
    :param length: the length requested paths / the length of the requested words in the paths
    :param board: game board
    :param words: an iterable of the format Iterable[str], representing a words dictionary
    :param by_word_length: generate paths by word length - False in default
    :return: For searching by word length -
    return a list of all legal on the board that contains a word
    in the given length that is in the words' dictionary.

    For searching by path length -
    return a list of all legal paths from on the board that
    is in the given length and contains a word in the words' dictionary.
    """
    path_list = []
    if by_word_length:

        words_set = set([word for word in words if len(word) <= length])
    else:
        words_set = set([word for word in words if len(word) >= length])

    return find_paths_helper(board, path_list, words_set, length, by_word_length)


def find_paths_helper(board: Board, path_list: List[Path],
                      words_set: set, length: int,
                      by_word_length: bool) -> List[Path]:
    for row_index in range(len(board)):
        for column_index in range(len(board[row_index])):
            paths_from_cell = []
            start_point = [(row_index, column_index)]
            current_word = board[row_index][column_index]
            current_words_set = set([one_word for one_word in words_set if current_word in words_set])
            path_generator(board, paths_from_cell,
                           start_point, length, current_word, current_words_set,
                           words_set,
                           by_word_length)
            path_list += paths_from_cell
    return path_list


def is_cell_in_board(board: Board, row_index: int, column_index: int) -> bool:
    """
    This function checks if a given cell is in a given board.
    :param board: game board
    :param row_index: The cell's row index
    :param column_index: The cell's column index
    :return: True if the cell is in the board, False otherwise
    """
    if row_index < 0 or column_index < 0:
        return False
    else:
        try:
            if board[row_index][column_index]:
                return True
        except IndexError:
            return False


def max_path_generator(board: Board, path_list: list,
                   path: Path, word: str, given_word: str) -> None:
    if len(word) == len(given_word):
        if len(path) > len(path_list[0]):
            path_list[0] = path
        return

    # the next lines adds a valid next cell to the path and updates the current word
    for one_direction in valid_next_steps(path[-1], board):
        if one_direction not in path:
            current_word = word + board[one_direction[0]][one_direction[1]]
            if current_word in given_word:
                max_path_generator(board, path_list, path + [one_direction], current_word, given_word)


if __name__ == "__main__":
    # print(valid_next_steps((3, 3)))
    s = [['C', 'DF', 'Y', 'L'],
         ['D', 'F', 'M', 'T'],
         ['M', 'T', 'A', 'N'],
         ['H', 'E', 'E', 'I']]
    # print(is_cell_in_board1(s, 2, 0))
    # print(find_length_n_paths(3, s, ["CFY", "GAI"]))

    # l = []
    with open("boggle_dict.txt", 'r') as f:
        all_words = f.readlines()
        words = [one_line.replace("\n", '') for one_line in all_words]
    # wor = {"kkk", "CDF", "CGI", "MT"}
    # # # path_genarator_by_word(s, l, 4, 4, [(0,0)], 3, "C")
    # print(find_length_n_words(3, s, words))
    # print(is_valid_path(s, [(2, 0), (3, 1),(2,1)], words))
    # d = dict()
    # print(path_score_generator(s, d, [(0,0)],3, "C", wor, wor))
    # print(d)
    # print(max_score_paths(s, words))
    # print(max_score_generator(s, d, wor, 3))
    # print(d)
