from turtle import *

def turn_right(t):
    t.right(10)

def turn_left(t):
    t.left(10)

def drop_shadow(t):
    t.stamp()




display = Screen()
display.bgcolor("teal")
display.listen()
display.onkeypress(lambda: turn_right(first),"Right")
display.onkeypress(lambda: turn_left(first),"Left")
display.onkey(lambda: drop_shadow(first),"space")

first = Turtle()
first.shape("turtle")

while True:
    first.pendown()
    first.forward(2)
    first.penup()
    first.forward(2)


display.mainloop()