import tkinter as tk
from tkinter.constants import *
from threading import Thread
from time import sleep

from snake_board import SnakeBoard
# from snake import Snake

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

        # create game board
        self.board = SnakeBoard(self)

        # exit button
        self.quit = tk.Button(self, text="Close", fg="red",
                              command=self.kill_snake)
        self.quit.pack()

    def init_game(self):
        # create in-memory grid
        self.grid_dict = dict()
        for x in range(GRID_SIZE):
            self.grid_dict[x] = dict(
                zip([y for y in range(GRID_SIZE)], [0]*GRID_SIZE))

        # bind controls
        self.master.bind("<Left>", self.turn_left)
        self.master.bind("<a>", self.turn_left)
        self.master.bind("<Right>", self.turn_right)
        self.master.bind("<d>", self.turn_right)
        self.master.bind("<Up>", self.turn_up)
        self.master.bind("<w>", self.turn_up)
        self.master.bind("<Down>", self.turn_down)
        self.master.bind("<s>", self.turn_down)

        # create snake
        # self.snake = Snake()

        # fill initial square
        self.head = [0, 0]
        self.grid_dict[self.head[0]][self.head[1]
                                     ] = self.board.fill_square(*self.head)
        
        # new grid update method
        # self.update_grid(self.snake.head.x, self.snake.head.y)

        # start snake thread for movement
        self.active = True
        self.direction = "RIGHT"
        self.snake_thread = Thread(target=self.move_snake)
        self.snake_thread.start()

    def update_grid(self, x, y):
        self.grid_dict[x, y] = self.board.fill_square(x ,y)

    def move_snake(self):
        while self.active:
            if self.direction == "LEFT":
                self.move_left()
            elif self.direction == "RIGHT":
                self.move_right()
            elif self.direction == "UP":
                self.move_up()
            elif self.direction == "DOWN":
                self.move_down()

            sleep(.5)

    def kill_snake(self):
        self.active = False
        self.snake_thread.join()
        self.master.destroy()

    def turn_left(self, event):
        self.direction = "LEFT"

    def turn_right(self, event):
        self.direction = "RIGHT"

    def turn_up(self, event):
        # drink responsibly
        self.direction = "UP"

    def turn_down(self, event):
        # for what?
        self.direction = "DOWN"

    def move_left(self):
        # delete current head on the UI
        self.board.delete_square(self.grid_dict[self.head[0]][self.head[1]])
        # erase current head in memory
        self.grid_dict[self.head[0]][self.head[1]] = 0

        # update head position
        if self.head[0] == 0:
            self.head[0] = GRID_SIZE - 1
        else:
            self.head[0] -= 1

        # draw new head position
        self.grid_dict[self.head[0]][self.head[1]
                                     ] = self.board.fill_square(*self.head)

    def move_right(self):
         # delete current head on the UI
        self.board.delete_square(self.grid_dict[self.head[0]][self.head[1]])
        # erase current head in memory
        self.grid_dict[self.head[0]][self.head[1]] = 0

        # update head position
        if self.head[0] == GRID_SIZE - 1:
            self.head[0] = 0
        else:
            self.head[0] += 1

        # draw new head position
        self.grid_dict[self.head[0]][self.head[1]
                                     ] = self.board.fill_square(*self.head)

    def move_up(self):
        # delete current head on the UI
        self.board.delete_square(self.grid_dict[self.head[0]][self.head[1]])
        # erase current head in memory
        self.grid_dict[self.head[0]][self.head[1]] = 0

        # update head position
        if self.head[1] == 0:
            self.head[1] = GRID_SIZE - 1
        else:
            self.head[1] -= 1

        # draw new head position
        self.grid_dict[self.head[0]][self.head[1]
                                     ] = self.board.fill_square(*self.head)

    def move_down(self):
        # delete current head on the UI
        self.board.delete_square(self.grid_dict[self.head[0]][self.head[1]])
        # erase current head in memory
        self.grid_dict[self.head[0]][self.head[1]] = 0

        # update head position
        if self.head[1] == GRID_SIZE - 1:
            self.head[1] = 0
        else:
            self.head[1] += 1

        # draw new head position
        self.grid_dict[self.head[0]][self.head[1]
                                     ] = self.board.fill_square(*self.head)


root = tk.Tk()
app = SnakeApp(master=root)
app.mainloop()
