#Program to draw multi color square
import turtle
def square(animal,size):
    for i in ['red','pink','purple','blue']:
        animal.color(i)
        animal.fd(size)
        animal.left(90)
    
wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor('light green')
t.pensize(3)
size = 20

for _ in range(15):
    square(t,size)
    size += 10
    t.fd(10)
    t.right(18)