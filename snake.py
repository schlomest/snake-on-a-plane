from time import sleep

from snake_board import GRID_SIZE


class Snake():
    def __init__(self, snake_board):
        self.board = snake_board
        self.alive = True
        self.body = [[5, 5], [4, 5], [3, 5]]
        self.body_ui = [snake_board.fill_square(self.body[0][0], self.body[0][1]),
                        snake_board.fill_square(self.body[1][0], self.body[1][1]),
                        snake_board.fill_square(self.body[2][0], self.body[2][1])]
        self.direction = "RIGHT"

    def move(self):
        self.body.pop()

        if self.direction == "RIGHT":
            self.body.insert(0, [self.body[0][0] + 1, self.body[0][1]])
        elif self.direction == "LEFT":
            self.body.insert(0, [self.body[0][0] - 1, self.body[0][1]])
        elif self.direction == "UP":
            self.body.insert(0, [self.body[0][0], self.body[0][1] - 1])
        elif self.direction == "DOWN":
            self.body.insert(0, [self.body[0][0], self.body[0][1] + 1])

        # make sure snake doesn't go off board
        if self.body[0][0] == GRID_SIZE:
            self.body[0][0] = 0
        elif self.body[0][1] == GRID_SIZE:
            self.body[0][1] = 0
        elif self.body[0][0] == -1:
            self.body[0][0] = GRID_SIZE - 1
        elif self.body[0][1] == -1:
            self.body[0][1] = GRID_SIZE - 1

        # update UI
        self.board.delete_square(self.body_ui.pop())
        self.body_ui.insert(0, self.board.fill_square(self.body[0][0], self.body[0][1]))
    
    def grow(self):
        if self.direction == "RIGHT":
            self.body.insert(0, [self.body[0][0] + 1, self.body[0][1]])
        elif self.direction == "LEFT":
            self.body.insert(0, [self.body[0][0] - 1, self.body[0][1]])
        elif self.direction == "UP":
            self.body.insert(0, [self.body[0][0], self.body[0][1] - 1])
        elif self.direction == "DOWN":
            self.body.insert(0, [self.body[0][0], self.body[0][1] + 1])

        # make sure snake doesn't go off board
        if self.body[0][0] == GRID_SIZE:
            self.body[0][0] = 0
        elif self.body[0][1] == GRID_SIZE:
            self.body[0][1] = 0
        elif self.body[0][0] == -1:
            self.body[0][0] = GRID_SIZE - 1
        elif self.body[0][1] == -1:
            self.body[0][1] = GRID_SIZE - 1

        # update UI
        self.body_ui.insert(0, self.board.fill_square(self.body[0][0], self.body[0][1]))
    