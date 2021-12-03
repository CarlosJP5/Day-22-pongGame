from turtle import Turtle
import random
TURN = ["left", "right"]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()

    def start(self):
        self.home()
        self.setheading(180)
        self.turns()

    def move(self):
        self.forward(10)

    def paddle_hit(self):
        if self.xcor() < 0:
            self.setheading(0)
            self.turns()
        else:
            self.setheading(180)
            self.turns()

    def turns(self):
        turn = random.choice(TURN)
        if turn == "left":
            self.left(random.randint(-45, 45))
        else:
            self.left(random.randint(-45, 45))
        self.move()
