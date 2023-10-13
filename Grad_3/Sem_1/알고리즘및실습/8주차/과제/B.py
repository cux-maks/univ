T = int(input())
for _ in range(T):
    N = int(input())
    num = []
    for i in sorted(list(map(int, input().split()))):
        s = str(i)
        l = len(s)
        while len(s) < 10: s += s[len(s) - l]
        num.append((list(s), str(i)))
    num.sort(key = lambda x : x[0], reverse = True)
    result = ""
    for i in num: result += i[-1]
    print(result if int(result) != 0 else 0)
