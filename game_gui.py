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
import uuid
from typing import *
from styles import *


######################################################################

class GameGui:
    def __init__(self) -> None:
        # helper variables
        # self._current_word = ""
        self._found_words = []
        # tkinter vars
        root = tkinter.Tk()
        root.title("Boggle")
        root.geometry("400x400")
        self.__root = root

        self._main_frame = tkinter.Frame(self.__root, width=100, height=100)
        self._main_frame.pack(fill=tkinter.BOTH, expand=True)

        self._title_label = tkinter.Label(self._main_frame, text="Boogle", **DISPLAY_WORD)
        self._title_label.pack(fill=tkinter.BOTH, expand=True)

        # self._display_word = tkinter.Label(self._main_frame, text="",**DISPLAY_WORD)
        # self._display_word.grid(row=1, column=0)
        self._score_display = tkinter.Label(self._main_frame, **DISPLAY_WORD)
        self._score_display.pack(fill=tkinter.BOTH, expand=True)

        self._buttons_frame = tkinter.Frame(self._main_frame)
        self._buttons_frame.pack(fill=tkinter.BOTH, expand=True)

        self._words_display = tkinter.Label(self._main_frame, **FOUND_WORDS)
        self._words_display.pack(fill=tkinter.BOTH, expand=True)

        self._buttons: Dict[tkinter.Button] = dict()

    def run(self):
        self.__root.mainloop()

    def create_button_command(self, f, cell, btn_id):
        def handler():
            # self._current_word += char
            # self._display_word["text"] = self._current_word
            self._buttons[btn_id]["state"] = "disabled"
            self._buttons[btn_id]["bg"] = DISABLED_COLOR
            word, score = f(cell)
            if word:
                self._found_words.append(word)
                self.update_board(score)

        return handler

    def _create_button(self, coord, char, f):
        btn_id = uuid.uuid4()
        button = tkinter.Button(self._buttons_frame,
                                text=char,
                                command=self.create_button_command(f, coord, btn_id), **BUTTON_STYLE)
        button.grid(row=coord[0], column=coord[1], sticky=tkinter.NSEW, rowspan=1, columnspan=1)
        self._buttons[btn_id] = button

    def create_board(self, board, f):
        # for i in range(4):
        # tkinter.Grid.grid_configure(self._buttons_frame,column=4, row=4)
        for row_i, row in enumerate(board):
            for col_i, char in enumerate(row):
                self._buttons_frame.grid_columnconfigure(col_i, weight=1, uniform="True")
                self._buttons_frame.grid_rowconfigure(row_i, weight=1, uniform="True")
                self._create_button((row_i, col_i), char, f)

    def update_board(self, score):
        for btn in self._buttons.values():
            btn["state"] = "normal"
            btn["bg"] = BTN_BG

        self._words_display["text"] = "found words:\n" + "\n".join(self._found_words)
        self._score_display["text"] = f'Score: {score}'


if __name__ == "__main__":
    pass
