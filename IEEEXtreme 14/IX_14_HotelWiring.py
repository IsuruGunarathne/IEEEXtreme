############################## SUCCESS ##############################

from heapq import heapify, heappush, heappop

tests = int(input())
MaxRoomArr = []

for i in range(tests):
    m,n,k = map(int,input().split())
    # m = number of floors
    # n = number of rooms per floor
    # k = number of master switches turned off
    RoomsInFloor = []
    heapify(RoomsInFloor)
    for j in range(m):
        numCorrect = int(input())
        heappush(RoomsInFloor,numCorrect)
    
    # now Rooms has the number of correctly wired rooms in each floor sorted in acsending order
    # i.e. first ones have least number of rooms correctly wired
    # i.e. they need masters to be turned off
    
    
    # print(RoomsInFloor)
    
    maxRooms=0
    for i in range(m):
        if k>0 : # we can still turn off more masters
            maxRooms += n-heappop(RoomsInFloor) # the number of rooms that are wrongly wired
            k -= 1
        else:
            maxRooms += heappop(RoomsInFloor) # the number of rooms that are correctly wired
    MaxRoomArr.append(maxRooms)
    
for n in MaxRoomArr:
    print(n)