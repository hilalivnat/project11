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
from ex11_helper import generate_score
from buttons import Buttons
from header import Header


######################################################################

class GameGui:
    def __init__(self) -> None:

        # tkinter vars
        root = tkinter.Tk()
        root.wm_resizable(False, False)
        root.geometry("750x650")
        self.__root = root

        self._main_frame = tkinter.Frame(self.__root,
                                         background=BACKGROUND_COLOR)

        self._start_photo = tkinter.PhotoImage(file=START_SCREEN)
        self._play_again_image = tkinter.PhotoImage(file=GAME_OVER_SCREEN)
        self._start_game_frame = tkinter.Label(self.__root,
                                               image=self._start_photo,
                                               background=WHITE)

        self._header = Header(self._main_frame)

        self._buttons: Buttons = Buttons(self.__root)

        self._found_words = tkinter.StringVar(self.__root, "")
        self._words_display = tkinter.Label(self._main_frame,
                                            textvariable=self._found_words,
                                            **FOUND_WORDS, background=BTN_BG)

        self._yes_image = tkinter.PhotoImage(file=YES_BUTTON)
        self._play_btn = tkinter.Button(self._start_game_frame,
                                        image=self._yes_image, background=WHITE)

        self._no_image = tkinter.PhotoImage(file=NO_BUTTON)
        self._exit_btn = tkinter.Button(self._start_game_frame,
                                        image=self._no_image,
                                        command=lambda: self.__root.destroy(),
                                        background=WHITE)

    def init_gui(self, play_func):
        self._start_game_frame.pack(fill=tkinter.BOTH, expand=True)
        self._play_btn["command"] = play_func
        self._play_btn.place(relx=0.43, rely=0.78)

    def run(self):
        self.__root.mainloop()

    def start_game(self):
        self._start_game_frame.pack_forget()
        self._header.start_game()
        self._main_frame.pack(fill=tkinter.BOTH, expand=True)
        self._words_display.pack(fill=tkinter.BOTH, expand=True, padx=15)
        self._buttons.load_buttons()
        self.__root.after(1000 * 60 * 3, self.game_over)

    def handel_btn_clicked(self, char, res):
        self._header.update_current_word(char)
        found_new_word, words, score = res
        if found_new_word:
            self._found_words.set(words)
            self._header.clear_current_word()
            self._header.update_score(score)
            self.update_board()

    def create_board(self, board, click_on_btn_f, clear_f):
        for row_i, row in enumerate(board):
            for col_i, char in enumerate(row):
                self._buttons.create_button((row_i, col_i),
                                            char, click_on_btn_f,
                                            self.handel_btn_clicked)

        def btn_clear_func():
            clear_f()
            self._header.clear_current_word()
            self._buttons.return_buttons_to_normal_state()

        self._header.update_clear_btn_command(btn_clear_func)

    def update_board(self):
        self._buttons.return_buttons_to_normal_state()

    def game_over(self):
        self._main_frame.pack_forget()
        self._play_btn.place(relx=0.35, rely=0.78)
        self._exit_btn.place(relx=0.50, rely=0.78)
        self._start_game_frame["image"] = self._play_again_image
        self._start_game_frame.pack(fill=tkinter.BOTH, expand=True)
        self._header.update_score(0)
        self._found_words.set("")
        self._header.clear_current_word()
        self._buttons.game_finished()
