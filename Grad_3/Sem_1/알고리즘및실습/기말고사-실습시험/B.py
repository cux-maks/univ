import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    S = list(input().rstrip())
    d = {}
    for x in range(len(S)):
        if S[x] not in d.keys(): d[S[x]] = [x]
        else: d[S[x]].append[x]
    buf = 0
    buf2 = 0
    for x in sorted(d.keys(), reverse = True):
        if len(d[x]) - d[x].count(-1) > 1:
            for i in range(len(d[x])):
                if d[x][i] > buf2:
                    S[d[x][i]] = None
                    buf = d[x][i]
                    d[x][i] = -1
                else:
                    S[d[x][i]] = None
                    buf2 = d[x][i]
                    d[x][i] = -1
