############################################################
# Name : Ben Burke      Date: 12/3/24                      #
# Unit 7 Problems                                          #
# Count Digits, Smallest index of list, List shuffle       # 
# Revise selection sort, bubble sort, merge sort           #
# Locker Problem, Turtle hangman                           #
############################################################

import turtle
import random


#problem 1
print("Problem 1 - Count of Digits")
print()

list1 = list()

for x in range(0,1000):
    list1.append(random.randint(0,9))

print(list1)
print()

print(f"There are {list1.count(0)} of the number 0")
print(f"There are {list1.count(1)} of the number 1")
print(f"There are {list1.count(2)} of the number 2")
print(f"There are {list1.count(3)} of the number 3")
print(f"There are {list1.count(4)} of the number 4")
print(f"There are {list1.count(5)} of the number 5")
print(f"There are {list1.count(6)} of the number 6")
print(f"There are {list1.count(7)} of the number 7")
print(f"There are {list1.count(8)} of the number 8")
print(f"There are {list1.count(9)} of the number 9")
print()

#problem 2
print("Problem 2 - Smallest Index")
print()

list2 = list()

def indexOfSmallestElement(lst):
    userNum1 = int(input("How many numbers do you want in a list? = "))

    for x in range(userNum1):
        lst.append(random.randint(0,100))
    
    print(lst)

indexOfSmallestElement(list2)

minimum = list2[0]

for number in list2:
    if number < minimum:
        minimum = number

index = list2.index (minimum)

print(f"The smallest number is {minimum}.")
print(f"at index {index}")
print()

#problem 3
print("Problem 3 - List Shuffle")
print()

list3 = list()

for x in range(10):
    list3.append(random.randint(0,100))

print(f"Original list = {list3}")

list3.sort()
print()

print(f"Sorted list = {list3}")
print()

def shuffle(lst):
    amount = 0

    for number in lst:
        amount += 1

    print(f"Shuffled Number = {random.sample(lst, amount)}")

shuffle(list3)
print()

#problem 4
print("Problem 4 - Revise Selection Sort")
print()


def selectionSortsm(lst):
  swaps = 0  #swaps counts how many times numbers were swapped to get the list in order
  for i in range(len(lst)):
    # Find the minimum in the lst[i : len(lst)]
    currentMin = lst[i]
    currentMinIndex = i
    
    #looks to see if there is a smaller number in the list and sets that to the smallest if it finds it
    for j in range(i + 1, len(lst)):
      if currentMin > lst[j]:
        currentMin = lst[j]
        currentMinIndex = j
    
    # Swap lst[i] with lst[currentMinIndex] if necessary
    if currentMinIndex != i:
      lst[currentMinIndex] = lst[i]
      lst[i] = currentMin
      swaps += 1
  print("Swaps", swaps)


"""Largest to Smallest"""

def selectionSortlg(lst):
  swaps = 0  #swaps counts how many times numbers were swapped to get the list in order
  for i in range(len(lst) -1, 0, -1):
    # Find the minimum in the lst[i : len(lst)]
    currentMin = lst[i]
    currentMinIndex = i
    #looks to see if there is a smaller number in the list and sets that to the smallest if it finds it
    for j in range(i -1, -1, -1):
      if currentMin < lst[j]:
        currentMin = lst[j]
        currentMinIndex = j
    # Swap lst[i] with lst[currentMinIndex] if necessary
    if currentMinIndex != i:
      lst[currentMinIndex] = lst[i]
      lst[i] = currentMin
      swaps += 1
  print("Swaps", swaps)

"create lists and sort with functions"

OrderList = []
for i in range(10):
    OrderList.append(random.randint(0,100))

OrderList2 = OrderList.copy()

selectionSortsm(OrderList)
print(OrderList)
print()

selectionSortlg(OrderList2)
print(OrderList2)
print()

#problem 5
print("Problem 5 - Bubble Sort")
print()

list5 = list()

for i in range(10):
    list5.append(random.randint(0,100))

print(f"Normal list = {list5}")
print()

def bubbleSort(lst):
    swap = 0
    boolean = True
    swapTF = False

    while boolean:
        swapTF = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i +1] = lst[i + 1], lst[i]
                swapTF = True
                swap += 1
        
        if swapTF == False:
            boolean = False 


            
    print(f"Bubble Sorted List = {lst}")
    print(f"Amount of Swaps = {swap}")

bubbleSort(list5)
print()


#problem 6
print("Problem 6 - Merge List")
print()

listM1 = list()
listM2 = list()

def merge(lst1, lst2):

    for x in range(5):
        lst1.append(random.randint(1, 100))
        lst2.append(random.randint(1, 100))
    
    print(f"Unsorted Lists = {lst1} {lst2}")
    print()

    lst1.sort(), lst2.sort()

    print(f"Sorted Lists = {lst1} {lst2}")
    print()

    listM3 = list()

    while lst1 and lst2:

        if lst1[0] < lst2[0]:
            listM3.append(lst1.pop(0))

        else:
            listM3.append(lst2.pop(0))
    
    listM3.extend(lst1)
    listM3.extend(lst2)

    print(f"Merged Sorted List = {listM3}")

    return listM3

merge(listM1, listM2)
print()

#problem 7
print("Problem 7 - Locker Problem")
print()

falseList = [False for x in range(101)]

for i in range(1, 101):

    for s in range(i, 101, i):
        if falseList[s]:
            falseList[s] = False
        
        else:
            falseList[s] = True


for x in range(101):
    if falseList[x]:
        print(f"Locker {x} is open")
print()

#problem 8
print("Problem 8 - Turtle Hangman")
