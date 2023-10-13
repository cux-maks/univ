def get_optimal_schedule(jobs, N):

    profit = 0
    info = [-1 for _ in range(N)]
    ret = []
    jobs.sort(key = lambda x: x[1], reverse=True)
    for job in jobs:
        for j in reversed(range(job[0])):
            if j < N and info[j] == -1:
                info[j] = job[2]
                ret.append(job[2])
                profit += job[1]
                break
    return ret

T = int(input())
for _ in range(T):
    N = int(input())
    J = list(map(int, input().split()))
    jobs = []
    for i in range(0, N*2, 2):
        jobs.append((J[i], J[i + 1], i // 2 + 1))
    result = get_optimal_schedule(jobs, N // 2 + 1)
    print(*sorted(result))
