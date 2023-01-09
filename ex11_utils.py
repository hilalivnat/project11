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
            path_genarator(path_list, board_height, board_width, [(row_index, column_index)], n)
    valid_path_list = []
    for one_path in path_list:
        if word_in_path(board, one_path) in words:
            valid_path_list.append(one_path)
    return valid_path_list


# def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
#     board_height = len(board)
#     board_width = len(board[0])
#     path_list = []
#     for row_index in range(board_height):
#         for column_index in range(board_width):
#             path_genarator_by_word(board: Board, path_list: list, board_height, board_width, path, length, word)
#     pass


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


def path_genarator(path_list: list, board_height, board_width, path, length):
    if len(path) == length:
        path_list.append(path)
        return
    for one_direction in valid_next_steps(path[-1], board_height, board_width):
        if one_direction not in path:
            path_genarator(path_list, board_height, board_width, path + [one_direction], length)


def path_genarator_by_word(board: Board, path_list: list, board_height, board_width, path, length, word):
    if len(word) == length:
        path_list.append({
            "word": word,
            "path": path})
        return
    for one_direction in valid_next_steps(path[-1], board_height, board_width):
        if one_direction not in path:
            current_word = word + board[one_direction[0]][one_direction[1]]
            path_genarator_by_word(board, path_list, board_height, board_width, path + [one_direction],length, current_word)

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
    path_genarator_by_word(s, l, 4, 4, [(0,0)], 3, "C")
    print(l)