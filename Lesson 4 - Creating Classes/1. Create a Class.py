from turtle import *

class Player(Turtle):
    def __init__(self, x, y, color, screen, left_key, right_key):
        super().__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.goto(x,y)
        self.color(color)
        self.shape("turtle")
        self.showturtle()
        self.health = 5
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)

    def turn_right(self):
        print("right")
        self.right(10)

    def turn_left(self):
        self.left(10)

    def sick(self, screen):
        screen.bgcolor("red")
        self.color("green")

display = Screen()
display.bgcolor("teal")

player = Player(100, 100, "yellow", display, "Left", "Right")

while True:
    player.forward(2)

display.mainloop()