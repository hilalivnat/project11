# https://www.etutorialspoint.com/index.php/544-countdown-clock-and-timer-using-tkinter-in-python

import tkinter


class Timer:
    def __init__(self, main_frame) -> None:
        self._minute = tkinter.StringVar(main_frame, "03:00")
        self._timer_frame = tkinter.Label(main_frame, width=3, textvariable=self._minute)

    def start_timer(self, pack_timer=False):
        if pack_timer: self._pack_timer_frame()
        curr_time = self._minute.get().split(":")
        user_input =int(curr_time[0])*60 + int(curr_time[1])  - 1
        mins,secs = divmod(user_input,60)
        
        mins = "".join("{0:2d}".format(mins).split())
        secs = "".join("{0:2d}".format(secs).split())
        
        if len(mins) < 2 : mins = f'0{mins}'
        if len(secs) < 2: secs = f'0{secs}'
        self._minute.set(f'{mins}:{secs}')
        
        if (user_input > 0):
            self._timer_frame.after(1000, self.start_timer)    
    
    
    def _pack_timer_frame(self):
        self._timer_frame.pack(fill=tkinter.BOTH, expand=True)  
