from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.speed(0)
        self.penup()
        self.refresh()
        self.color("blue")
    def refresh(self):
        self.goto(random.randint(-280,280), random.randint(-280,280))