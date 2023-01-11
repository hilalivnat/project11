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
from typing import List, Tuple, Iterable, Optional, Set
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
    board_height = len(board)
    board_width = len(board[0])
    word = check_path_valid(board, board_height, board_width, path)
    if word is not False and word in words:
        return word



def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    return find_paths(n, board, words)


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    return find_paths(n, board, words, True)


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    pass


#####################
# helper functions:
#####################

def check_path_valid(board: Board, board_height: int, board_width: int, path: Path) -> Optional[str, bool]:
    """
    This function checks that a given path is valid
    :param board: game board
    :param board_height: board's height
    :param board_width: board's width
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
        if not is_cell_in_board(board_height, board_width, row_index, column_index):
            return False
        # the next lines checks that the cell is a valid next step for the privies cell in the path
        if cell_index > 0:
            last_cell_in_path = path[cell_index - 1]
            if cell not in valid_next_steps(last_cell_in_path, board_height, board_width):
                return False
        word += board[row_index][column_index]
    return word


def valid_next_steps(cell: Cell, board_height: int, board_width: int) -> Set[Cell]:
    """
    This function returns all the cells that are in a valid direction for the next step from the given cell.
    :param cell: A tuple representing a cell coordinate
    :param board_height: board's height
    :param board_width: board's height
    :return: a set containing all the valid coordinates for a next step from the cell.
    """
    next_steps = set()
    row_index = cell[0]
    column_index = cell[1]
    for row in range(row_index - 1, row_index + 2):
        for column in range(column_index - 1, column_index + 2):
            # the next lines adds the cell in (row, column) to the set if it's in the board
            if is_cell_in_board(board_height, board_width, row, column):
                next_steps.add((row, column))
    next_steps.remove(cell)
    return next_steps


def is_cell_in_board(board_height: int, board_width: int, row_index: int, column_index: int) -> bool:
    """
    This function checks if a given cell is in a given board.
    :param board_height: boards' height
    :param board_width: boards' width
    :param row_index: The cell's row index
    :param column_index: The cell's column index
    :return: True if the cell is in the board, False otherwise
    """
    return (0 <= row_index < board_height) and (0 <= column_index < board_width)


def path_generator(board: Board, path_list: list,
                   board_height: int, board_width: int,
                   path: Path, length: int, word: str,
                   words_set: set, by_word_length: bool) -> List[Path]:
    """
    This function generates legal paths from one cell
    on the board that contains a word in the words' dictionary,
    so that the length of the word or the path is the desired length.

    :param board: game board
    :param path_list: list
    :param board_height: boards' height
    :param board_width: boards' width
    :param path: a list that contains the first cell in the path
    :param length: the length requested paths / the length of the requested words in the paths
    :param word: the letter in the first cell
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
        if word in words:
            path_list.append(path)
        return
    # the next lines will run if the function called in "by_word_length" mode
    elif by_word_length and len(word) == length:
        if word in words:
            path_list.append(path)
        return
    # the next lines adds a valid next cell to the path and updates the current word
    for one_direction in valid_next_steps(path[-1], board_height, board_width):
        if one_direction not in path:
            current_word = word + board[one_direction[0]][one_direction[1]]
            path_generator(board, path_list, board_height, board_width, path + [one_direction],length, current_word,words_set, by_word_length)


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
    board_height = len(board)
    board_width = len(board[0])
    path_list = []
    words = set(words)  # So that search in the words dictionary will run in O(1) running time.
    # The next lines adds to path_list all the valid paths from each cell on the board.
    for row_index in range(board_height):
        for column_index in range(board_width):
            paths_from_cell = []
            start_point = [(row_index, column_index)]
            word = board[row_index][column_index]
            path_generator(board, paths_from_cell,
                           board_height, board_width,
                           start_point, length, word, words,
                           by_word_length)
            path_list += paths_from_cell
    return path_list

    
if __name__ == "__main__":
    # print(valid_next_steps((3, 3)))
    s = [['C', 'DF', 'Y', 'L'],
         ['I', 'G', 'M', 'T'],
         ['M', 'T', 'A', 'N'],
         ['H', 'E', 'E', 'I']]
    # print(find_length_n_paths(3, s, ["CFY", "GAI"]))

    l = []
    words = ["kkk", "CDF", "CGI", "MT"]
    # path_genarator_by_word(s, l, 4, 4, [(0,0)], 3, "C")
    print(find_length_n_words(2, s, words))