# https://www.etutorialspoint.com/index.php/544-countdown-clock-and-timer-using-tkinter-in-python

import tkinter
from styles import *

INITIAL_TIME = "03:00"

class Timer:
    def __init__(self, main_frame) -> None:
        self._current_time = tkinter.StringVar(main_frame, INITIAL_TIME)
        self._timer_frame = tkinter.Label(main_frame, textvariable=self._current_time, **DISPLAY_WORD, background="white")
        self._timer_frame.pack(fill="y" , expand=True)  

    def start_timer(self):
        curr_time = self._current_time.get().split(":")
        user_input =int(curr_time[0])*60 + int(curr_time[1])  - 1
        mins,secs = divmod(user_input,60)
        
        mins = "".join("{0:2d}".format(mins).split())
        secs = "".join("{0:2d}".format(secs).split())
        
        if len(mins) < 2 : mins = f'0{mins}'
        if len(secs) < 2: secs = f'0{secs}'
        self._current_time.set(f'{mins}:{secs}')
        
        if (user_input > 0):
            self._timer_frame.after(1000, self.start_timer) 
        else:
            self._current_time.set(INITIAL_TIME)

    
    
