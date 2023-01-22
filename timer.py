######################################################################
# FILE: timer.py
# WRITERS: Michal_Caduri, michal.caduri, 213088735
# Hila_Livnat, hilalivnat, 324862028
# EXERCISE: intro2cs1 ex11 2023
# DESCRIPTION: A program defines the timer in the GUI.
# WEB PAGE WE USED: https://www.etutorialspoint.com/
# index.php/544-countdown-clock-and-timer-using-tkinter-in-python
######################################################################
######################################################################
# imports:
import tkinter
from styles import *
######################################################################

INITIAL_TIME = "03:00"


class Timer:
    """a class that controls game timer"""
    def __init__(self, main_frame) -> None:
        """param main_frame: reference to container"""
        self._current_time = tkinter.StringVar(main_frame, INITIAL_TIME)
        self._timer_frame = tkinter.Label(main_frame,
                                          textvariable=self._current_time,
                                          **DISPLAY_WORD,
                                          background=BACKGROUND_COLOR)
        self._timer_frame.pack(fill="y", expand=True)

    def start_timer(self):
        """start the timer"""

        curr_time = self._current_time.get().split(":")
        time_in_seconds =int(curr_time[0])*60 + int(curr_time[1]) - 1
        mins, secs = divmod(time_in_seconds, 60)
        
        mins = "".join("{0:2d}".format(mins).split())
        secs = "".join("{0:2d}".format(secs).split())
        
        if len(mins) < 2 : mins = f'0{mins}'
        if len(secs) < 2: secs = f'0{secs}'
        self._current_time.set(f'{mins}:{secs}')
        
        # update the timer after a second
        if time_in_seconds > 0:
            self._timer_frame.after(1000, self.start_timer) 
        else:
            self._current_time.set(INITIAL_TIME)

    
    
