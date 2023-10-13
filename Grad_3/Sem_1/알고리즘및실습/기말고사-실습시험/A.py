import sys
input = sys.stdin.readline

def sol(A, B):
    dp = [[0 for _ in range(len(B) + 2)] for _ in range(len(A) + 2)]
    for i in range(1, len(A) + 1):
        check = False
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                if check == True: dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    check = True
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j])

    return dp[len(A)][len(B)]

for _ in range(int(input().rstrip())):
    A = input().rstrip()
    B = input().rstrip()
    if len(A) > len(B): print(sol(B, A))
    else: print(sol(A, B))