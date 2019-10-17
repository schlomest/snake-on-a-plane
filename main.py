import tkinter as tk
from tkinter.constants import *

BOARD_SIZE = 200
SQUARE_SIZE = 10
x0, y0 = 5, 5


class SnakeApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.init_game()

    def create_widgets(self):
        self.label = tk.Label(self, text="Snake on a Plane")
        self.label.pack(fill=X, expand=1)

        # draw grid
        self.board = tk.Canvas(self, width=BOARD_SIZE+x0, height=BOARD_SIZE+y0)
        self.board.create_rectangle(x0, y0, x0 + BOARD_SIZE, y0 + BOARD_SIZE)

        for i in range(0, BOARD_SIZE, SQUARE_SIZE):
            self.board.create_line(x0 + i, y0, x0 + i, y0 + BOARD_SIZE)
            self.board.create_line(x0, y0 + i, x0 + BOARD_SIZE, y0 + i)

        self.board.pack()

        # test button
        self.fill_button = tk.Button(self)
        self.fill_button["text"] = "fill square"
        self.fill_button["command"] = self.fill_square
        self.fill_button.pack()

        # exit button
        self.quit = tk.Button(self, text="Close", fg="red",
                              command=self.master.destroy)
        self.quit.pack()

    def init_game(self):
        # create in memory grid
        # grid = [[y for y in range(BOARD_SIZE)] for x in range(BOARD_SIZE)]
        pass

    def fill_square(self):
        self.board.create_polygon(
            x0, y0,
            x0 + SQUARE_SIZE, y0,
            x0 + SQUARE_SIZE, y0 + SQUARE_SIZE,
            x0, y0 + SQUARE_SIZE,
            x0, y0)


root = tk.Tk()
app = SnakeApp(master=root)
app.mainloop()
