import turtle
import random

#problem 6

print("Problem 6 - Random Turtle")

#setting variables
w = turtle.Screen()
t = turtle.Turtle()
t2 = turtle.Turtle()
circleCount = 0
triangleCountFill = 0
triangleCountnoFill = 0
lineCount = 0
turtle.colormode(255)

R = 0
G = 0
B = 0
R2 = 0
G2 = 0
B2 = 0
R3 = 0
G3 = 0
B3 = 0


circleLoop = True
triFillLoop = False
trinoFillLoop = False
lineLoop = False

t.speed(50), t2.speed(50)
t.home()
t.goto(300,0)
t.goto(-300,0)
t.home()
t.goto(0,300)
t.goto(0,-300)


while circleLoop == True:

    circleX = random.randint(-300, -12)
    circleY = random.randint(5, 290)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    if circleCount < 0:
        t.pensize(1.3)
        t.penup()
        t.goto(circleX,  circleY)
        t.color(R, G, B)
        t.pendown()
        t.circle(10)
        circleCount += 1
    
    else:
        t.color(0, 0, 0)
        t.penup()
        t.home()
        circleLoop = False
        triFillLoop = True

while triFillLoop == True:

    triFillX = random.randint(-250, -10)
    triFillY = random.randint(-250, -10)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    if triangleCountFill < 10:
        t.penup(), t2.penup()
        t.home(), t2.home()
        t.goto(triFillX, triFillY), t2.goto(t.pos())
        t.fillcolor(R, G, B), t2.fillcolor(R, G, B)
        t.color(R, G, B), t2.color(R, G, B)
        t.begin_fill(), t2.begin_fill()
        t.pendown(), t2.pendown()
        t.lt(180)
        t.fd(48)
        t.lt(90)
        t.fd(36)
        t2.goto(t.pos())
        t.end_fill(), t2.end_fill()
        t.penup(), t2.penup()
        triangleCountFill += 1

    else:
        t.color(0, 0, 0), t2.color(0, 0, 0)
        t.penup()
        t.home(), t2.home()
        t2.hideturtle()
        triFillLoop = False
        trinoFillLoop = True

while trinoFillLoop == True:    

    trinoFillX = random.randint(5, 250)
    trinoFillY = random.randint(5, 260)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    R2 = random.randint(0, 255)
    G2 = random.randint(0, 255)
    B2 = random.randint(0, 255)
    R3 = random.randint(0, 255)
    G3 = random.randint(0, 255)
    B3 = random.randint(0, 255)


    if triangleCountnoFill < 10:
        t.penup()
        t.goto(trinoFillX, trinoFillY)
        t.color(R, G, B)
        t.pendown()
        t.lt(90)
        t.fd(60)
        t.color(R2, G2, B2)
        t.rt(120)
        t.fd(60)
        t.color(R3, G3, B3)
        t.rt(120)
        t.fd(60)
        t.penup()
        t.color(0, 0, 0)
        t.home()
        triangleCountnoFill = triangleCountnoFill + 1
    
    else:
        t.color(0, 0, 0), t2.color(0, 0, 0)
        t.penup()
        t.home()
        triangleCountnoFill = False
        lineCount = True
    
while lineCount == True:

        lineX1 = random.randint(2, 300)
        lineY1 = random.randint(-300, -2)
        lineX2 = random.randint(2, 300)
        lineY2 = random.randint(-300, -2)

        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)

        if lineCount < 100:
            t.penup()
            t.home()
            t.goto(lineX1, lineY1)
            t.color(R, G, B)
            t.pendown()
            t.goto(lineX2, lineY2)
            t.penup()
            t.home()
            lineCount += 1
        
        else:
            t.color(0, 0, 0), t2.color(0, 0, 0)
            t.penup()
            t.home()
            lineCount = false

        w.mainloop()
        
