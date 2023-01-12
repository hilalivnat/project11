import tkinter

class buttons:
    def __init__(self, root) -> None:
        self._buttons_frame = tkinter.Frame(self._main_frame)
        self._buttons_frame.pack(fill=tkinter.BOTH, expand=True)
        