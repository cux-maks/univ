'''
1) 아래 주어진 문장에서 모든 단어 마다 몇 번 등장하는지 출력할 수 있는 프로그램 작성
주의 사항
".", ",", "(", ")", " " 와 같은 문자는 제거할 것.
문장 1
A woman finds a pot of treasure on the road while she is returning from work. Delighted (very happy) with her luck, she decides to keep it. As she is taking it home, it keeps changing. However, her enthusiasm refuses to fade away (disappear or faint slowly).
결과물 1: [('A', 1), ('woman', 1), ('finds', 1), ('a', 1), ('pot', 1), ('of', 1), ('treasure', 1), ('on', 1), ('the', 1), ('road', 1), ('while', 1), ('she', 3), ('is', 2), ('returning', 1), ('from', 1), ('work', 1), ('Delighted', 1), ('very', 1), ('happy', 1), ('with', 1), ('her', 2), ('luck', 1), ('decides', 1), ('to', 2), ('keep', 1), ('it', 3), ('As', 1), ('taking', 1), ('home', 1), ('keeps', 1), ('changing', 1), ('However', 1), ('enthusiasm', 1), ('refuses', 1), ('fade', 1), ('away', 1), ('disappear', 1), ('or', 1), ('faint', 1), ('slowly', 1)]
문장 2
This classic fable (story) tells the story of a very slow tortoise (another word for turtle) and a speedy hare (another word for rabbit). The tortoise challenges the hare to a race. The hare laughs at the idea that a tortoise could run faster than him, but when the two actually race, the results are surprising.
결과물 2: [('This', 1), ('classic', 1), ('fable', 1), ('story', 2), ('tells', 1), ('the', 5), ('of', 1), ('a', 4), ('very', 1), ('slow', 1), ('tortoise', 3), ('another', 2), ('word', 2), ('for', 2), ('turtle', 1), ('and', 1), ('speedy', 1), ('hare', 3), ('rabbit', 1), ('The', 2), ('challenges', 1), ('to', 1), ('race', 2), ('laughs', 1), ('at', 1), ('idea', 1), ('that', 1), ('could', 1), ('run', 1), ('faster', 1), ('than', 1), ('him', 1), ('but', 1), ('when', 1), ('two', 1), ('actually', 1), ('results', 1), ('are', 1), ('surprising', 1)]

2) 결과물 1과 결과물 2 간의 덧셈 뺄셈 기능 추가
결과물 1 + 결과물 2

결과: [('A', 1), ('woman', 1), ('finds', 1), ('a', 5), ('pot', 1), ('of', 2), ('treasure', 1), ('on', 1), ('the', 6), ('road', 1), ('while', 1), ('she', 3), ('is', 2), ('returning', 1), ('from', 1), ('work', 1), ('Delighted', 1), ('very', 2), ('happy', 1), ('with', 1), ('her', 2), ('luck', 1), ('decides', 1), ('to', 3), ('keep', 1), ('it', 3), ('As', 1), ('taking', 1), ('home', 1), ('keeps', 1), ('changing', 1), ('However', 1), ('enthusiasm', 1), ('refuses', 1), ('fade', 1), ('away', 1), ('disappear', 1), ('or', 1), ('faint', 1), ('slowly', 1), ('This', 1), ('classic', 1), ('fable', 1), ('story', 2), ('tells', 1), ('slow', 1), ('tortoise', 3), ('another', 2), ('word', 2), ('for', 2), ('turtle', 1), ('and', 1), ('speedy', 1), ('hare', 3), ('rabbit', 1), ('The', 2), ('challenges', 1), ('race', 2), ('laughs', 1), ('at', 1), ('idea', 1), ('that', 1), ('could', 1), ('run', 1), ('faster', 1), ('than', 1), ('him', 1), ('but', 1), ('when', 1), ('two', 1), ('actually', 1), ('results', 1), ('are', 1), ('surprising', 1)]
결과물 1 - 결과물 2

결과: [('A', 1), ('woman', 1), ('finds', 1), ('pot', 1), ('treasure', 1), ('on', 1), ('road', 1), ('while', 1), ('she', 3), ('is', 2), ('returning', 1), ('from', 1), ('work', 1), ('Delighted', 1), ('happy', 1), ('with', 1), ('her', 2), ('luck', 1), ('decides', 1), ('to', 1), ('keep', 1), ('it', 3), ('As', 1), ('taking', 1), ('home', 1), ('keeps', 1), ('changing', 1), ('However', 1), ('enthusiasm', 1), ('refuses', 1), ('fade', 1), ('away', 1), ('disappear', 1), ('or', 1), ('faint', 1), ('slowly', 1)]
'''

str_1 = "A woman finds a pot of treasure on the road while she is returning from work. Delighted (very happy) with her luck, she decides to keep it. As she is taking it home, it keeps changing. However, her enthusiasm refuses to fade away (disappear or faint slowly)."
str_2 = "This classic fable (story) tells the story of a very slow tortoise (another word for turtle) and a speedy hare (another word for rabbit). The tortoise challenges the hare to a race. The hare laughs at the idea that a tortoise could run faster than him, but when the two actually race, the results are surprising."

str_1 = list(str_1)
str_2 = list(str_2)

while(')' in str_1 or '(' in str_1 or '.' in str_1 or ',' in str_1 or ')' in str_2 or '(' in str_2 or '.' in str_2 or ',' in str_2):
  if '(' in str_1: str_1.remove('(')
  if ')' in str_1: str_1.remove(')')
  if '.' in str_1: str_1.remove('.')
  if ',' in str_1: str_1.remove(',')
  if '(' in str_2: str_2.remove('(')
  if ')' in str_2: str_2.remove(')')
  if '.' in str_2: str_2.remove('.')
  if ',' in str_2: str_2.remove(',')

str_1 = ''.join(x for x in str_1)
str_2 = ''.join(x for x in str_2)

dict_1 = {}
str_1 = str_1.split(' ')

dict_2 = {}
str_2 = str_2.split(' ')

for x in str_1:
  if x in dict_1:
    dict_1[x] += 1
  else:
    dict_1[x] = 1

for x in str_2:
  if x in dict_2:
    dict_2[x] += 1
  else:
    dict_2[x] = 1


result_1 = []
result_2 = []

for x, y in dict_1.items():
  result_1.append((x, y))

for x, y in dict_2.items():
  result_2.append((x, y))

print(result_1)
print(result_2)

plus_result = []

for x, y in dict_1.items():
  if x in dict_2:
    plus_result.append((x, dict_2[x] + dict_1[x]))
  else:
    plus_result.append((x, y))

for x, y in dict_2.items():
  if x not in dict_1:
    plus_result.append((x, y))

print(plus_result)

minus_result = []

for x, y in dict_1.items():
  if x in dict_2:
    if y > dict_2[x]:
      minus_result.append((x, y - dict_2[x]))
    else:
      pass
  else:
    minus_result.append((x, y))

print(minus_result)