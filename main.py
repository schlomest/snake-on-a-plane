import tkinter
from tkinter.constants import *

BOARD_SIZE = 200
SQUARE_SIZE = 10
x0, y0 = 5, 5


tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RAISED, borderwidth=2)
frame.pack(fill=BOTH,expand=1)

label = tkinter.Label(frame, text="Snake on a Plane")
label.pack(fill=X, expand=1)

# create in memory grid
grid = [[y for y in range(BOARD_SIZE)] for x in range(BOARD_SIZE)]

# for x, x_list in enumerate(grid):
#     for y in x_list:
#         print(x, y)

board = tkinter.Canvas(frame, width=BOARD_SIZE*1.2, height=BOARD_SIZE*1.2)
board.create_rectangle(x0, y0, x0 + BOARD_SIZE, y0 + BOARD_SIZE)

# draw grid
for i in range(0, BOARD_SIZE, SQUARE_SIZE):
    board.create_line(x0 + i, y0, x0 + i, y0 + BOARD_SIZE)
    board.create_line(x0, y0 + i, x0 + BOARD_SIZE, y0 + i)

board.pack(fill=BOTH, expand=1)

board.create_polygon(
    x0, y0,
    x0 + SQUARE_SIZE, y0,
    x0 + SQUARE_SIZE, y0 + SQUARE_SIZE,
    x0, y0 + SQUARE_SIZE,
    x0, y0)

button = tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()