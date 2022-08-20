##################### SUCCESS #####################

n,cb,cp = map(int,input().split())

nBlack = 0
nPink = 0

for i in range(n):
    temp = list(map(int,input().split()))
    nBlack += temp[0]
    nPink += temp[1]

# now we have total pink and black tiles needed


nb = 0 #number of black sets
np = 0 #number of pink sets
if (nBlack%10 == 0):
    nb = nBlack//10
else:
    nb = nBlack//10 + 1

if (nPink%10 == 0):
    np = nPink//10
else:
    np = nPink//10 + 1 

print(nb*cb + np*cp)