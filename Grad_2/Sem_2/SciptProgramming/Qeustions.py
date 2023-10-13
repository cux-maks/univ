# # 20221023 박주을 Question

# #교재 6.5절의 이중연결구조로 덱 구현하고, 후단을 스택으로 사용하여 깊이우선탐색에 적용

# class DNode:
#     def __init__(self, elem, prev = None, next = None):
#         self.data = elem
#         self.prev = prev
#         self.next = next

# class DoublyLinkedDeque:
#     def __init__(self):
#         self.front = None
#         self.array = []
#         self.top = None

#     def isEmpty(self):
#         return self.front == None

#     def clear(self):
#         self.front = self.front = None

#     def size(self):
#         node = self.front
#         count = 0
#         while not node == None:
#             node = node.next
#             count += 1
#         return count

#     def display(self, msg):
#         print(msg, end='')
#         node = self.front
#         while not node == None:
#             print(node.data, end='')
#             node = node.next
#         print()

#     def disp_list(self):
#         node = self.front
#         ret_val = []
#         while not node == None:
#             ret_val.append(node.data)
#             node = node.next
#         return ret_val

#     def addFront(self, item):
#         node = DNode(item, None, self.front)
#         if (self.isEmpty()):
#             self.front = self.top = node
#         else:
#             self.front.prev = node
#             self.front = node

#     def addRear(self, item):
#         node = DNode(item, self.top, None)
#         if (self.isEmpty()):
#             self.front = self.top = node
#         else:
#             self.top.next = node
#             self.top = node

#     def deleteFront(self):
#         if not self.isEmpty():
#             data = self.front.data
#             self.front = self.front.next
#             if self.front == None:
#                 self.top = None
#             else:
#                 self.front.prev = None
#             return data

#     def deleteRear(self):
#         if not self.isEmpty():
#             data = self.top.data
#             self.top = self.top.prev
#             if self.top == None:
#                 self.front = None
#             else:
#                 self.top.next = None
#             return data

# # ----------------------------------------------------------------

# MAZE_SIZE_X = 10
# MAZE_SIZE_Y = 12
# map = [['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
#        ['1', '1', '1', '1', '1', '1', '0', '1', '0', '1'],
#        ['1', '1', '1', '1', '1', '1', '0', '0', '0', '1'],
#        ['1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
#        ['1', '1', '1', '1', '1', '1', '1', '0', '0', 'x'],
#        ['1', '1', '0', '0', '1', '1', '0', '0', '1', '1'],
#        ['1', '1', '1', '0', '0', '0', '0', '1', '1', '1'],
#        ['1', '1', '1', '0', '1', '1', '1', '1', '1', '1'],
#        ['1', '1', '1', '0', '1', '1', '1', '1', '1', '1'],
#        ['e', '0', '1', '0', '1', '1', '1', '1', '1', '1'],
#        ['1', '0', '0', '0', '0', '0', '0', '1', '1', '1'],
#        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

# def isValidPos(map, x, y):
#     if x < 0 or y < 0 or x >= MAZE_SIZE_X or y >= MAZE_SIZE_Y:
#         return False
#     elif map[y][x] == '0' or map[y][x] == 'x':
#         return True

# def DFS():
#     stack = DoublyLinkedDeque()
#     stack.addRear((0, 9))
#     print('DFS: ')

#     while not stack.isEmpty():
#         here = stack.deleteRear()
#         print(here, end='->')
#         (x, y) = here
#         if (map[y][x] == 'x'):
#             map[y][x] = '.'
#             return True
#         else:
#             map[y][x] = '.'
#             if isValidPos(map, x, y - 1): stack.addRear((x, y - 1))
#             if isValidPos(map, x, y + 1): stack.addRear((x, y + 1))
#             if isValidPos(map, x - 1, y): stack.addRear((x - 1, y))
#             if isValidPos(map, x + 1, y): stack.addRear((x + 1, y))
#         print(' 현재 스택 :', stack.disp_list())
#         # print(' 현재 스택 : ', list(filter(None, stack.array)))
#     return False

# if __name__ == '__main__':
#     result = DFS()
#     if result:
#         print(' --> 미로탐색 성공\n')
#     else:
#         print(' --> 미로탐색 실패\n')

# # 20221009 최상규 Question

# MAZE_SIZE = 11
# map = [['1','1','0','1','1','1','1','1','1','1','0'],
#        ['e','0','0','0','0','0','0','0','0','1','1'],
#        ['1','1','1','0','1','1','0','1','0','0','1'],
#        ['1','1','1','0','0','1','0','1','1','0','1'],
#        ['0','1','1','0','1','1','0','1','0','0','x'],
#        ['0','1','0','0','1','1','0','1','1','1','0'],
#        ['0','1','1','1','1','1','0','0','0','0','1'],
#        ['0','1','0','0','0','0','1','1','0','1','1'],
#        ['0','1','0','1','1','0','0','0','0','1','0'],
#        ['0','1','1','1','0','0','1','1','1','1','0'],
#        ['1','1','1','1','1','1','1','1','1','1','0']]

# class CircularQueue:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.front = 0
#         self.rear = 0
#         self.items = [None] * capacity

#     def print(self):
#         return self.items

#     def isEmpty(self):
#         return self.front == self.rear

#     def isFull(self):
#         return self.front == (self.rear + 1) % self.capacity

#     def clear(self):
#         self.front = self.rear

#     def enqueue(self, item):
#         if not self.isFull():
#             # self.rear = (self.rear + 1) & self.capacity
#             self.items[self.rear] = item
#             self.rear += 1
#             # print("enqueue value: ", self.rear - 1, self.items[self.rear - 1])

#     def dequeue(self):
#         if not self.isEmpty():
#             # self.front = (self.front + 1) & self.capacity
#             self.front += 1
#             return self.items[self.front - 1]

#     def peek(self):
#         if not self.isEmpty():
#             return self.items[(self.front + 1) % self.capacity]

#     def size(self):
#         return (self.rear - self.front + self.capacity) % self.capacity

#     # def print(self):
#     #     print(self.items)

# def isValidPos(x, y, map):
#     if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
#         return False
#     else:
#         return map[y][x] == '0' or map[y][x] == 'x'

# def BFS():
#     que = CircularQueue(50)
#     que.enqueue((0,1))
#     print('BFS: ')
    
#     while que.isEmpty() != True:
#         here = que.dequeue()
#         print(here, end='->')
#         x, y = here
#         if (map[y][x] == 'x'):
#             return True
#         else:
#             map[y][x] = '.'
#             if isValidPos(x, y - 1, map) : #상
#                 que.enqueue((x, y - 1))
#             if isValidPos(x, y + 1, map) : #하
#                 que.enqueue((x, y + 1))
#             if isValidPos(x - 1, y, map) : #좌
#                 que.enqueue((x - 1, y))
#             if isValidPos(x + 1, y, map) : #우
#                 que.enqueue((x + 1, y))
#         #print('현재스택 : ',end='')
#         #for x in range (que.size()):
#            # if (que.items[x] != None):
#                # print(que.items[x],end='')
#         #print('')
#     return False

# result1 = BFS()
# if result1 : print(' --> 미로탐색 성공')
# else: print(' --> 미로탐색 실패')

# 20221002 홍민이형 Question
# map = [ ['1','1','1','1','1','1'],
#         ['e','0','0','0','0','1'],
#         ['1','0','1','0','1','1'],
#         ['1','1','1','0','0','x'],
#         ['1','1','1','0','1','1'],
#         ['1','1','1','1','1','1']]
# MAZE_SIZE = 6

# class ArrayStack :
#     def __init__(self,capacity):
#         self.capacity = capacity
#         self.array = [None]*self.capacity
#         self.top = -1

#     def isEmpty(self) : return self.top == -1
#     def isFull(self) : return self.top == self.capacity-1

#     def push( self, item ):
#         if not self.isFull() :
#             self.top += 1 # 처음 self.top 은 - 1임.
#             self.array[self.top] = item # self.array[-1] , 즉 맨 아래에 삽입
#         else: pass # overflow 예외는 처리하지 않았음

#     def pop( self ):
#         if not self.isEmpty(): # 비어있지 않아야 self.top -1이 가능함
#             self.top -= 1
#             return self.array[self.top+1]
#         else: pass # underflow 예외는 처리하지 않았음

#     def peek( self ):
#         if not self.isEmpty():
#             return self.array[self.top - 1]
#         else: pass # underflow 예외는 처리하지 않았음
    
#     def to_list(self):
#         if not self.isEmpty():
#             return self.array[:self.top + 1]
#         else: pass

#     def size( self ) : 
#         return self.top+1      
    
#     def __str__(self):
#         return str(self.top)

# def isValidPos(x,y) :
#     if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE : return False
#     else : return map[y][x] == '0' or map[y][x] == 'x'  # 갈 수 있는 곳이면 True 반환

# def DFS() :
#     stack = ArrayStack(50)
#     stack.push((0,1))
#     print('DFS :')

#     while not stack.isEmpty():
#         here = stack.pop()
#         print(here,end = '->')
#         (x,y) = here
#         if (map[y][x] == 'x') : return True
#         else :
#             map[y][x] = '.'
#             if isValidPos(x,y-1) : stack.push((x,y-1)) #상
#             if isValidPos(x,y+1) : stack.push((x,y+1)) #하
#             if isValidPos(x-1,y) : stack.push((x-1,y)) #좌
#             if isValidPos(x+1,y) : stack.push((x+1,y)) #우
#         print(' 현재 스택: ', stack.to_list())    # 현재 스택 내용 출력
#     return False

# if DFS() == True : print('미로탐색 생공')
# else : print('미로탐색 생공')

# 20221002 박주을 Question
# import copy

# class ArrayStack:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.array = [None]*self.capacity
#         self.top = -1

#     def isEmpty(self):
#         return self.top == -1

#     def isFull(self):
#         return self.top == self.capacity - 1

#     def push (self, item):
#         if not self.isFull():
#             self.top += 1
#             self.array[self.top] = item
#         else:
#             pass

#     def pop(self):
#         if not self.isEmpty():
#             self.top -= 1
#             return self.array[self.top+1]
#         else:
#             pass

#     def peek(self):
#         if not self.isEmpty():
#             return self.array[self.top]
#         else:
#             pass

#     def size(self):
#         return self.top + 1

# #----------------------------------------------------

# MAZE_SIZE_X = 10
# MAZE_SIZE_Y = 12
# map = [['1','1','1','1','1','1','1','1','1','1'],
#        ['1','1','1','1','1','1','0','1','0','1'],
#        ['1','1','1','1','1','1','0','0','0','1'],
#        ['1','1','1','1','1','1','1','1','0','1'],
#        ['1','1','1','1','1','1','1','0','0','x'],
#        ['1','1','0','0','1','1','0','0','1','1'],
#        ['1','1','1','0','0','0','0','1','1','1'],
#        ['1','1','1','0','1','1','1','1','1','1'],
#        ['1','1','1','0','1','1','1','1','1','1'],
#        ['e','0','1','0','1','1','1','1','1','1'],
#        ['1','0','0','0','0','0','0','1','1','1'],
#        ['1','1','1','1','1','1','1','1','1','1']]

# map_copy = copy.deepcopy(map)

# def isValidPos(map, x, y):
#     if x < 0 or y < 0 or x >= MAZE_SIZE_X or y >= MAZE_SIZE_Y:
#         return False
#     elif map[y][x] == '0' or map[y][x] == 'x':
#         return True

# # def isValidPosCopy(x, y):
# #     if x < 0 or y < 0 or x>= MAZE_SIZE_X or y >= MAZE_SIZE_Y:
# #         return False
# #     else:
# #         return map_copy[y][x] == '0' or map_copy[y][x] == 'x'

# def DFS():
#     stack = ArrayStack(1000)
#     stack.push((0, 9))
#     print('DFS: ')

#     while not stack.isEmpty():
#         here = stack.pop()
#         print(here, end = '->')
#         (x, y) = here
#         if (map[y][x] == 'x'):
#             map[y][x] = '.'
#             return True
#         else:
#             map[y][x] = '.'
#             if isValidPos(map, x, y-1): stack.push((x, y-1))
#             if isValidPos(map, x, y+1): stack.push((x, y+1))
#             if isValidPos(map, x-1, y): stack.push((x-1, y))
#             if isValidPos(map, x+1, y): stack.push((x+1, y))
#         print(' 현재 스택 : ', list(filter(None, stack.array)))
#     return False

# #----------------------------------------------------

# def DFSCopy():
#     stack_c = ArrayStack(1000)
#     stack_c.push((0, 9))
#     print('DFSCopy: ')

#     while not stack_c.isEmpty():
#         here_c = stack_c.pop()
#         print(here_c, end = '->')
#         (x, y) = here_c
#         if map_copy[y][x] == 'x':
#             map_copy[y][x] = '.'
#             return True
#         else:
#             map_copy[y][x] = '.'
#             if isValidPos(map_copy, x, y-1): stack_c.push((x, y-1))
#             if isValidPos(map_copy, x, y+1): stack_c.push((x, y+1))
#             if isValidPos(map_copy, x+1, y): stack_c.push((x+1, y))
#             if isValidPos(map_copy, x-1, y): stack_c.push((x-1, y))

#         print(' 현재 스택 : ', list(filter(None, stack_c.array)))
#     return False

# result = DFS()
# if result: print(' --> 미로탐색 성공')
# else: print(' --> 미로탐색 실패')

# result_copy = DFSCopy()
# if result_copy: print(' --> 미로탐색 성공')
# else: print(' --> 미로탐색 실패')