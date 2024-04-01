from turtle import *
import random

########################## CLASS AND FUNCTION DEFINITIONS ##########################
class MysteryOne(Turtle):
    def __init__(self, x, y, key):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.goto(x,y)
        self.shape("turtle")
        self.screen = screen
        self.screen.onkeypress(self.draw, key)

    def draw(self):
        for i in range(4):
            if i%2==0:
                self.color("red")
            else:
                self.color("blue")
            self.begin_fill()
            for i in range(4):
                self.forward(20)
                self.right(90)
            self.end_fill()
            self.forward(20)
            
class MysteryTwo(Turtle):
    def __init__(self, x, y, key):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.goto(x,y)
        self.shape("turtle")
        self.screen = screen
        self.screen.onkeypress(self.draw, key)

    def draw(self):
        for i in range(10):
            if i%2==0:
                self.color("light blue")
            else:
                self.color("blue")
            self.begin_fill()
            for i in range(4):
                self.circle(20)
            self.end_fill()
            self.right(36)
            self.penup()
            self.forward(20)
            self.pendown()

class MysteryThree(Turtle):
    def __init__(self, x, y, key):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.goto(x,y)
        self.shape("turtle")
        self.screen = screen
        self.screen.onkeypress(self.draw, key)

    def draw(self):
        self.color("white")
        self.begin_fill()
        for i in range(5):
            self.forward(100)
            self.right(144)
        self.end_fill()
            
########################## PROGRAM ##########################
screen = Screen()
screen.bgcolor("black")
screen.listen()

# one = MysteryOne(-100,0)
# one.draw()

one = MysteryOne(-200,0,"a")
two = MysteryTwo(0,0,"b")
three = MysteryThree(200,0,"c")


screen.mainloop()