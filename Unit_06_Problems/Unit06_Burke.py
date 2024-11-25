############################################################
# Name : Ben      Date: 11/12/24                           #
# Unit 6 Problems                                          #
# Sum of Digits, sort 3 numbers, Display Characters        #
# Palindrome Number, Palindromic Prime, Emirp              #
# Turtle Draw Shapes                                       #
############################################################

import random

#problem 1

sumInput = eval(input("Give me a number of any length and it will return the sum of the digits = "))
print()

def sumdigits(numb):
    sum = 0
    for digit in str(sumInput):
        sum += int(digit)
    
    print(f"Your Number is {sum}.")

sumdigits(sumInput)
print()

# #problem 2

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

# #problem 3

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

def reverseInt(inp):              
    newNum = str()                
    for digit in str(inp):
        newNum = digit + newNum
    return int(newNum)      

def isPalindrome(inp):
    return int(inp) == reverseInt(inp)  #

userNum = int(input("Enter a number: "))
print()

print(isPalindrome(userNum))

#problem 5

userNum2 = int(input("How many palindrome primes do you want to see = "))

def isPrime(num):
    if num > 1:                             
        for i in range(2, (num//2)+1):      
            if (num % i) == 0:               
                break                      
        else:                             
            return True                    
                                            
def palindromicPrime(NumOfPrimes):
    primeCount = 0    
    lineCount = 0     
    currentNumber = 2 

    while primeCount < NumOfPrimes:                  
        if isPrime(currentNumber):                   
            if isPalindrome(currentNumber):           
                print(f'{currentNumber:5d}', end=' ') 
                primeCount += 1                        
                lineCount += 1                       
                if lineCount == 10:                   
                    print()                         
                    lineCount = 0                   
        currentNumber += 1  
    print("Done")
    
palindromicPrime(userNum2)
print()

#problem 6

primeCount1 = 0
currentNum1 = 2
currentNum2 = str(currentNum1)[::-1]
lineCount1 = 0

userNum3 = 100


while primeCount1 < userNum3:

    if isPrime(currentNum1):
        if isPrime(reverseInt(currentNum1)):
            if not isPalindrome(currentNum1):

                print(f'{currentNum1:5d}', end=' ')
                primeCount1 += 1
                lineCount1 += 1

                if lineCount1 == 10:
                    print()
                    lineCount1 = 0
    
    currentNum1 += 1
print("Done")

