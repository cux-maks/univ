'''
1) 임의의 시퀀스 데이터가 주어졌을 때 중복을 제거하는 함수(my_func) 만들기
입력은 아래 x, y와 같은 시퀀스가 주어질 수 있으며 각 입력의 원소는 'int' 혹은 'str' 타입을 가질 수 있음
출력은 중복이 제거된 list가 반환되어야 함
2) 사전을 원소로만 갖는 임의의 시퀀스 데이터가 주어졌을 때 지정하는 key에 대응하는 value의 중복을 제거하는 함수(my_func2) 만들기
입력은 아래 x2, y2와 같은 시퀀스가 주어질 수 있으며 각 입력의 원소는 오직 사전 'dict' 타입만 가질 수 있음
함수(my_func2)의 또 다른 입력으로써 중복을 제거하길 원하는 key를 임의로 입력되어야 함
출력은 중복이 제거된 list가 반환되어야 함
'''

def my_func(a):
    return list(set(a))

def my_func2(a, key):

    # print("def my_func2:", a, key)

    def item_value(item, key): # dict 자료형에서 특정 key에 대한 value만 뽑아서 tuple로 반환하는 함수
        values = [] # 이 함수의 반환값을 저장할 list
        for _key in key: # key에서 한 개씩 불러와서 _key에 대입
            values.append(item.get(_key)) # values에 item에서 _key값에 해당하는 데이터 append
            # print("print_def_item_value:", values)
        return tuple(values)

    result = [] # 이 함수의 반환값 저장할 list
    seen = set() # 본 적 있는놈 저장하는 set 자료형

    for items in a: # 전달받은 dict 자료형에서 한개씩 뽑아오며 반복
       #  print("for_items_in_a:", items)
        val = items if key is None else item_value(items, key) # val은 만약 key값이 None이라면 items, 그게 아니라면 item_value(items, key)를 실행한 결과를 저장
        if val not in seen: # 만약 val값이 이전에 본 아이템이 아니다
            result.append(items) # 결과 리스트에 items 추가
            seen.add(val) # 본 적 있는놈에도 추가
        elif val == (None, ): # 만약 val값이 tuple이긴 한데,,,, (None, ) 이다
            result.append(items) # 결과 리스트에 items 추가
    return result # 결과 리스트 반환

x = [1, 5, 2, 1, 9, 1, 5, 10]
y = ['a', 'bc', 'a', 'b_', 123, 78, 'bc', '123', 123, 'b']

x2 = [
  {'a':1, 'b':1},
  {'a':1, 'b':2},
  {'a':1, 'b':1},
  {'a':2, 'b':2}
]
y2 = [
  {'a': 'x', 'b': 'y'}, 
  {'a': 'x1', 'b': 'y1'}, 
  {'a': 'x', 'b': 'y'}, 
  {'a': 'x1'}, 
  {'b': 'y1'}, 
  {'b': 'y2'}
]

x_ = my_func(x)
y_ = my_func(y)

print("print(my_func(x)) -> ", x_)
print("print(my_func(y)) -> ", y_)

x2_ = my_func2(x2, key = ('a', 'b'))
x22_ = my_func2(x2, key = ('a'))
y2_ = my_func2(y2, key = ('a', 'b'))
y22_ = my_func2(y2, key = ('a'))

print("print(my_func2(x2, key=('a', 'b'))) -> ", x2_)
print("print(my_func2(x2, key=('a'))) -> ", x22_)
print("print(my_func2(y2, key=('a', 'b'))) -> ", y2_)
print("print(my_func2(y2, key=('a'))) -> ", y22_)