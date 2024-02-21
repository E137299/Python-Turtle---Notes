from turtle import *
from random import randint, uniform, choice

display = Screen()
display.bgcolor("black")

'''
SETTING A TURTLE'S ATTRIBUTES
'''
# Instantiating a Turtle
first = Turtle()

# Shape - turtle.shape(shape) sets the turtle's shape. Options: turtle, circle, square, triangle, arrow
first.shape("turtle") 

# Color - turtle.color(color) sets turtle's color. color() can take in a string value or three float values
first.color("teal") 
# first.color(0.0,1.0,0.0)

# Speed - turtle.speed() sets the turtle's speed. Range from 1 to 10; however, 0 is fastest
first.speed(0)

# Pen Up
first.penup()

# Set heading
first.setheading(45)



'''
CHECK A TURTLE'S ATTRIBUTES
'''
second = Turtle()
second.color(uniform(0.5,1.0), uniform(0.5,1.0), uniform(0.5,1.0))
second.shape(choice(["circle","square","triangle","turtle","arrow"]))
second.setheading(randint(0,360))
second.pencolor(uniform(0.5,1.0), uniform(0.5,1.0), uniform(0.5,1.0))
second.setposition(randint(-150,150),randint(-150,150))

print("The second turtle's color is "+str(second.color()[1]))
print("The second turtle's pen color is "+str(second.pencolor()))
print("The second turtle's shape is "+second.shape())
print("The second turtle's heading is "+str(second.heading()))
print("The second turtle's position is "+str(second.position()))



display.mainloop()

