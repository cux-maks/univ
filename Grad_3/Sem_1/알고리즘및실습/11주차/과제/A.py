import sys
input = sys.stdin.readline

def sequenceAlignment(X, Y, misP, gapP):
    m = len(X)
    n = len(Y)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        table[i][0] = i * gapP

    for j in range(1, n + 1):
        table[0][j] = j * gapP

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            p = 0 if X[i - 1] == Y[j - 1] else misP
            table[i][j] = min(p + table[i - 1][j - 1], gapP + table[i - 1][j], gapP + table[i][j - 1])

    return table[m][n]


for _ in range(int(input().rstrip())):
    G, M, X, Y = map(str, input().rstrip().split(' '))
    G = int(G)
    M = int(M)
    X = list(X)
    Y = list(Y)
    result = sequenceAlignment(X, Y, M, G)
    print(result)
