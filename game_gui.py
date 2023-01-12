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
from ex11_helper import *


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

        self._display_word = tkinter.Label(self._main_frame, textvariable=self._current_word,**DISPLAY_WORD)
        self._display_word.pack(fill=tkinter.BOTH, expand=True)

        self._game_score = tkinter.StringVar(self._main_frame, generate_score(0))

        self._score_display = tkinter.Label(self._main_frame, textvariable=self._game_score, **DISPLAY_WORD)
        self._score_display.pack(fill=tkinter.BOTH, expand=True)

        self._buttons_frame = tkinter.Frame(self._main_frame)
        self._buttons_frame.pack(fill=tkinter.BOTH, expand=True)

        self._clear_btn = tkinter.Button(self._main_frame, text="Clear Word")
        self._clear_btn.pack(fill=tkinter.BOTH, expand=True)

        self._found_words= tkinter.StringVar(self.__root, "")
        self._words_display = tkinter.Label(self._main_frame,textvariable=self._found_words, **FOUND_WORDS)
        self._words_display.pack(fill=tkinter.BOTH, expand=True)

        self._buttons: Dict[tkinter.Button] = dict()

    def run(self):
        self.__root.mainloop()

    def return_to_regular_color(self, btn_id):
        def handler():
            self._buttons[btn_id]["bg"] = BTN_BG
        return handler    

    def create_button_command(self, f, cell, char, btn_id):
        def handler():
            res = f(cell)
            print('res: ', res)
            if not bool(res):
                self._buttons[btn_id]["bg"] = "red"
                self.__root.after(100,  self.return_to_regular_color(btn_id))
                return
            self._current_word.set(self._current_word.get() + char)
            self._buttons[btn_id]["state"] = "disabled"
            self._buttons[btn_id]["bg"] = DISABLED_COLOR
            words, score = res
            if score:
                self._found_words.set(words)
                self._current_word.set("")
                self._game_score.set(generate_score(score))
                self.update_board()


        return handler

    def _create_button(self, coord, char, f):
        btn_id = uuid.uuid4()
        button = tkinter.Button(self._buttons_frame,
                                text=char,
                                command=self.create_button_command(f, coord, char, btn_id), **BUTTON_STYLE)
        button.grid(row=coord[0], column=coord[1], sticky=tkinter.NSEW, rowspan=1, columnspan=1)
        self._buttons[btn_id] = button

    def create_board(self, board, click_on_btn_f, clear_f):
        for row_i, row in enumerate(board):
            for col_i, char in enumerate(row):
                self._buttons_frame.grid_columnconfigure(col_i, weight=1, uniform="True")
                self._buttons_frame.grid_rowconfigure(row_i, weight=1, uniform="True")
                self._create_button((row_i, col_i), char, click_on_btn_f)
        
        def btn_clear_func():
            clear_f()
            self._current_word.set("")
            self._return_buttons_to_normal_state()
            
        self._clear_btn["command"] = btn_clear_func

            
    def _return_buttons_to_normal_state(self):
        for btn in self._buttons.values():
            btn["state"] = "normal"
            btn["bg"] = BTN_BG

    def update_board(self):
        self._return_buttons_to_normal_state()


if __name__ == "__main__":
    pass
