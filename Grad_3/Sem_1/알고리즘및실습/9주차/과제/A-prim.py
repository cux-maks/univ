import sys
import heapq

input = sys.stdin.readline

def prim(adj_list):
    N = len(adj_list)
    visited = [False] * N
    pq = []
    start_node = 0
    visited[start_node] = True

    for adj_node, weight in adj_list[start_node]:
        heapq.heappush(pq, (weight, start_node, adj_node))

    mst_cost = 0
    while pq:
        weight, src, dst = heapq.heappop(pq)
        if visited[dst]:
            continue
        visited[dst] = True
        mst_cost += weight
        for adj_node, weight in adj_list[dst]:
            if not visited[adj_node]:
                heapq.heappush(pq, (weight, dst, adj_node))

    return mst_cost


T = int(input().rstrip())
for _ in range(T):
    N, E = map(int, input().rstrip().split())
    adj_list = [[] for _ in range(N)]
    buf = list(map(int, input().rstrip().split()))
    for i in range(0, E * 3, 3):
        adj_list[buf[i]].append((buf[i + 1], buf[i + 2]))
        adj_list[buf[i + 1]].append((buf[i], buf[i + 2]))
    print(prim(adj_list))
