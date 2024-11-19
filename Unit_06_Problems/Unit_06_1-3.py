############################################################
# Name : Ben      Date: 11/12/24                           #
# Unit 6 Problems                                          #
# Sum of Digits, sort 3 numbers, Display Characters        #
# Palindrome Number, Palindromic Prime, Emirp              #
# Turtle Draw Shapes                                       #
############################################################

import random

sumInput = eval(input("Give me a number of any length and it will return the sum of the digits = "))
print()

def sumdigits(numb):
    sum = 0
    for digit in str(sumInput):
        sum += int(digit)
    
    print(f"Your Number is {sum}.")

sumdigits(sumInput)
print()

#problem 2

num1, num2, num3 = eval(input("Write me 3 different numbers that are seperated by commas (ex: 1,2,3) = "))
print()

def displaySortedNumbers(num1, num2, num3):

    if num1 < num2 < num3:
        print(num1, num2, num3)

    if num1 < num3 < num2:
        print(num1, num3, num2)

    if num2 < num1 < num3:
        print(num2, num1, num3)

    if num3 < num2 < num1:
        print(num3, num2, num1)

    if num3 < num1 < num2:
        print(num3, num1, num2)

displaySortedNumbers(num1, num2, num3)
print()

#problem 3

ch1, ch2 = input("Give me 2 letters seperated by a comma (ex: a,b) = ").lower().split(",")
numPerLine = eval(input("How many letters would you like to be displayed on each line? = "))

def printChars(ch1, ch2, numPerLine):
    counter = 0

    for letter in range(ord(ch1), ord(ch2) + 1):
        print(chr(letter), end = "")
        counter += 1

        if counter >= int(numPerLine):
            print()
            counter = 0 

printChars(ch1, ch2, numPerLine)

#problem 4

def isPalindrome(inp):
    pass



def reverseInt(inp):
    pass
