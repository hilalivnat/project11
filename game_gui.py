import tkinter
class GameGui:
    def __init__(self) -> None:
        root = tkinter.Tk()
        root.title("Boogle")
        root.resizable(False, False)
        self.__root = root
        
        self._title_label = tkinter.Label(root, text="Boogle", font=("Courier", 30))
        self._title_label.pack()
        
        self._button_frame = tkinter.Frame(root)
        self._button_frame.pack()

        self._display_word = tkinter.Label(root)
        self._display_word.pack()



    def run(self):
        self.__root.mainloop()

    def _create_button(self, coord, char):
        button = tkinter.Button(self._button_frame, text=char, command=lambda : print("hi"))
        button.grid(row=coord[0], column=coord[1])
        # button.pack()



    def create_board(self,board):
        print('board: ', board)
        # for i in range(4):
        tkinter.Grid.grid_configure(self._button_frame,column=4, row=4)
        for row_i, row in enumerate(len(board)):
            for col_i, char in enumerate(row):
                self._create_button((row_i, col_i), char)
                    

if __name__ == "__main__":
    game = GameGui()
    game.run()