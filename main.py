from turtle import Screen
from paletas import Paddle

# TODO: Create Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=540)
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

# TODO: Create and move Paddle
paddle = Paddle()
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")

# TODO: Create another paddle
# Game Start
game_on = True
while game_on:
    screen.update()
    # paddle.pc_move()



# TODO: Create de Ball and make move
# TODO: Detect collision with wall
# TODO: Detect collision with paddle
# TODO: Detect when paddle misses
# TODO: Keep Score
screen.exitonclick()
