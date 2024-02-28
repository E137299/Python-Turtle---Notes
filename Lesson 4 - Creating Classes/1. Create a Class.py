from turtle import *
import random


class Flower(Turtle):
    def __init__(self, x, y, screen, left_key, right_key):
        super().__init__()
        print("Flower")
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.x = x
        self.y = y
        self.goto(self.x,self.y)
        self.pencolor("purple")
        self.screen = screen
        self.screen.onkeypress(self.draw_one, left_key)
        self.screen.onkeypress(self.draw_two, right_key)
    
    def draw_one(self):
        red = 0.1
        green = 0.7
        blue = 0.7
        self.pendown()
        
        for j in range(50):
            red += 0.1
            self.begin_fill()
            self.fillcolor(red,green,blue)
            self.circle(50,90)
            self.right(33)
            self.end_fill()
            if red > 1.0:
                red = 0.0

    
    def draw_two(self):
        self.pendown()
        for i in range(36):
            self.begin_fill()
            self.fillcolor(random.uniform(0.5,1.0),random.uniform(0.5,1.0),random.uniform(0.5,1.0))
            for x in range(9):
                self.backward(45)
                self.left(38)
            self.end_fill()
            self.right(35)

display = Screen()
display.bgcolor("teal")
display.listen()
display.tracer(0)

flower = Flower(0,0,display,"Left","Right")

display.mainloop()