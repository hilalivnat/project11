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
from header import Header


######################################################################

class GameGui:
    def __init__(self) -> None:

        # tkinter vars
        root = tkinter.Tk()
        root.title("Boggle")
        root.geometry("750x450")
        self.__root = root

        self._game_template = tkinter.PhotoImage(file="./assets/game_template.png")
        self._main_frame = tkinter.Frame(self.__root)
        
        # self._background_game = tkinter.Label(self._main_frame, image=self._game_template).pack(expand=True)

        self._start_photo = tkinter.PhotoImage(file="./assets/start_screen.png")
        self._start_game_frame = tkinter.Label(self.__root, image=self._start_photo)
        
        self._play_text = tkinter.StringVar(self._start_game_frame, "play")
        self._header = Header(self._main_frame)
        
        self._buttons: Buttons = Buttons(self.__root)

        self._found_words = tkinter.StringVar(self.__root, "")
        self._words_display = tkinter.Label(self._main_frame, textvariable=self._found_words, **FOUND_WORDS)

        
    def init_gui(self, play_func):
        self._start_game_frame.pack(fill=tkinter.BOTH, expand=True,)
        self._play_btn = tkinter.Button(self._start_game_frame, textvariable=self._play_text, command=play_func, **START_GAME_BTN)
        self._play_btn.place(relx=0.4, rely=0.75)

        self._close_game =  tkinter.Button(self._start_game_frame, text="exit")
    
    def run(self):
        self.__root.mainloop()

    def start_game(self):
        self._start_game_frame.pack_forget() 
        self._header.start_game()
        self._main_frame.pack(fill=tkinter.BOTH, expand=True)
        self._words_display.pack(fill=tkinter.BOTH, expand=True)
        self._buttons.load_buttons()
        self.__root.after(1000*60*3, self.game_over)


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
                self._buttons.create_button((row_i, col_i), char, click_on_btn_f, self.handel_btn_clicked)

        def btn_clear_func():
            clear_f()
            self._header.clear_current_word()
            self._buttons.return_buttons_to_normal_state()

        self._header.update_clear_btn_command(btn_clear_func)

    def update_board(self):
        self._buttons.return_buttons_to_normal_state()

    def game_over(self):
        self._main_frame.pack_forget()
        self._start_game_frame.pack(fill=tkinter.BOTH, expand=True,)
        self._header.update_score(0)
        self._found_words.set("")
        self._header.clear_current_word()
        self._close_game.pack(expand=True)
        self._play_text.set("play again")
        self._buttons.game_finished()

if __name__ == "__main__":
    pass
