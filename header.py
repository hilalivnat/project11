######################################################################
# FILE: header.py
# WRITERS: Michal_Caduri, michal.caduri, 213088735
# Hila_Livnat, hilalivnat, 324862028
# EXERCISE: intro2cs1 ex11 2023
# DESCRIPTION: A program defines the header in the GUI.
######################################################################
######################################################################
# imports:
import tkinter
from typing import *
from styles import *
from ex11_helper import *
from timer import Timer


######################################################################

class Header:
    """a class that contains the game header"""
    
    def __init__(self, main_frame) -> None:
        self._header = tkinter.Frame(main_frame,
                                     height=200,
                                     background=BACKGROUND_COLOR)

        self._logo_image = tkinter.PhotoImage(file=BOGGLE_LOGO)
        self._logo = tkinter.Label(self._header,
                                   image=self._logo_image,
                                   background=BACKGROUND_COLOR)
        self._logo.pack(expand=True)

        self._timer = Timer(self._header)

        self._current_word = tkinter.StringVar(self._header, "")
        self._display_word = tkinter.Label(self._header,
                                           textvariable=self._current_word,
                                           **DISPLAY_WORD,
                                           background=BACKGROUND_COLOR)
        self._display_word.pack(expand=True)

        self._game_score = tkinter.StringVar(self._header,
                                             generate_score(0))
        self._score_display = tkinter.Label(self._header,
                                            textvariable=self._game_score,
                                            **DISPLAY_WORD,
                                            background=BACKGROUND_COLOR)
        self._score_display.pack(expand=True)

        self._clear_image = tkinter.PhotoImage(file=CLEAR_BUTTON)
        self._clear_btn = tkinter.Button(self._header,
                                         image=self._clear_image,
                                         background=BACKGROUND_COLOR)
        self._clear_btn.pack(expand=True)

    def start_game(self):
        """pack header and start timer"""
        self._header.pack(expand=True)
        self._timer.start_timer()

    def update_current_word(self, char):
        """update presented word
        param char: new character"""
        self._current_word.set(self._current_word.get() + char)

    def clear_current_word(self):
        """clear presented word"""
        self._current_word.set("")
        # print("curr", self._current_word.get())

    def update_score(self, score):
        """update game score
        param score: new score"""
        self._game_score.set(generate_score(score))

    def update_clear_btn_command(self, btn_clear_func):
        """update clear btn's command"""
        self._clear_btn["command"] = btn_clear_func
