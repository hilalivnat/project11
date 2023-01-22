######################################################################
# FILE: buttons.py
# WRITERS: Michal_Caduri, michal.caduri, 213088735
# Hila_Livnat, hilalivnat, 324862028
# EXERCISE: intro2cs1 ex11 2023
# DESCRIPTION: A program defines the buttons in the GUI.
######################################################################
######################################################################
# imports:
import tkinter
import uuid
from typing import *
from styles import *
######################################################################
class Buttons:
    """a class that controls all the character's buttons in the game"""
    def __init__(self, root) -> None:
        """param root: frame container"""
        self._buttons_frame = tkinter.Frame(root, borderwidth=15, background=BACKGROUND_COLOR)
        
        self._buttons: Dict[uuid.UUID, tkinter.Button] = dict()

    def _return_to_regular_color(self, btn_id):
        """return the buttons to normal state"""
        def handler():
            self._buttons[btn_id]["bg"] = BTN_BG
        return handler    

    def _create_button_command(self, model_handel_click, board_handel_click,
                               cell_data: Tuple[Tuple, str, str]):
        """create a commend to handel button clicked
        param model_handel_click: method from game model
        param board_handel_click: method from the main gui class
        param cell_data: a tuple contains btn data -
        cell on board, char, id """
        
        cell, char, btn_id = cell_data
        def handler():
            res = model_handel_click(cell)
            if not bool(res):
                self._buttons[btn_id]["bg"] = INVALID_COLOR
                self._buttons_frame.after(
                    100, self._return_to_regular_color(btn_id))
                return
            self._buttons[btn_id]["state"] = "disabled"
            self._buttons[btn_id]["bg"] = DISABLED_COLOR
            board_handel_click(char, res)
        return handler

    def create_button(self, coord, char,
                      model_handel_click, board_handel_click):
        """creates a new btn on board
        param coord: coordinate on board
        param char: character on btn 
        param model_handel_click: method from game model
        param board_handel_click: method from the main gui class"""
        self._buttons_frame.grid_rowconfigure(coord[0],
                                              weight=1, uniform="True")
        self._buttons_frame.grid_columnconfigure(coord[1],
                                                 weight=1, uniform="True")
        
        btn_id = uuid.uuid4()
        button = tkinter.Button(self._buttons_frame, text=char,
                                command=self._create_button_command(
                                    model_handel_click, board_handel_click,
                                    (coord, char, btn_id)), **BUTTON_STYLE)
        button.grid(row=coord[0], column=coord[1],
                    sticky=tkinter.NSEW, rowspan=1, columnspan=1)
        self._buttons[btn_id] = button
    
    def return_buttons_to_normal_state(self):
        """returns all buttons in the board to regular state"""
        for btn in self._buttons.values():
            btn["state"] = "normal"
            btn["bg"] = BTN_BG

    def load_buttons(self):
        """loads all btns on board"""
        self._buttons_frame.pack(fill=tkinter.BOTH,
                                 expand=True, side=tkinter.BOTTOM)

    def game_finished(self):
        """handel buttons when the game is over"""
        self._buttons_frame.pack_forget()
        for button in self._buttons.values():
            # button.grid_forget()
            button.grid_remove()   
        self._buttons = dict()    
        
        