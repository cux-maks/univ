import sys
input = sys.stdin.readline

def sol(nums, target, idx, currSum, memo):
    key = str(idx) + "-" + str(currSum)
    if key in memo.keys(): return memo[key]
    if idx == len(nums):
        if currSum == target:
            memo[key] = 1
        else:
            memo[key] = 0
        
    cnt1 = sol(nums, target, idx + 1, currSum + nums[idx], memo)
    cnt2 = sol(nums, target, idx + 1, currSum, memo)

    memo[key] = cnt1 + cnt2
    return memo[key]

for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    nums = list(map(int, input().rstrip().split()))
    if sum(nums) % 2 == 1: print("false")
    else: print("true" if sol(nums, sum(nums)//2, 0, 0, dict()) else "")
