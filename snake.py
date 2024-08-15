from turtle import Turtle
MOVING_DISTANCES = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.body = []
        for i in STARTING_POSITIONS:
            self.create_body(i)
            self.head = self.body[0]
    def create_body(self,position):
            body_part = Turtle(shape="square")
            body_part.penup()
            body_part.color("white")
            self.body.append(body_part)
            body_part.goto(position)
    def increase_size(self,how_much):
        for i in range(how_much):
            self.create_body(self.body[-1].position())
    def __make_body_ready_to_move(self):
        for i in range(len(self.body)):
            if i == 0:
                continue
            # g = 1*i
            g = i
            self.body[len(self.body)-g].goto(self.body[len(self.body)-g-1].xcor(),self.body[len(self.body)-g-1].ycor())
    def move(self):
        self.__make_body_ready_to_move()
        self.head.forward(MOVING_DISTANCES)
    def turn_right(self):
        self.__make_body_ready_to_move()
        self.head.right(90)
        self.head.forward(MOVING_DISTANCES)
    def turn_left(self):
        self.__make_body_ready_to_move()
        self.head.left(90)
        self.head.forward(MOVING_DISTANCES)
    def moveloop(self):
        while True:
            self.move()
    def right(self):
        if self.head.heading() == 180:
            return None
        self.head.setheading(0)

    def left(self):
        if self.head.heading() == 0:
            return None
        self.head.setheading(180)
    def Up(self):
        if self.head.heading() == 270:
            return None
        self.head.setheading(90)
    def Down(self):
        if self.head.heading() == 90:
            return None
        self.head.setheading(270)
    def reset(self):
        for i in self.body:
            i.reset()
            i.hideturtle()
    def clear(self):
        for i in self.body:
            i.clear()