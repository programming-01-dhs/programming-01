############################################################
# Name : Ben Burke       Date:  10/17/24                   #
# Unit 5 Problems                                          #
# clock countdown, Divisible by 5 or 6,                    #
# display a pyramid, math game, Number Guessing Game       #
# random turtle                                            #
############################################################

import turtle
import time
import math 
import random

#problem 1

print("Problem 1 - Countdown:")
print()

userCountdown = int(input("Please enter a number that you would like to count down from = "))

for i in range(userCountdown,0 ,-1):
    time.sleep(1)
    print(i)

print()

#problem 2

print("Problem 2 - Divisible by 5 or 6:")
print()

count = 0
for number in range(100, 1001):
    if number % 5 == 0 or number % 6 == 0:
        if count < 9:
            print(number, end=" ")
            count = count + 1
        
        else:
            print(number)
            count = 0

print()

#problem 3

userNumber = 0

while userNumber < 1 or userNumber > 15:
    userNumber = eval(input("Give me a number to make a pyramid (1-15) = "))

    if userNumber < 1:
        userNumber = eval(input("Invalid input, try again (1-15) = "))
    
    if userNumber > 15:
        userNumber = eval(input("Invalid input, try again (1-15) = "))

#setting variables
spacer = "   "
spacer2 = " "

if userNumber > 9:
    spacer = "   "
    spacer2 = " "

spacer3 = ""

currentNum = 1

for row in range(1, userNumber + 1):
    if row == 1:
        print(spacer * (userNumber - currentNum), currentNum)
    
    elif row >= 1:
        print(spacer * (userNumber - currentNum), currentNum, end='')
        for i in range(1, currentNum):
            if (currentNum-i) < 9:
                print(spacer2, (currentNum-i), end="")

            else:
                print(spacer3, (currentNum - i), end="")
        
        for i in range(currentNum, 1, -1):
            if (currentNum - i + 2) < 9:
                print(spacer2, (currentNum - i) + 2, end='')
            
            else:
                print(spacer3, (currentNum - i) + 2, end='')
        
        print()

    currentNum += 1

print()

#problem 4


#setting variables
problemNum = 0
correctAnswers = 0
wrongAnswers = 0

print("Problem 4 - Math Game:")
print()

#user input
userAnswer = input("What type of problem would you like to have? (addition - A, subtraction - S, both - B) = ").upper()
print()

print("Your goal is to get 5 correct answers. If you get 3 wrong answers, you lose.")

#using a while loops until conditions are met
while correctAnswers < 5 and wrongAnswers < 3:

    randomInt1 = random.randint(0, 9)
    randomInt2 = random.randint(0, 9)
    randomSign = random.choice(["+", "-"])   #this random.choice is choosing between + and - for problems

    #using if statements to calculate+
    if userAnswer == "A":
        userResponse = eval(input(f"Problem {problemNum + 1}: {randomInt1} + {randomInt2} = "))

        if userResponse == randomInt1 + randomInt2:
            print("Correct!")
            print()
            correctAnswers += 1
            problemNum += 1

        else:
            print("Incorrect!")
            print()
            wrongAnswers += 1
            problemNum += 1

    if userAnswer == "S":
        userResponse = eval(input(f"Problem {problemNum + 1}: {randomInt1} - {randomInt2} = "))

        if userResponse == randomInt1 - randomInt2:
            print("Correct!")
            print()
            correctAnswers += 1
            problemNum += 1

        else:
            print("Incorrect!")
            print()
            wrongAnswers += 1
            problemNum += 1

    if userAnswer == "B":
        userResponse = eval(input(f"Problem {problemNum + 1}: {randomInt1} {randomSign} {randomInt2} = "))

        if userResponse == randomInt1 + randomInt2 or randomInt1 - randomInt2:
            print("Correct!")
            print()
            correctAnswers += 1
            problemNum += 1

        else:
            print("Incorrect!")
            print()
            wrongAnswers += 1
            problemNum += 1

    #seeing if the loop conditionals have been met
    if correctAnswers == 5:
        print("Congrats! You won the game!")
        print(f"You got {correctAnswers} correct answers and {wrongAnswers} wrong answers.")

    else:
        if wrongAnswers == 3:
          print("You lost the game.")
          print(f"You got {correctAnswers} correct answers and {wrongAnswers} wrong answers.")

print()

#problem 5

print("Problem 5 - Number Guessing Game:")
print()

#setting variables
guessAmount = 1
cpuGuess = 0
numberGuess = random.randint(1,100)
userRandom = eval(input("Please give me a number between 1 and 100 and I will guess it = "))
print()

#using while loop to check if user entered a valid number
while userRandom < 1 or userRandom > 100:


    if userRandom > 100:
        userRandom = eval(input("Invalid input, try again = "))

    if userRandom < 1:
        userRandom = eval(input("Invalid input, try again = "))

loop1 = True
loop2 = False

while loop1 == True:

    #setting variables inside the while loop
    numberLower1 = random.randint(1,25)
    numberHigher1 = random.randint(1,25)

    cpuGuess = input(f"Guess {guessAmount}: Is your number {numberGuess}? Give me a high, low, or correct. (H/L/C) = ").upper()


    if cpuGuess == "H":
        numberGuess = numberGuess - numberLower1
        guessAmount = guessAmount + 1

    if cpuGuess == "L":
        numberGuess = numberGuess + numberHigher1
        guessAmount = guessAmount + 1

    if cpuGuess == "C":
        print(f"Wow, your number was {numberGuess}. It took {guessAmount} trys to get the correct.")

        loop1 = False
        loop2 = False
    
    if guessAmount == 5:
        loop1 = False
        loop2 = True

while loop2 == True:

    #setting variables
    numberLower2 = random.randint(1,5)
    numberHigher2 = random.randint(1,5)

    cpuGuess = input(f"Guess {guessAmount}: Is your number {numberGuess}? Give me a high, low, or correct. (H/L/C) = ").upper()


    if cpuGuess == "H":
        numberGuess = numberGuess - numberLower2
        guessAmount = guessAmount + 1

    if cpuGuess == "L":
        numberGuess = numberGuess + numberHigher2
        guessAmount = guessAmount + 1

    if cpuGuess == "C":
        print(f"Wow, your number was {numberGuess}. It took {guessAmount} trys to get the correct.")

        loop2 = False



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

t.speed(0), t2.speed(0)
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

    if circleCount < 100:
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

    if triangleCountFill < 100:
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


    if triangleCountnoFill < 100:
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
        triangleCountnoFill += 1

    else:
        t.color(0, 0, 0), t2.color(0, 0, 0)
        t.penup()
        t.home()
        trinoFillLoop = False
        lineLoop = True
    
while lineLoop == True:

    lineX1 = random.randint(2, 300)
    lineY1 = random.randint(-300, -2)
    lineX2 = random.randint(2, 300)
    lineY2 = random.randint(-300, -2)

    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    if lineCount < 100:
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
        lineLoop = False

w.mainloop()
