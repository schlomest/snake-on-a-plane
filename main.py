import tkinter as tk
from tkinter.constants import *

BOARD_SIZE = 200  # pixels
SQUARE_SIZE = 10  # pixels
x0, y0 = 5, 5
GRID_SIZE = BOARD_SIZE // SQUARE_SIZE


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

        # exit button
        self.quit = tk.Button(self, text="Close", fg="red",
                              command=self.master.destroy)
        self.quit.pack()

    def init_game(self):
        # create in-memory grid
        # self.grid_dict = dict(zip([x for x in range(BOARD_SIZE)], [dict(zip([y for y in range(BOARD_SIZE)], [0 for y in range(BOARD_SIZE)])) for]]))
        self.grid_dict = dict()
        for x in range(GRID_SIZE):
            self.grid_dict[x] = dict(
                zip([y for y in range(GRID_SIZE)], [0]*GRID_SIZE))

        # bind controls
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<a>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<d>", self.move_right)
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<w>", self.move_up)
        self.master.bind("<Down>", self.move_down)
        self.master.bind("<s>", self.move_down)

        # fill initial square
        self.head = [0, 0]
        self.grid_dict[self.head[0]][self.head[1]
                                     ] = self.fill_square(*self.head)

    def move_left(self, event):
        # delete current head on the UI
        self.delete_square(self.grid_dict[self.head[0]][self.head[1]])
        # erase current head in memory
        self.grid_dict[self.head[0]][self.head[1]] = 0

        # update head position
        if self.head[0] == 0:
            self.head[0] = GRID_SIZE - 1
        else:
            self.head[0] -= 1

        # draw new head position
        self.grid_dict[self.head[0]][self.head[1]
                                     ] = self.fill_square(*self.head)

    def move_right(self, event):
         # delete current head on the UI
        self.delete_square(self.grid_dict[self.head[0]][self.head[1]])
        # erase current head in memory
        self.grid_dict[self.head[0]][self.head[1]] = 0

        # update head position
        if self.head[0] == GRID_SIZE - 1:
            self.head[0] = 0
        else:
            self.head[0] += 1

        # draw new head position
        self.grid_dict[self.head[0]][self.head[1]
                                     ] = self.fill_square(*self.head)

    def move_up(self, event):
        # delete current head on the UI
        self.delete_square(self.grid_dict[self.head[0]][self.head[1]])
        # erase current head in memory
        self.grid_dict[self.head[0]][self.head[1]] = 0

        # update head position
        if self.head[1] == 0:
            self.head[1] = GRID_SIZE - 1
        else:
            self.head[1] -= 1

        # draw new head position
        self.grid_dict[self.head[0]][self.head[1]
                                     ] = self.fill_square(*self.head)

    def move_down(self, event):
        # delete current head on the UI
        self.delete_square(self.grid_dict[self.head[0]][self.head[1]])
        # erase current head in memory
        self.grid_dict[self.head[0]][self.head[1]] = 0

        # update head position
        if self.head[1] == GRID_SIZE - 1:
            self.head[1] = 0
        else:
            self.head[1] += 1

        # draw new head position
        self.grid_dict[self.head[0]][self.head[1]
                                     ] = self.fill_square(*self.head)

    def fill_square(self, x, y):
        return self.board.create_polygon(
            x0 + (x * SQUARE_SIZE), y0 + (y * SQUARE_SIZE),
            x0 + (x * SQUARE_SIZE) + SQUARE_SIZE, y0 + (y * SQUARE_SIZE),
            x0 + (x * SQUARE_SIZE) + SQUARE_SIZE, y0 +
            (y * SQUARE_SIZE) + SQUARE_SIZE,
            x0 + (x * SQUARE_SIZE), y0 + (y * SQUARE_SIZE) + SQUARE_SIZE,
            x0 + (x * SQUARE_SIZE), y0 + (y * SQUARE_SIZE))

    def delete_square(self, square_id):
        self.board.delete(square_id)


root = tk.Tk()
app = SnakeApp(master=root)
app.mainloop()
