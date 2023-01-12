######################################################################
# FILE: game_gui.py
# WRITERS: Michal_Caduri, michal.caduri, 213088735
# Hila_Livnat, hilalivnat, 324862028
# EXERCISE: intro2cs1 ex11 2023
# DESCRIPTION: A program defines the class GameGui
# that controls the GUI of boggle game.
######################################################################
######################################################################
# imports:
import tkinter
from typing import *
from styles import *
from ex11_helper import *
from buttons import Buttons


######################################################################

class GameGui:
    def __init__(self) -> None:

        # tkinter vars
        root = tkinter.Tk()
        root.title("Boggle")
        root.geometry("400x600")
        self.__root = root

        self._main_frame = tkinter.Frame(self.__root, width=100, height=100)
        self._main_frame.pack(fill=tkinter.BOTH, expand=True)

        self._title_label = tkinter.Label(self._main_frame, text="Boggle", **DISPLAY_WORD)
        self._title_label.pack(fill=tkinter.BOTH, expand=True)

        self._current_word = tkinter.StringVar(self._main_frame, "")

        self._display_word = tkinter.Label(self._main_frame, textvariable=self._current_word, **DISPLAY_WORD)
        self._display_word.pack(fill=tkinter.BOTH, expand=True)

        self._game_score = tkinter.StringVar(self._main_frame, generate_score(0))

        self._score_display = tkinter.Label(self._main_frame, textvariable=self._game_score, **DISPLAY_WORD)
        self._score_display.pack(fill=tkinter.BOTH, expand=True)

        self._buttons: Buttons = Buttons(self.__root)

        self._clear_btn = tkinter.Button(self._main_frame, text="Clear Word")
        self._clear_btn.pack(fill=tkinter.BOTH, expand=True)

        self._found_words = tkinter.StringVar(self.__root, "")
        self._words_display = tkinter.Label(self._main_frame, textvariable=self._found_words, **FOUND_WORDS)
        self._words_display.pack(fill=tkinter.BOTH, expand=True)

        

    def run(self):
        self.__root.mainloop()


    def handel_btn_clicked(self, char, res):
        self._current_word.set(self._current_word.get() + char)
        found_new_word, words, score = res
        if found_new_word:
            self._found_words.set(words)
            self._current_word.set("")
            self._game_score.set(generate_score(score))
            self.update_board()


    def create_board(self, board, click_on_btn_f, clear_f):
        for row_i, row in enumerate(board):
            for col_i, char in enumerate(row):
                self._buttons.create_button(
                    (row_i, col_i), char, click_on_btn_f, self.handel_btn_clicked)

        def btn_clear_func():
            clear_f()
            self._current_word.set("")
            self._buttons.return_buttons_to_normal_state()

        self._clear_btn["command"] = btn_clear_func

    def update_board(self):
        self._buttons.return_buttons_to_normal_state()


if __name__ == "__main__":
    pass
