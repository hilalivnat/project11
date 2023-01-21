######################################################################
# FILE: ex11_helper.py
# WRITERS: Michal_Caduri, michal.caduri, 213088735
# Hila_Livnat, hilalivnat, 324862028
# EXERCISE: intro2cs1 ex11 2023
# DESCRIPTION: A program defines helper functions
# for the class GameModel
######################################################################

MAX_WORDS_LENGTH = 26


def open_words_file(index_file):
    """
    This function gets a text file and returns its words in a set
    :param index_file: Name of a text file that contains words
    :return: A set with all the words in the file
    """
    with open(index_file, 'r') as f:
        all_words = f.readlines()
    # the next line cutting off "\n" from each line
    words = [one_line.replace("\n", '') for one_line in all_words]
    return set(words)


def generate_score(score):
    """
    This function displays the score of the game
    :param score: int representing the score in the game.
    :return: string representing the score in the game.
    """
    return f'Score: {score}'


def generate_found_words(words):
    """
    This function creates a string of
    all the found words
    :param words: list of words
    :return: a string of all the words,
    including 7 words in each line.
    """
    words_string = ""
    for i, word in enumerate(words):
        if i > 0 and i % 7 == 0:
            words_string += f'{word} \n'
        else:
            words_string += f'{word}, '

    return words_string
