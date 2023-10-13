import copy
import sys
input = sys.stdin.readline

def howsum(m, A):
    table = [None] * (m+1)
    table[0] = []
    for i in range(m+1):
        if table[i] != None:
            for x in A:
                if i+x <= m and table[i+x] == None:
                    table[i+x] = table[i] + [x]
    return table[m]


for _ in range(int(input().rstrip())):
    M, N = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    result = howsum(M, nums)
    if result == None: print(-1)
    else: print(len(result), *result)