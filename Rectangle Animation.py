import turtle

screen = turtle.Screen()
screen.bgcolor('black')


t = turtle.Turtle()
t.shape('square')
t.color('white')

width = 200
height = 100
speed = 0.1

text = turtle.Turtle()
text.color('white')
text.penup()
text.goto(0, 0)
text.hideturtle()

def change_size(new_width, new_height):
    global width, height
    width = new_width
    height = new_height

def change_speed(new_speed):
    global speed
    speed = new_speed

def change_color(new_color):
    t.color(new_color)

def show_text(message):
    text.clear()
    text.write(message, align='center', font=('Arial', 12, 'normal'))

while True:
    t.goto(-width / 2, -height / 2)
    t.shapesize(height / 20, width / 20)
    t.goto(width / 2, -height / 2)
    t.goto(width / 2, height / 2)
    t.goto(-width / 2, height / 2)
    t.goto(-width / 2, -height / 2)
    
    turtle.update()
    turtle.delay(speed)

turtle.done()
