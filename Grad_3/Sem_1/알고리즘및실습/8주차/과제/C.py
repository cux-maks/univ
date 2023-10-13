T = int(input())

for _ in range(T):
    N = int(input())
    stack = []
    p = map(int, input().split())
    for planet in p:
        while stack and stack[-1] > 0 and planet < 0:
            if stack[-1] < abs(planet):
                stack.pop()
            elif stack[-1] == abs(planet):
                stack.pop()
                break
            else:
                break
        else:
            stack.append(planet)

    print(*stack)