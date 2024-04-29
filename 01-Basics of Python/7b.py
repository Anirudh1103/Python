import turtle
import time
def draw_poly(sides):

 try:
    win = turtle.Screen() # Creates a window
    win.bgcolor("lightgreen")
    tess = turtle.Turtle() # Creates a turtle
    if sides<0:
        raise ValueError # Raises ValueError if number of sides is negative
    else:
        angle = 360 / sides
        for i in range(sides): # Draws a polygon with given number of sides
            tess.forward(50)
            tess.left(angle)
            time.sleep(1)
 except ValueError:
    print("Sorry, number of sides cannot be negative")
 except ZeroDivisionError:
    print("Sorry, number of sides cannot be zero, it leads to zero division error")
 finally:
     win.mainloop() # Waits till the user closes the window
n=int(input("Enter the number of sides to draw a polygon:"))
draw_poly(n)