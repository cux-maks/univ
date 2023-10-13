'''
주어진 임의의 정수 집합에서 크기 순으로 상위 5개 하위 5개를 알아내보자.
'''

import numpy as np

my_collection = list(np.random.randint(-50, 50, 100))
print(my_collection)

my_collection.sort()
my_collection_2 = my_collection[::-1]
print(my_collection_2[0:5:])
print(my_collection[0:5])