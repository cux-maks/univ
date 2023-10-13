import heapq
import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a <= b: parent[b] = a
    else: parent[a] = b

def kruskal(edges, skip):
    parent = [i for i in range(N)]
    weight = 0
    for i in range(len(edges)):
        cost, start, end, idx = edges[i]
        if idx == skip: continue
        if find(parent, start) != find(parent, end):
            union(parent, start, end)
            weight += cost
    return weight

T = int(input().rstrip())
for _ in range(T):
    N, E = map(int, input().rstrip().split())
    edges = []
    buf = list(map(int, input().rstrip().split()))
    for i in range(0, E*3, 3):
        edges.append((buf[i + 2], buf[i], buf[i + 1], i//3))
    edges.sort()
    weight = kruskal(edges, -1)
    result = []
    for i in range(len(edges)):
        w = kruskal(edges, i)
        if w != weight:
            result.append(i)
    if len(result) == 0: print(-1)
    else: print(*sorted(result))

