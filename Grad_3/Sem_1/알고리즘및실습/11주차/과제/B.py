import sys
input = sys.stdin.readline

def find_target_sum_count(nums, target, current_sum, index, memo):
    if index == len(nums):
        if current_sum == target:
            return 1
        else:
            return 0
    
    if memo[index][current_sum] is not None:
        return memo[index][current_sum]
    
    positive_count = find_target_sum_count(nums, target, current_sum + nums[index], index + 1, memo)
    negative_count = find_target_sum_count(nums, target, current_sum - nums[index], index + 1, memo)
    
    memo[index][current_sum] = positive_count + negative_count
    
    return memo[index][current_sum]

for _ in range(int(input().rstrip())):
    M, N = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    memo = [[None] * 2001 for _ in range(N)]
    result = find_target_sum_count(nums, M, 0, 0, memo)
    print(result)