import tkinter as tk
from random import randrange
from threading import Thread
from time import sleep
from tkinter.constants import X

from snake import Snake
from snake_board import GRID_SIZE, SnakeBoard


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
        self.snake = Snake(self.board)

        self.food = [randrange(GRID_SIZE), randrange(GRID_SIZE)]
        self.add_food()

        # start snake movenment thread
        self.snake_thread = Thread(target=self.move_snake)
        self.snake_thread.start()

    def move_snake(self):
        while self.snake.alive:
            if self.snake.body[0] == self.food:
                self.snake.grow()
                self.eat_food()
                self.add_food()
            else:
                self.snake.move()
            sleep(.2)

    def kill_snake(self):
        self.snake.alive = False
        self.snake_thread.join()
        self.master.destroy()

    def turn_left(self, event):
        if not self.snake.direction == "RIGHT":
            self.snake.direction = "LEFT"

    def turn_right(self, event):
        if not self.snake.direction == "LEFT":
            self.snake.direction = "RIGHT"

    def turn_up(self, event):
        # drink responsibly
        if not self.snake.direction == "DOWN":
            self.snake.direction = "UP"

    def turn_down(self, event):
        # for what?
        if not self.snake.direction == "UP":
            self.snake.direction = "DOWN"

    def add_food(self):
        while self.food in self.snake.body:
            self.food = [randrange(GRID_SIZE), randrange(GRID_SIZE)]
        
        self.food_id = self.board.fill_square(self.food[0], self.food[1])

    def eat_food(self):
        self.board.delete_square(self.food_id)


root = tk.Tk()
app = SnakeApp(master=root)
app.master.title("Snake on a Plane")
app.master.maxsize(250, 280)
app.master.minsize(200, 250)
app.mainloop()
