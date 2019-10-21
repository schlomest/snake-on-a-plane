import tkinter as tk

BOARD_SIZE = 200  # pixels
SQUARE_SIZE = 10  # pixels
x0, y0 = 5, 5
GRID_SIZE = BOARD_SIZE // SQUARE_SIZE


class SnakeBoard(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master, width=BOARD_SIZE+x0, height=BOARD_SIZE+y0)

        self.create_rectangle(x0, y0, x0 + BOARD_SIZE, y0 + BOARD_SIZE)

        for i in range(0, BOARD_SIZE, SQUARE_SIZE):
            self.create_line(x0 + i, y0, x0 + i, y0 + BOARD_SIZE)
            self.create_line(x0, y0 + i, x0 + BOARD_SIZE, y0 + i)

        self.pack()

    def fill_square(self, x, y):
        return self.create_polygon(
            x0 + (x * SQUARE_SIZE), y0 + (y * SQUARE_SIZE),
            x0 + (x * SQUARE_SIZE) + SQUARE_SIZE, y0 + (y * SQUARE_SIZE),
            x0 + (x * SQUARE_SIZE) + SQUARE_SIZE, y0 +
            (y * SQUARE_SIZE) + SQUARE_SIZE,
            x0 + (x * SQUARE_SIZE), y0 + (y * SQUARE_SIZE) + SQUARE_SIZE,
            x0 + (x * SQUARE_SIZE), y0 + (y * SQUARE_SIZE))

    def delete_square(self, square_id):
        self.delete(square_id)
