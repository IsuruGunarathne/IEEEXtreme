########################### SUCCESS ###############################

import sys

n = int(input())
test = [0 for i in range(n)]

def printGuess(guess):
    print("Q", end=" ")
    for i in range(n):
        print(guess[i],end=" ")
    print()
    sys.stdout.flush()

def printAnswer(answer):
    print("A", end=" ")
    for i in range(n):
        print(answer[i],end=" ")
    print()

nZeros = n

printGuess(test)
correct = int(input())
prevCorr =correct

if (correct == n):
    printAnswer(test)
    exit()

for i in range(n):
    test[i] = 1
    printGuess(test)
    correct = int(input())
    if correct == n:
        break
    elif correct>prevCorr:
        # that means the change we did is correct
        prevCorr = correct
    else:
        # the change we did is wrong, undo it
        test[i] = 0

printAnswer(test)
    