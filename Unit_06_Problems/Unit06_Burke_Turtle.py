import turtle

w = turtle.Screen()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()


#problem 7

def drawRectangle(color="black", x=0, y=0, width=30, height=30, angle=0):
    t1.goto(x, y)
    t1.pendown()
    t1.color(color)
    t1.fillcolor(color)
    t1.begin_fill()
    t1.rt(angle)
    t1.fd(width)
    t1.lt(angle)
    t1.fd(height)
    t1.lt(angle)
    t1.fd(width)
    t1.lt(angle)
    t1.fd(height)
    t1.end_fill()
    t1.penup()
    t1.home()

def drawPolygon(color="black", x=0, y=0, numsides=4, length=30):
    pass

def drawCircle(color="black", x=0, y=0, radius=50):
    pass
