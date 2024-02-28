from turtle import *

window = Screen()
window.setup(800,300)
window.bgcolor("black")
window.title("Write Your Name")


# A
a = Turtle()
a.shape("turtle")
a.speed(0)
a.color("red")
a.pensize(5)
a.penup()
a.goto(-225,-50)
a.pendown()
a.setheading(90)
a.forward(75)
a.circle(-25,180)
a.forward(75)
a.backward(50)
a.right(90)
a.forward(50)
a.penup()
a.goto(-150,50)

# U
a.pendown()
a.color("orange")
a.setheading(-90)
a.forward(75)
a.circle(25,180)
a.forward(75)
a.penup()
a.goto(-75,-25)

# S
a.pendown()
a.color("yellow")
a.setheading(-90)
a.circle(25,270)
a.circle(-25,270)
a.penup()
a.goto(0,50)

# T
a.pendown()
a.color("green")
a.setheading(0)
a.forward(50)
a.backward(25)
a.right(90)
a.forward(100)
a.penup()
a.goto(75,-50)

# I
a.pendown()
a.color("blue")
a.setheading(0)
a.forward(50)
a.backward(25)
a.left(90)
a.forward(100)
a.left(90)
a.forward(25)
a.backward(50)
a.penup()
a.goto(150,-50)

# N
a.pendown()
a.color("violet")
a.setheading(90)
a.forward(100)
a.goto(200,-50)
a.forward(100)

window.mainloop()