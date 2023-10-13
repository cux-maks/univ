'''
1) 아래 주어진 코드의 출력 결과를 초래한 함수 my_average 함수 만들기
my_average는 1개 이상의 숫자 값을 받아 평균을 구하는 함수
입력 인자를 단 한개도 주지 않을 경우 아래 에러를 반환해야함
print(my_average())
TypeError: my_average() missing 1 required positional argument: ......
코드
print(my_average(1))
print(my_average(1, 2, 3, 4))
print(my_average(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(my_average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
출력 결과
1.0
2.5
5.0
8.0

2) Call-back 함수 만들기 : 아래 주어진 코드의 결과를 초래한 모든 함수(apply_function, add) 만들기
단, (apply_function, add) 함수에서는 print 구문 사용 금지
my_callback 함수는 아래 셀에 주어진 것과 같음
코드
apply_function(add, (1, 2, 3), callback=my_callback)
apply_function(add, ('script', 'programming', 'is', 'the', 'best'), callback=my_callback)
코드 수행 결과
my result: 6
my result: scriptprogramming is the best
'''

def my_average(*nums):
  if len(nums) == 0:
    return 'TypeError: my_average() missing 1 required positional argument: ......'
  else: 
    return sum(nums)/len(nums)

def my_callback(result):
    print('my result:', result)

def add(values):
  result = type(values[0])()
  for a in values:
    result += a
    if type(values[0]) == ' str':
      result += ' '
  return result

def apply_function(f, values, callback):
  result = f(values)
  callback(result)


print(my_average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
apply_function(add, (1, 2, 3), callback=my_callback)
apply_function(add, ('script', 'programming', 'is', 'the', 'best'), callback=my_callback)