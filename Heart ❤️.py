import math
import turtle

def xt(t):
    return 16 * math.sin(t) ** 3

def yt(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

def draw_heart():
    t.penup()
    t.goto(xt(0) * 200, yt(0) * 200)
    t.pendown()
    t.color('#FF428A', '#FF82C6')  
    t.width(3) 
    t.begin_fill()
    for i in range(2550):
        t.goto(xt(i) * 20, yt(i) * 20)
    t.goto(xt(0) * 20, yt(0) * 20)  
    t.end_fill()


t = turtle.Turtle()
t.speed(1000)
t.hideturtle()


turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)

draw_heart()
write_text()


turtle.update()
turtle.mainloop()
