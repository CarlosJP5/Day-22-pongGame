from turtle import Turtle
PLAYER_START = [(-360, -20), (-360, 0), (-360, 20)]
PC_START = [(360, -20), (360, 0), (360, 20)]
TOP = 250
BOT = -250
MOVE_DISTANCE = 25


class Paddle:

    def __init__(self):
        self.player = []
        self.pc = []
        for position in PLAYER_START:
            body = Turtle(shape="square")
            body.color("white")
            body.penup()
            body.goto(position)
            self.player.append(body)

        for positions in PC_START:
            body = Turtle(shape="square")
            body.color("white")
            body.penup()
            body.goto(positions)
            self.pc.append(body)

        self.player_head = self.player[0]
        self.pc_head = self.pc[0]

    def move_up(self):
        self.player_head = self.player[-1]
        if self.player_head.ycor() <= TOP:
            for body in self.player:
                body.setheading(90)
                body.forward(MOVE_DISTANCE)

    def move_down(self):
        self.player_head = self.player[0]
        if self.player_head.ycor() >= BOT:
            for body in self.player:
                body.setheading(270)
                body.forward(MOVE_DISTANCE)
