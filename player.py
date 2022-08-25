from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_SPEED = 20


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)


    def move(self):
        self.forward(MOVE_SPEED)

    def go_to_start(self):
        self.goto(STARTING_POSITION)