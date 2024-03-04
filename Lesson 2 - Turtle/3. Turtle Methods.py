from turtle import *

display = Screen()
display.bgcolor("teal")



'''
Movement using forward(), left(), right()
'''
# Instantiating a Turtle
first = Turtle()
first.shape("square")
first.color("red")

# Move turtle
for side in range(4):
    for steps in range(5):
        first.pendown()
        first.forward(10)
        first.penup()
        first.forward(10)
    first.right(90)
first.hideturtle()

'''
Movement by assigning position to turtle .goto(x,y) or setposition(x,y)
'''
# Instantiate Turtle object
second = Turtle()
second.shape("circle")
second.color("yellow")
second.hideturtle()
# Move turtle object
second.penup()
second.goto(150,150)
second.pendown()
second.pensize(10)
second.goto(150,-150)
second.goto(-150,-150)
second.goto(-150,150)
second.goto(150,150)
second.showturtle()

display.mainloop()

