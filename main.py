from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    # Detect car collision
    for c in car.all_cars:
        if c.distance(player) < 20:
            score.game_over()
            is_game_on = False

    # Detect win
    if player.ycor() > 280:
        score.add_level()
        player.go_to_start()
        car.add_level()












screen.exitonclick()

