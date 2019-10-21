from time import sleep


# the snake is a reverse linked-list. The head is the last node
# in the linked list. The tail is the first
class Snake():
    def __init__(self):
        self.alive = True
        self.head = self.SnakeNode(5, 5)
        self.tail = self.SnakeNode(3, 5)
        self.tail.next = self.SnakeNode(4, 5)
        self.tail.next.next = self.head
        self.direction = "RIGHT"

    def add_section(self, x, y):
        self.tail = self.SnakeNode(x, y)

    class SnakeNode():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.next = None
