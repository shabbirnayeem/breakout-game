# TODO: Create the screen
# TODO: Create the paddle
# TODO: Create the Ball
# TODO: Create the tiles on TOP
# TODO: Create class for the BAll to keep Moving
# TODO: Detect collision with hte wall and bounce
# TODO: Detect collision with the tiles and destroy the tiles
# TODO: Detect collision with the paddle
# TODO: Keep Score
# TODO: Extra life

from turtle import Screen
from turtle import Turtle
# screen setup
game_screen = Screen()
game_screen.title("BreakOut Game")
game_screen.setup(width=800, height=800)
game_screen.bgcolor("black")

pad = Turtle()

pad.shape("square")
pad.color("white")
pad.shapesize(stretch_wid=1, stretch_len=10)
pad.penup()
pad.goto(y=-350, x=0)
pad.speed(0)

def move_left():
    pad.back(3)


def move_right():
    pad.forward(3)


# start listening to key stocks

game_screen.listen()
game_screen.onkey(key="Left", fun=move_left)
game_screen.onkey(key="Right", fun=move_right)

game_screen.exitonclick()
