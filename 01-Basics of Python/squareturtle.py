import turtle
t = turtle.Turtle()
bg = turtle.Screen()
bg.bgcolor("Aqua")
t.speed(1)
t.begin_fill()
t.color("white")
t.fillcolor("red")
for i in range(4):
    t.fd(100)
    t.lt(90)
t.end_fill()
t.hideturtle() 
