'''
The following code demonstrates how methods belonging to the Screen class 
can be used to customize the display window.
'''

# Provides the program access to all the classes and functions with in the Turtle library
from turtle import *

# Creates a Screen object
display = Screen()
display.title("Customized Window") #.title(title) places a title at the top of the window
display.bgcolor("teal") #.bgcolor(color) set the color of the display
display.setup(1200, 600) #.setup(width, height) defines the dimensions of the window. 
display.tracer(0) #.tracer(n) Controls the animation speed. n specifies the number of turtle moves before the screen updates. Passing n=0 will update the screen after each turtle move.




# mainloop() keeps the screen open until it is manually closed
display.mainloop()