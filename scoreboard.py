from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.create()

    def create(self):
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(x=-270, y=260)
        self.write(f"LEVEL {self.level}", font=FONT)

    def redraw(self):
        self.clear()
        self.write(f"LEVEL {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def add_level(self):
        self.clear()
        self.level += 1
        self.redraw()
