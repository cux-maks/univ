'''
1) 주어진 임의의 사전에서 values를 기준으로 내림차순 key-value 쌍 5개, 오름차순 key-value 쌍 5개.
2) 주어진 임의의 사전에서 keys를 기준으로 사전에서 내림차순 key-value 쌍 5개, 오름차순 key-value 쌍 5개.
'''

import operator as op

prices = {
  'ABC': 89.23,
  'KIUP BANK': 100.54,
  'SHINHAN BANK': 38.48,
  'SAMSUNG': 201.78,
  'LG': 200.45,
  'APPLE': 167.85,
  'TOMATO': 134.78,
  'KAKAO': 162.51,
  'NC': 87.12,
  'NEXON': 56.02,
}

print("\n\n", prices, "\n\n", type(prices), "\n\n")

prices_key = sorted(prices.items(), key=op.itemgetter(0))
print("key sort 하위 5개: ", prices_key[0:5], type(prices_key))
prices_key = prices_key[::-1]
print("key sort 상위 5개: ", prices_key[0:5])

prices_value = sorted(prices.items(), key=op.itemgetter(1))
print("value sort 하위 5개: ", prices_value[0:5], type(prices_value))
prices_value = prices_value[::-1]
print("value sort 하위 5개: ", prices_value[0:5])