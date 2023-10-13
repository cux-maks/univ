import sys
input = sys.stdin.readline

def Floyed_Warshall(G, n):
    dist = [[float('inf') if i != j else 0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != float('inf'): dist[i][j] = G[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in range(n):
        if dist[i][i] < 0: return None
    return dist

for _ in range(int(input().rstrip())):
    N, E = map(int, input().rstrip().split())
    buf = list(map(int, input().rstrip().split()))
    graph = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(0, E*3, 3):
        graph[buf[i]][buf[i + 1]] = buf[i + 2]
    result = Floyed_Warshall(graph, N)
    if result == None:
        print(-1)
    else:
        start = None
        end = None
        max_val = -1 * float('inf')
        for i in range(len(result)):
            for j in range(len(result[i])):
                if result[i][j] != float('inf') and result[i][j] > max_val:
                    start, end, max_val = i, j, result[i][j]
        print(start, end, max_val)

