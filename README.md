# Python Turtle - Notes

## Screen Class
### Attributes:
* dimensions (width, height)
* color
* image
* title
* refresh rate

### Method: 
[Link to All Methods](https://docs.python.org/3/library/turtle.html#methods-of-turtlescreen-screen)
* Setters
    * [setup(width, height)](https://docs.python.org/3/library/turtle.html#turtle.setup) - sets dimensions
    * [bgcolor(color)](https://docs.python.org/3/library/turtle.html#turtle.bgcolor) - sets color
    * [bgpic(picture)](https://docs.python.org/3/library/turtle.html#turtle.bgpic) - sets background
    * [title(title)](https://docs.python.org/3/library/turtle.html#turtle.title) - sets title
    * [tracer(n)](https://docs.python.org/3/library/turtle.html#turtle.tracer)- sets refresh rate
* Others:
    * [listen()](https://docs.python.org/3/library/turtle.html#turtle.listen) - Makes the screen listen for events. This method allows the program to respond to keyboard or mouse input.
    * [onkey(function, key)](https://docs.python.org/3/library/turtle.html#turtle.onkey) - Binds the specified function fun to the given key. When the key is pressed, the function is executed.
    * [onscreenclick(function)](https://docs.python.org/3/library/turtle.html#turtle.onclick) - Binds the specified function fun to mouse clicks on the screen. 
    * [update()](https://docs.python.org/3/library/turtle.html#turtle.update) - Updates the screen's appearance. This method is useful for animations to display changes made since the last update.
 



## Coordinate Plane
![Coordinate Plane](images/coordinate%20plane.webp)
![Headings](images/Turtle%20Degrees.webp)
## Turtle Class
### Attributes:
* color 
* pen color
* shape
* position (x,y)
* speed
* heading
* pen up / pen down
* pen size
* visibility (hidden or showing)

### Methods:
[Link to all Turtle methods](https://docs.python.org/3/library/turtle.html#methods-of-rawturtle-turtle-and-corresponding-functions)
* Setters
    * [setx(x)](https://docs.python.org/3/library/turtle.html#turtle.setx) - Sets the x-coordinate of the turtle to the specified value.
    * [sety(y)](https://docs.python.org/3/library/turtle.html#turtle.sety) - Sets the y-coordinate of the turtle to the specified value.
    * [setposition(x, y)](https://docs.python.org/3/library/turtle.html#turtle.goto) - Sets the position of the turtle to the specified (x, y) coordinates.
    * [setheading(angle)](https://docs.python.org/3/library/turtle.html#turtle.setheading) - Sets the orientation of the turtle (heading) to the specified angle in degrees.
    * [speed(speed)](https://docs.python.org/3/library/turtle.html#turtle.speed) - Sets the speed of the turtle's movement. The speed parameter can be an integer from 0 to 10, with 0 being the fastest and 10 being the slowest.

    * [pensize(width)](https://docs.python.org/3/library/turtle.html#turtle.pensize) - Sets the width of the turtle's pen (drawing tool) to the specified width.
    * [penup()](https://docs.python.org/3/library/turtle.html#turtle.penup) - Lifts the turtle's pen off the screen, so it no longer draws when moving.
    * [pendown()](https://docs.python.org/3/library/turtle.html#turtle.pendown) - Lowers the turtle's pen onto the screen, so it draws when moving.
    * [pencolor(color)](https://docs.python.org/3/library/turtle.html#turtle.pencolor) - Sets the color of the turtle's pen to the specified color.

* Setters
    * [xcor()](https://docs.python.org/3/library/turtle.html#turtle.xcor) - Returns the current x-coordinate of the turtle.
    * [ycor()](https://docs.python.org/3/library/turtle.html#turtle.ycor) - Returns the current y-coordinate of the turtle.
    * [position()](https://docs.python.org/3/library/turtle.html#turtle.position) - Returns a tuple containing the current (x, y) coordinates of the turtle.
    * [heading()](https://docs.python.org/3/library/turtle.html#turtle.heading) - Returns the current orientation of the turtle (heading) in degrees.
    * [distance(x,y)](https://docs.python.org/3/library/turtle.html#turtle.distance) - Returns the distance between the turtle's current position and the specified point.

* Others
    * [forward(distance)](https://docs.python.org/3/library/turtle.html#turtle.forward) - Moves the turtle forward by the specified distance.
    * [backward(distance)](https://docs.python.org/3/library/turtle.html#turtle.backward) - Moves the turtle backward by the specified distance.
    * [left(angle)](https://docs.python.org/3/library/turtle.html#turtle.left) - Turns the turtle counterclockwise (left) by the specified angle in degrees.
    * [right(angle)](https://docs.python.org/3/library/turtle.html#turtle.right) - Turns the turtle clockwise (right) by the specified angle in degrees.
    * [goto(x, y)](https://docs.python.org/3/library/turtle.html#turtle.goto) - Moves the turtle to the specified position (x, y) on the screen without drawing.
    * [circle(radius, extent=None)](https://docs.python.org/3/library/turtle.html#turtle.circle) - Draws a circle with the specified radius. If the extent is provided, it draws only a part of the circle (specified in degrees).
    * [stamp()](https://docs.python.org/3/library/turtle.html#turtle.stamp) - Stamps an impression of the turtle shape onto the screen at the current turtle position.
    * [clear()](https://docs.python.org/3/library/turtle.html#turtle.clear) - Clears the turtle's drawing on the screen, resetting it to its initial state.