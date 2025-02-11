
### **Table: Key Event Methods in `turtle.Screen()`**
| Method | Description | Example |
|---------|------------|---------|
| `listen()` | Sets the window to listen for keyboard input. | `screen.listen()` |
| `onkey(function, key)` | Binds a function to a key press (when a key is pressed). | `screen.onkey(move_forward, "Up")` |
| `onkeypress(function, key)` | Similar to `onkey()`, but only works if the key is **held down**. | `screen.onkeypress(move_forward, "w")` |
| `onkeyrelease(function, key)` | Triggers a function when the key is released. | `screen.onkeyrelease(stop_moving, "space")` |
| `onscreenclick(function, btn=1, add=None)` | Binds a function to mouse clicks. The `btn` value specifies **left (1), middle (2), or right (3) button clicks**. | `screen.onscreenclick(draw_circle, 1)` |
| `ontimer(function, t)` | Calls a function after `t` milliseconds. | `screen.ontimer(update_position, 500)` |
| `mainloop()` or `done()` | Keeps the window open, listening for events. | `turtle.mainloop()` |

---

### **Example: Key Binding in Turtle**
```python
import turtle

# Create screen and turtle
screen = turtle.Screen()
screen.title("Turtle Key Binding Example")
t = turtle.Turtle()

# Define movement functions
def move_forward():
    t.forward(20)

def move_backward():
    t.backward(20)

def turn_left():
    t.left(30)

def turn_right():
    t.right(30)

def clear_screen():
    t.clear()

def exit_program():
    screen.bye()

# Set up key bindings
screen.listen()
screen.onkey(move_forward, "Up")       # Arrow Up moves forward
screen.onkey(move_backward, "Down")     # Arrow Down moves backward
screen.onkey(turn_left, "Left")         # Arrow Left turns left
screen.onkey(turn_right, "Right")       # Arrow Right turns right
screen.onkey(clear_screen, "c")         # Press 'c' to clear screen
screen.onkey(exit_program, "q")         # Press 'q' to quit program

# Keep window open
screen.mainloop()
```

### **How It Works:**
- `listen()` ensures the screen captures keyboard events.
- `onkey()` binds specific keys to movement functions.
- `Up`, `Down`, `Left`, and `Right` keys move the turtle.
- Pressing `"c"` clears the drawing.
- Pressing `"q"` exits the program.

