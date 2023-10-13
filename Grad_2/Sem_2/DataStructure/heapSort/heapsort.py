# @copyright 한국기술교육대학교 컴퓨터공학부 자료구조및실습
# @version 2022년도 2학기
# @author 김상진
# 힙정렬

def reheapDown(heap, index, size, cmp):
	while index < size:
		leftidx = 2*index + 1
		rightidx = leftidx + 1
		if leftidx >= size: return
		maxChildIdx = leftidx
		if rightidx < size and cmp(heap[rightidx], heap[leftidx]):
			maxChildIdx = rightidx
		if cmp(heap[maxChildIdx], heap[index]):
			temp = heap[maxChildIdx]
			heap[maxChildIdx] = heap[index]
			heap[index] = temp
		else: return
		index = maxChildIdx

# 주어진 리스트를 이진힙으로 바꾸기 O(n)
def heapify(array, cmp) -> None:

	def check(array, cmp):
		result = True
		for i in range(len(array)):
			if 2*i + 2 >= len(array): break
			if not cmp(array[i], array[2*i + 1]) or not cmp(array[i], array[2*i + 2]):
				result = False
				break
		return result

	while not check(array, cmp):

		for i in range(len(array)):
			reheapDown(array, i, len(array), cmp)
		# print(array)

# 이진 힙을 정렬된 상태로 바꾸기
def reorder(array, cmp) -> None:

	def check(array, cmp):
		result = True
		for j in range(len(array) - 1):
			if not cmp(array[j], array[j + 1]):
				result = False
				array[j], array[j + 1] = array[j + 1], array[j]
				break
		return result

	while not check(array, cmp):

		for b in range(len(array)):
			# print("check_")
			reheapDown(array, b, len(array), cmp)
		

# 단계 1. 기존 배열을 이진힙 특성을 갖도록 재배치: 비용 O(n)
# 단계 2. 가장 큰 값을 맨 뒤로 이동한 후 이 값을 제외하고 이진힙 다시 구성 O(n log n)
def heapsort(array, cmp=lambda x,y: x<y):
	heapify(array, cmp)
	reorder(array, cmp)

nums = [1,5,2,9,4,6,8,3,7]
heapsort(nums, cmp=lambda x, y: x < y)