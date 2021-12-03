from turtle import Screen
from paletas import Paddle
from ball import Ball
import time


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

# TODO: Create de Ball and make move
ball = Ball()

# TODO: Create another paddle
# Game Start
ball.start()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    # TODO: Detect collision with wall
    # TODO: Detect collision with paddle
    for part in paddle.player:
        if part.distance(ball) <= 30:
            print("hit")
            ball.paddle_hit()
# TODO: Detect when paddle misses
# TODO: Keep Score
screen.exitonclick()
