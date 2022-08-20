##################### SUCCESS #####################

from operator import itemgetter


n = int(input())
prisoners = [["test",0] for x in range(n)]

for i in range(n):
    temp =   list(map(str,input().split()))
    prisoners[i][0] = temp[0] #string name
    prisoners[i][1] = int(temp[1])

# got input, prisoners to list of lists
# [name,height]

def sortByHeight(prisoners):
    newPrisoners = sorted(prisoners, key=itemgetter(1))
    return newPrisoners

prisoners = sortByHeight(prisoners)

# we now have people sorted by height
# loop throught it and get people with same heights in a list

# for prisoner in prisoners:
#     print(prisoner)

prisoners.append(["test",0]) # to make the loop run once more
currentHeight = prisoners[0][1]
currNames = []
count = 1
for prisoner in prisoners:
    if prisoner[1] == currentHeight:
        currNames.append(prisoner[0])

    else:

        currNames = sorted(currNames)
        for name in currNames:
            print(name,end=" ")
        print(count,count+len(currNames)-1)
        count += len(currNames)
        currNames = []
        currentHeight = prisoner[1]
        currNames.append(prisoner[0])



