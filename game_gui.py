import tkinter
class GameGui:
    def __init__(self) -> None:
        root = tkinter.Tk()
        root.title("Boogle")
        root.resizable(False, False)
        self.__root = root
        
        self._title_label = tkinter.Label(self.__root, text="Boogle", font=("Courier", 30))
        self._title_label.grid(row=0, column=0)
        
        self._buttons_frame = tkinter.Frame(self.__root)
        # tkinter.Grid.grid_configure(self._button_frame,column=4, row=4)
        self._buttons_frame.grid(row=1, column=0)
        # self._buttons_frame.grid_configure()

        self._display_word = tkinter.Label(self.__root, text="kk")
        self._display_word.grid(row=2, column=0)



    def run(self):
        self.__root.mainloop()

    def _create_button(self, coord, char):
        print('coord: ', coord)
        button = tkinter.Button(self._buttons_frame, text=char, font=("Asimon", 15), command= lambda:print(coord))
        button.grid(row=coord[0] + 2, column=coord[1],sticky=tkinter.NSEW, rowspan=1, columnspan=1)
        # button.pack()



    def create_board(self,board):
        print('board: ', board)
        # for i in range(4):
            # tkinter.Grid.grid_configure(self._buttons_frame,column=4, row=4)
        for row_i, row in enumerate(board):
            for col_i, char in enumerate(row):
                self._create_button((row_i, col_i), char)

        
            

if __name__ == "__main__":
    game = GameGui()
    game.run()