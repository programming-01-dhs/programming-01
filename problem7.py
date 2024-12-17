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
