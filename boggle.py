import boggle
from boggle_board_randomizer import *
from ex11_utils import *
from ex11_helper import *

class BoggleGame:
    words_dict = open_words_file("boggle_dict.txt")
    # def __int__(self):


    def __init__(self):
        self.__board = randomize_board()
    def __str__(self):
        return "\n".join(str(line)for line in self.__board)



# c = randomize_board()
# print("\n".join(str(line)for line in c))
# path = [(0,0),(0,1),(0,2),(0,3),(1,0)]
# print(check_path_valid(c, 4, 4 ,path))
b = BoggleGame()
print(b.words_dict)
