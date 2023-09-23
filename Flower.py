import turtle as tur
import colorsys as cs

tur.setup(800, 800)
tur.speed(0)
tur.tracer(10)
tur.width(5)
tur.bgcolor("black")

for j in range(50):
    for i in range(15):
        hsv_color = cs.hsv_to_rgb((i / 15 + j / 50) % 1, 1, 1)
        tur.color(hsv_color)
        
        tur.right(90)
        tur.circle(300 - j * 6, 90)
        tur.left(90)
        tur.circle(300 - j * 6, 90)
        tur.right(180)
        tur.circle(100, 24)

tur.hideturtle()
tur.done()
