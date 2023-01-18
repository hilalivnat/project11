import tkinter
import uuid
from typing import *
from styles import *
from ex11_helper import *

class Buttons:
    def __init__(self, root) -> None:
        self._buttons_frame = tkinter.Frame(root)
        
        self._buttons: Dict[uuid.UUID,tkinter.Button] = dict()

    def return_to_regular_color(self, btn_id):
        def handler():
            self._buttons[btn_id]["bg"] = BTN_BG
        return handler    

    def create_button_command(self, model_handel_click, board_handel_click, cell_data:Tuple[Tuple,str, str]):
        cell, char, btn_id = cell_data
        def handler():
            res = model_handel_click(cell)
            if not bool(res):
                self._buttons[btn_id]["bg"] = "red"
                self._buttons_frame.after(100,  self.return_to_regular_color(btn_id))
                return
            self._buttons[btn_id]["state"] = "disabled"
            self._buttons[btn_id]["bg"] = DISABLED_COLOR
            board_handel_click(char, res)
        return handler

    def create_button(self, coord, char, model_handel_click, board_handel_click):
        self._buttons_frame.grid_rowconfigure(coord[0], weight=1, uniform="True")
        self._buttons_frame.grid_columnconfigure(coord[1], weight=1, uniform="True")
        
        btn_id = uuid.uuid4()
        button = tkinter.Button(self._buttons_frame,
                                text=char,
                                command=self.create_button_command(model_handel_click, board_handel_click, (coord, char, btn_id)), **BUTTON_STYLE)
        button.grid(row=coord[0], column=coord[1], sticky=tkinter.NSEW, rowspan=1, columnspan=1)
        self._buttons[btn_id] = button
    
    def return_buttons_to_normal_state(self):
        for btn in self._buttons.values():
            btn["state"] = "normal"
            btn["bg"] = BTN_BG

    def load_buttons(self):
        self._buttons_frame.pack(fill=tkinter.BOTH, expand=True,side=tkinter.BOTTOM )

    def game_finished(self):
        self._buttons_frame.pack_forget()
        for button in self._buttons.values():
            # button.grid_forget()
            button.grid_remove()   
        self._buttons = dict()    
        
        