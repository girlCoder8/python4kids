### Project 3: Drawing Shapes
# Code

````
import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")
    alex = turtle.Turtle()
    alex.color("blue")
    for _ in range(4):
        alex.forward(100)
        alex.right(90)
    window.mainloop()

draw_square()
