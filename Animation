import turtle

screen = turtle.Screen()
screen.bgcolor('black')

cube = turtle.Turtle()
cube.speed(0)
cube.hideturtle()

cube.width(3)
cube.penup()
cube.goto(0, 0)
cube.pendown()

def draw_cube(size):
    for _ in range(4):
        cube.forward(size)
        cube.right(90)
    cube.right(45)
    cube.forward(size)
    cube.right(135)
    cube.forward(size)
    cube.right(45)
    cube.forward(size)

size = 10
angle = 0
color_index = 0
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
while True:
    cube.pensize(size // 30)
    cube.color(colors[color_index])

    draw_cube(size)

    size += 5

    cube.right(angle)
    angle += 1

    color_index += 1
    if color_index >= len(colors):
        color_index = 0

    cube.clear()

turtle.done()
