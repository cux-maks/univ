import sys
input = sys.stdin.readline

def cansum(m, nums, memo):
    if m < 0: return False
    if m == 0: return True
    if memo[m] != -1: return memo[m] == 1
    for x in nums:
        if cansum(m - x, nums, memo):
            memo[m] = 1
            return True
    memo[m] = 0
    return False

for _ in range(int(input().rstrip())):
    M, N = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    result = cansum(M, nums, [-1 for _ in range(M + 1)])
    if result: print("true")
    else: print("false")