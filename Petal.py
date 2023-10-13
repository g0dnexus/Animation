import turtle

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

screen = turtle.Screen()
screen.bgcolor('black')

t = turtle.Turtle()
t.speed(0)
t.width(3)

for i in range(500):
    t.pencolor(colors[i % len(colors)])
    t.forward(i)
    t.right(59)

turtle.done()
