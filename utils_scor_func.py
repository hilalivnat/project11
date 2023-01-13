
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
                    path_generator(board, max_words_path, start_point, current_word, one_word)
        if len_word > 1 and len(max_words_path[0]) > 1:
            all_words_paths_list.append(max_words_path[0])
        elif len(max_words_path[0]) == 1:
            all_words_paths_list.append(max_words_path[0])
    return all_words_paths_list


#####################
# helper functions:
#####################

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
                path_generator(board, path_list, path + [one_direction], current_word, given_word)




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



####################################################################################################last_function


if __name__ == "__main__":
    # print(valid_next_steps((3, 3)))
    s = [['C', 'DF', 'Y', 'L'],
         ['D', 'F', 'M', 'T'],
         ['M', 'T', 'A', 'N'],
         ['H', 'C', 'G', 'I']]
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
    print(max_score_paths(s, words))
    # print(max_score_generator(s, d, wor, 3))
    # print(d)
