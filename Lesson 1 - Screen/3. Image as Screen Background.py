# Provides the program access to all the classes and functions with in the Turtle library
from turtle import *

# Creates a Screen object
display = Screen()
display.bgpic("images/landscape.gif") #.bgpic(file_path) sets the window's background to an image. Must be a GIF
display.setup(540,320) #.setup(width, height) to fit window's to dimensions to match image's image dimensions

# mainloop() keeps the screen open until it is manually closed
display.mainloop()