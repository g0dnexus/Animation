import turtle

window = turtle.Screen()
window.bgcolor('black')
window.setup(width=1000, height=800)

pen = turtle.Turtle()
pen.shape('triangle') 
pen.color('white')
pen.speed(1000)

for i in range(1, 601):
    pen.forward(i * 2)
    pen.right(91)
    pen.right(1)

turtle.done()
