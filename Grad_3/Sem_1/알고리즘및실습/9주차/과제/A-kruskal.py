import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input().rstrip())
for _ in range(T):
    N, E = map(int, input().rstrip().split())
    edges = []
    buf = list(map(int, input().rstrip().split()))
    for i in range(0, E*3, 3):
        edges.append((buf[i + 2], buf[i], buf[i + 1]))
    edges.sort()
    parent = [i for i in range(N)]
    ans = 0
    for cost, start, end in edges:
        if find(parent, start) != find(parent, end):
            union(parent, start, end)
            ans += cost
    print(ans)
    