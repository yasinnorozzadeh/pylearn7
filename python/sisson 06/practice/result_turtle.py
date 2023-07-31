import turtle
turtle.bgcolor("red")
s = turtle.Pen()

t = 3
z = int(360 / t)
y = 50
s.shape("turtle")
s.shapesize(0.5)
s.pencolor("white")
for i in range(6):
    s.right(10)
    s.setx((t * i)*(3))
    s.sety((t * i)*(-3))
    for j in range(t):
        s.pendown()
        s.left(z)
        s.forward(y)
        z = int(360 / t)
    s.penup()
    y+=30
    t = t + 1
    s.setx((t * i)*(3))
    s.sety((t * i)*(-j))
s.done()