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

# screen setup
game_screen = Screen()
game_screen.title("BreakOut Game")
game_screen.setup(width=800, height=800)
game_screen.bgcolor("black")


game_screen.exitonclick()
