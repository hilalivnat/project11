from typing import List, Tuple, Iterable, Optional

Board = List[List[str]]
Path = List[Tuple[int, int]]


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    board_height = len(board)
    board_width = len(board[0])
    word = check_path_valid(board, board_height, board_width, path)
    if word is not False and word in words:
        return word


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    board_height = len(board)
    board_width = len(board[0])
    path_list = []
    for row_index in range(board_height):
        for column_index in range(board_width):
            paths_from_cell = []
            start_point = [(row_index, column_index)]
            word = board[row_index][column_index]
            # path_genarator_by_len(path_list, board_height, board_width, tart_point, n)
            path_generator(board, paths_from_cell, board_height, board_width, start_point, n, word, words)
            path_list += paths_from_cell
    return path_list


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    # the next line creates a set of all the words in length n
    board_height = len(board)
    board_width = len(board[0])
    paths_list = []
    for row_index in range(board_height):
        for column_index in range(board_width):
            paths_from_cell = []
            start_point = [(row_index, column_index)]
            word = board[row_index][column_index]
            path_generator(board, paths_from_cell, board_height, board_width, start_point, n, word, words, True)
            paths_list += paths_from_cell
    return paths_list


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    pass


###################################################


def check_path_valid(board: Board, board_height, board_width, path: Path):
    word = ""
    for cell_index in range(len(path)):
        if path[cell_index] in path[:cell_index]:
            return False
        cell = path[cell_index]
        row_index = cell[0]
        column_index = cell[1]
        if not is_cell_in_board(board_height, board_width, row_index, column_index):
            return False
        if cell_index > 0:
            last_cell_in_path = path[cell_index - 1]
            if cell not in valid_next_steps(last_cell_in_path, board_height, board_width):
                return False
        word += board[row_index][column_index]
    return word


def valid_next_steps(cell, board_height, board_width):
    next_steps = set()
    row_index = cell[0]
    column_index = cell[1]
    for row in range(row_index - 1, row_index + 2):
        for column in range(column_index - 1, column_index + 2):
            if is_cell_in_board(board_height, board_width, row, column):
                next_steps.add((row, column))
    next_steps.remove(cell)
    return next_steps


def is_cell_in_board(board_height, board_width, row_index, column_index):
    return (0 <= row_index < board_height) and (0 <= column_index < board_width)


# def path_genarator_by_len(path_list: list, board_height, board_width, path, length):
#     if len(path) == length:
#         path_list.append(path)
#         return
#     for one_direction in valid_next_steps(path[-1], board_height, board_width):
#         if one_direction not in path:
#             path_genarator_by_len(path_list, board_height, board_width, path + [one_direction], length)


def path_generator(board: Board, path_list: list, board_height, board_width, path, length, word, words, by_word_length=False):
    if not by_word_length and len(path) == length:
        if word in words:
            path_list.append(path)
        return
    if by_word_length and len(word) == length:
        if word in words:
            # path_list.append({"word": word, "path": path})
            path_list.append(path)
        return
    for one_direction in valid_next_steps(path[-1], board_height, board_width):
        if one_direction not in path:
            current_word = word + board[one_direction[0]][one_direction[1]]
            path_generator(board, path_list, board_height, board_width, path + [one_direction],length, current_word,words, by_word_length)

def word_in_path(board: Board, path):
    word = ""
    for cell in path:
        word += board[cell[0]][cell[1]]
    return word


if __name__ == "__main__":
    # print(valid_next_steps((3, 3)))
    s = [['C', 'DF', 'Y', 'L'],
         ['I', 'G', 'M', 'T'],
         ['M', 'T', 'A', 'N'],
         ['H', 'E', 'E', 'I']]
    # print(find_length_n_paths(3, s, ["CFY", "GAI"]))

    l = []
    words = ["kkk", "CDF" , "CGI", "MT"]
    # path_genarator_by_word(s, l, 4, 4, [(0,0)], 3, "C")
    print(find_length_n_words(2, s, words))