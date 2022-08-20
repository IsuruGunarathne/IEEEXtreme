########################### SUCCESS ###############################

from heapq import heapify, heappush, heappop

n,m = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

heapify(B)

# print(A,B)

result = []

Aptr = 0
while len(B)>0:
    # adding elements from B and A to results

    if A[Aptr]<B[0]:
        result.append(A[Aptr])
        Aptr+=1 #added from A, can move to next item in A
    else:
        result.append(B[0])
        heappop(B)
        # still pointing to same item in A
    if Aptr>=len(A):
        # add remaining stuff from B
        for i in range(len(B)):
            result.append(heappop(B))

# adding remaining elements in A
while Aptr<n:
    result.append(A[Aptr])
    Aptr+=1

for i in result:
    print(i,end=' ')