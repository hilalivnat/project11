import tkinter
from typing import *
from styles import *
from ex11_helper import *
from timer import Timer

class Header:
    def __init__(self, main_frame) -> None:
        self._header = tkinter.Frame(main_frame, width=50, height=50, bg="")

        self._timer = Timer(self._header)

        self._current_word = tkinter.StringVar(self._header, "")
        self._display_word = tkinter.Label(self._header, textvariable=self._current_word,  **DISPLAY_WORD)
        self._display_word.pack(expand=True)
        
        self._game_score = tkinter.StringVar(self._header, generate_score(0))
        self._score_display = tkinter.Label(self._header, textvariable=self._game_score,  **DISPLAY_WORD)
        self._score_display.pack(expand=True)
       
        self._clear_btn = tkinter.Button(self._header, text="clear")
        self._clear_btn.pack(expand=True)

    def start_game(self):
         self._header.pack(expand=True)   
         self._timer.start_timer()

    def update_current_word(self, char):
        self._current_word.set(self._current_word.get() + char)     

    def clear_current_word(self):
        self._current_word.set("")

    def update_score(self, score):
        self._game_score.set(generate_score(score))  

    def update_clear_btn_command(self, btn_clear_func):
        self._clear_btn["command"] = btn_clear_func 