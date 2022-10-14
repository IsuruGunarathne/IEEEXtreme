## basically the same as the fibonacci sequence, but with a different formula

ways = [0 for i in range(22001)]
ways[0] = 0
ways[1] = 1
ways[2] = 2

for i in range(3, 22001):
    ways[i] = ways[i - 1] + ways[i - 2]


times = int(input())
WaysOut = []

for i in range(times):
    n = int(input())
    WaysOut.append(ways[n])

for i in WaysOut:
    print(i)