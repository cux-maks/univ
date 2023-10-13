import sys
input = sys.stdin.readline

def countsum(m, nums, memo):
    if m < 0: return 0
    if m == 0: return 1
    if memo[m] != -1: return memo[m]
    cnt = 0
    for x in nums:
        cnt += countsum(m - x, nums, memo)
    memo[m] = cnt
    return memo[m]

for _ in range(int(input().rstrip())):
    M, N = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    MEMO = [-1] * (M + 1)
    print(countsum(M, nums, MEMO))