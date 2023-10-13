'''
1) 문제
2048 게임은 4×4 크기의 보드에서 혼자 즐기는 재미있는 게임이다. 이 링크를 누르면 게임을 해볼 수 있다.
이 게임에서 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다. 이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다. 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다. (실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)



<그림 1>의 경우에서 위로 블록을 이동시키면 <그림 2>의 상태가 된다. 여기서, 왼쪽으로 블록을 이동시키면 <그림 3>의 상태가 된다.


<그림 4>의 상태에서 블록을 오른쪽으로 이동시키면 <그림 5>가 되고, 여기서 다시 위로 블록을 이동시키면 <그림 6>이 된다. 여기서 오른쪽으로 블록을 이동시켜 <그림 7>을 만들 수 있다.


<그림 8>의 상태에서 왼쪽으로 블록을 옮기면 어떻게 될까? 2가 충돌하기 때문에, 4로 합쳐지게 되고 <그림 9>의 상태가 된다.


<그림 10>에서 위로 블록을 이동시키면 <그림 11>의 상태가 된다.

<그림 12>의 경우에 위로 블록을 이동시키면 <그림 13>의 상태가 되는데, 그 이유는 한 번의 이동에서 이미 합쳐진 블록은 또 합쳐질 수 없기 때문이다.


마지막으로, 똑같은 수가 세 개가 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다. 예를 들어, 위로 이동시키는 경우에는 위쪽에 있는 블록이 먼저 합쳐지게 된다. <그림 14>의 경우에 위로 이동하면 <그림 15>를 만든다.


이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다. 보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

2) 입력
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다. 0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다. 블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.


3) 출력
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
'''

from itertools import *
max_size = int(input())

board = []
maxResult = 0

def right(map):
  returnValue = []
  for x in map:
    buffer = []
    for y in range(0, x.count(0)):
      buffer.append(0)
    for y in x:
      if y != 0: buffer.append(y)
    returnValue.append(buffer)
  map = returnValue
  returnValue = []
  for x in map:
    for y in range(len(x) - 1):
      if x[len(x) - y - 2] == x[len(x) - y - 1]:
        x[len(x) - y - 1] = x[len(x) - y - 2] + x[len(x) - y - 1]
        x[len(x) - y - 2] = 0
  for x in map:
    buffer = []
    for y in range(0, x.count(0)):
      buffer.append(0)
    for y in x:
      if y != 0: buffer.append(y)
    returnValue.append(buffer)
  return returnValue

def left(map):
  returnValue = []
  for x in map:
    buffer = []
    for y in x:
      if y != 0: buffer.append(y)
    for y in range(0, x.count(0)):
      buffer.append(0)
    returnValue.append(buffer)
  map = returnValue
  returnValue = []
  for x in map:
    for y in range(len(x) - 1):
      if x[y] == x[y + 1]:
        x[y] = x[y] + x[y + 1]
        x[y + 1] = 0
  for x in map:
    buffer = []
    for y in x:
      if y != 0: buffer.append(y)
    for y in range(0, x.count(0)):
      buffer.append(0)
    returnValue.append(buffer)
  return returnValue

def up(map):
  value = []
  returnValue = []
  for x in range(len(map[0])):
    buffer = []
    for y in range(len(map[0])):
      buffer.append(map[y][x])
    value.append(buffer)
  value = left(value)
  for x in range(len(map[0])):
    buffer = []
    for y in range(len(map[0])):
      buffer.append(value[y][x])
    returnValue.append(buffer)
  return returnValue

def down(map):
  value = []
  returnValue = []
  for x in range(len(map[0])):
    buffer = []
    for y in range(len(map[0])):
      buffer.append(map[y][x])
    value.append(buffer)
  value = right(value)
  for x in range(len(map[0])):
    buffer = []
    for y in range(len(map[0])):
      buffer.append(value[y][x])
    returnValue.append(buffer)
  return returnValue

for x in range(0, max_size):
  board.append(list(map(int, input().split())))

method = list(product([x for x in range(0, 4)], repeat = 5))
c_board = board

for y in method:
  board = c_board
  for x in range(len(y)):
    if y[x] == 0:
      board = right(board)
    elif y[x] == 1:
      board = left(board)
    elif y[x] == 2:
      board = up(board)
    elif y[x] == 3:
      board = down(board)
  for y in board:
    buffer = y
    buffer.append(maxResult)
    maxResult = max(buffer)
print(maxResult)