from turtle import *

display = Screen()

# Instantiating a Turtle
first = Turtle()

'''
SETTING A TURTLE'S ATTRIBUTES
'''
# Shape - turtle.shape(shape) sets the turtle's shape. Options: turtle, circle, square, triangle, arrow
first.shape("turtle") 

# Color - turtle.color(color) sets turtle's color. color() can take in a string value or three float values
first.color("teal") 
# first.color(0.0,1.0,0.0)

# Speed - turtle.speed() sets the turtle's speed. Range from 1 to 10; however, 0 is fastest
first.speed(0)

# Pen Up

display.mainloop()