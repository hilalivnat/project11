def open_words_file(index_file):
    """
    This function gets a text file and returns its words in a set
    :param index_file: Name of a text file that contains words
    :return: A set with all the words in the file
    """
    words = []
    with open(index_file, 'r') as f:
        all_words = f.readlines()
    # the next line cutting off "\n" from each line
    words = [one_line.replace("\n", '') for one_line in all_words]
    return set(words)


def word_in_path(board, path):
    word = ""
    for cell in path:
        word += board[cell[0]][cell[1]]
    return word


if __name__ == "__main__":
    pass