from turtle import *

def draw_boundary():
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    t.pencolor("yellow")
    t.penup()
    t.goto(-300,300)
    t.pensize(10)
    t.pendown()
    for side in range(4):
        t.forward(600)
        t.right(90)

class Player(Turtle):
    def __init__(self, x, y, shape, screen, left_key, right_key):
        super().__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.goto(x,y)
        self.colors = [(0.0,.7,0.0), (0.0,.8,0.0), (0.0,.9,0.0),(0.0,1.0,0.0)]
        self.sick_index = 0
        self.color(self.colors[self.sick_index])
        self.shape(shape)
        self.showturtle()
        self.screen = screen
        self.screen.onkeypress(self.turn_left, left_key)
        self.screen.onkeypress(self.turn_right, right_key)
    
    def move(self):
        if self.xcor()>290 or self.xcor()<-290:
            self.sick_index += 1
            self.get_sicker()
            self.setheading(180-self.heading())
        if self.ycor()>290 or self.ycor()<-290:
            self.sick_index += 1
            self.get_sicker()
            self.color(self.colors[self.sick_index])
            self.setheading(-1*self.heading())
        self.forward(2)

    def turn_right(self):
        self.right(10)

    def turn_left(self):
        self.left(10)

    def get_sicker(self):
        self.color(self.colors[self.sick_index])

    def die(self, screen):
        self.get_sicker()
        self.sick_index=0

display = Screen()
display.title("Fade to Green")
display.bgcolor((0.0,1.0,0.0))
display.listen()

draw_boundary()

one = Player(-100,0, "circle", display, "a","b")
two = Player(100, 0, "square", display, "Left", "Right")


while True:
    one.move()
    two.move()
    if one.distance(two)<20:
        one.sick_index += 1
        two.sick_index += 1
    if one.sick_index == 3:
        one.die(display)
    if two.sick_index == 3:
        two.die(display)

display.mainloop()