import sys
input = sys.stdin.readline

def knapsack(items, W):
    n = len(items)
    table = [[0] * (W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for x in range(1, W+1):
            if items[i-1][1] > x:
                table[i][x] = table[i-1][x]
            else:
                table[i][x] = max(table[i-1][x], table[i-1][x-items[i-1][1]] + items[i-1][0])
    return table[n][W]

for _ in range(int(input().rstrip())):
    W, N = map(int, input().rstrip().split())
    buf = list(map(int, input().rstrip().split()))
    things = []
    for i in range(0, N * 2, 2):
        things.append((buf[i], buf[i + 1]))
    result = knapsack(things, W)
    print(result)