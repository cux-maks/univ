#stack
class stack:
    def __init__(self):
        self.data = [None for _ in range(4)] # => [None, None, None, None]
        self.top = 0

    def peek(self):     # 가장 위에 있는 원소를 반환
        return self.data[self.top - 1]

    def pop(self):      # 가장 위에 있는 원소를 제거
        self.data[self.top - 1] = None
        self.top -= 1

    def push(self, num): # 새로운 데이터 추가
        # self.data.append(num)
        self.data[self.top] = num
        self.top += 1

    def print_me(self):
        print(self.data)

Stack = stack()

'''
### 자동으로 리스트의 크기를 늘리는 함수를 작성해오세요
1. 리스트의 크기가 증가되는 조건
2. 리스트의 크기가 한 번에 얼마나 증가되는지 - 기존의 x 2
3. 리스트이 크기가 증가될 때 코드 설명
'''