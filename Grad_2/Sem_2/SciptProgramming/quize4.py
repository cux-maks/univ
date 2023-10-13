'''
Plus to Minus
"plus"라는 이름의 파일을 읽기
읽어 온 내용 중 + 연산자는 모두 - 연산자로 대체하여 "minus"라는 새로운 파일 만들기
"minus" 파일은 "/content/temp4/temp5/temp6" 폴더에 생성되어야 함
"minus_solution" 이라는 파일을 생성하여 "minus" 파일 내용 중 "<?>"에 들어가야 할 정답만 따로 쓸 것
"minus_solution" 파일 역시 "/content/temp4/temp5/temp6" 폴더 아래에 생성되어야 함
'''

import os
import random

path = '/'.join([os.getcwd(), 'temp1', 'temp2', 'temp3'])
if not os.path.exists(path):
  os.makedirs(path)

path_2 = '/'.join([os.getcwd(), 'temp4', 'temp5', 'temp6'])
if not os.path.exists(path_2):
  os.makedirs(path_2)

file_path = '/'.join([path, 'plus'])

with open(file_path, 'w', encoding='utf-8') as f:
  for _ in range(100):
    question = '+'.join([str(random.randrange(0, 10)) for i in range(random.randrange(2, 5))]) + '=<?>\n'
    print(question, file=f, end='')

s = open('/content/temp1/temp2/temp3/plus')
minus = open('/content/temp4/temp5/temp6/minus', 'w')
minus_solution = open('/content/temp4/temp5/temp6/minus_solution', 'w')

for i, line in enumerate(s):

  line_str = list(line)
  for k in range(0, len(line)):
    if line_str[k] == '+': line_str[k] = '-'
  # print(i+1, ':', line, end="")
  line_str = ''.join(a for a in line_str)
  minus.write(line_str)

  line_str = line_str[0 :len(line_str) - 4]
  line_list = list(line_str)
  result = int(line_list[0])
  for a in line_list[1:]:
    if a != '-' and a != '=': result -= int(a)
  line_str += str(result)
  line_str += "\n"
  minus_solution.write(line_str)

s.close()
minus.close()
minus_solution.close()

minus = open('/content/temp4/temp5/temp6/minus', 'r')
minus_solution = open('/content/temp4/temp5/temp6/minus_solution', 'r')

print("minus\n")
for i, line in enumerate(minus):
  print(i+1, ':', line, end="\n")
print("minus_solution\n")
for i, line in enumerate(minus_solution):
  print(i+1, ':', line, end="\n")

minus.close()
minus_solution.close()