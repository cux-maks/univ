import sys
input = sys.stdin.readline

def bestsum(m, A):
    table = [None] * (m+1)
    table[0] = []

    for i in range(m+1):
        if table[i] != None:
            for x in A:
                if i+x <= m:
                    new_combination = table[i] + [x]
                    if table[i+x] == None or len(new_combination) < len(table[i+x]):
                        table[i+x] = new_combination

    return table[m]

for _ in range(int(input().rstrip())):
    M, N = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    result = bestsum(M, nums)
    if result == None: print(-1)
    else: print(len(result), *result)