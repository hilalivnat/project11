import tkinter
from typing import *
from styles import *
from ex11_helper import *
from timer import Timer

class Header:
    def __init__(self, main_frame) -> None:
        self._header = tkinter.Frame(main_frame, height=200, background="white")

        self._logo_image = tkinter.PhotoImage(file="./assets/re_boggle_logo.png")
        self._logo = tkinter.Label(self._header, image=self._logo_image, background="white")
        self._logo.pack(expand=True)

        self._timer = Timer(self._header)

        self._current_word = tkinter.StringVar(self._header, "")
        self._display_word = tkinter.Label(self._header, textvariable=self._current_word, **DISPLAY_WORD, background="white")
        self._display_word.pack(expand=True)
        
        self._game_score = tkinter.StringVar(self._header, generate_score(0))
        self._score_display = tkinter.Label(self._header, textvariable=self._game_score,  **DISPLAY_WORD, background="white")
        self._score_display.pack(expand=True)
       
        self._clear_image = tkinter.PhotoImage(file="./assets/re_clear_button.png")
        self._clear_btn = tkinter.Button(self._header, image=self._clear_image)
        self._clear_btn.pack(expand=True)

    def start_game(self):
         self._header.pack(expand=True)   
         self._timer.start_timer()

    def update_current_word(self, char):
        self._current_word.set(self._current_word.get() + char)     

    def clear_current_word(self):
        self._current_word.set("")
        print("curr",self._current_word.get())

    def update_score(self, score):
        self._game_score.set(generate_score(score))  

    def update_clear_btn_command(self, btn_clear_func):
        self._clear_btn["command"] = btn_clear_func 