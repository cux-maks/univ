# @copyright 한국기술교육대학교 컴퓨터공학부 자료구조및실습
# @version 2022년도 2학기
# @author 김상진
# @file unsortedlist02.h
# 용량 고정, 중복 허용, 배열을 이용한 비정렬 정수 리스트
# 순서를 유지하는 방법으로 pushFront, popFront, remove를 구현함
# 코드 중복 제거
from re import I
from typing import List, Tuple, Union, Any, Optional
from collections.abc import Iterator

class UnsortedList:
	MAX = 10
	def __init__(self, *initList: int) -> None:
		values: List[int] = initList[0] \
			if len(initList) == 1 and isinstance(initList[0], list) \
			else list(initList)
		if len(values) > UnsortedList.MAX:
			values = values[:UnsortedList.MAX]
		self.numItems = min(UnsortedList.MAX, len(values))
		self.items: List[int] = [0]*UnsortedList.MAX
		self.items[:len(values)] = values
	
	def __len__(self) -> int:
		return self.numItems
	
	def isFull(self) -> bool:
		return self.numItems==UnsortedList.MAX
	
	def clear(self) -> None:
		self.numItems=0

	def __getitem__(self, index: Union[int, slice]) -> Union[int, List[int]]:
		if isinstance(index, int) or isinstance(index, slice):
			return self.items[:self.numItems][index]
		else: 
			raise TypeError('Index must be int or slice, not {}'.format(type(index).__name__))
	
	def _setitems(self, sliceInfo: slice, itemList: List[int]):
		self.items = self.items[:self.numItems]
		self.items[sliceInfo] = itemList
		self.numItems = len(self.items)
		if self.numItems > UnsortedList.MAX: 
			self.numItems = UnsortedList.MAX
			del self.items[self.numItems:]
		elif self.numItems < UnsortedList.MAX:
			self.items += [0]*(UnsortedList.MAX-self.numItems)

	def __setitem__(self, index: Union[int, slice], item) -> None:
		if isinstance(index, int):
			if abs(index)<self.numItems:
				self.items[index] = item
			else: raise IndexError('index out of range')
		elif isinstance(index, slice):
			self._setitems(index, item)
		else: 
			raise TypeError('Index must be int or slice, not {}'.format(type(index).__name__))
	
	# def pushback(self, item: int) -> None:
	# 	if self.isFull(): raise RuntimeError('pushback: list is full')
	# 	self.items[self.numItems] = item
	# 	self.numItems += 1
	
	def popback(self) -> int:
		if not self: raise RuntimeError('popback: list is empty')
		self.numItems -= 1
		return self.items[self.numItems]
	
	# def pushfront(self, item: int) -> None:
	# 	if self.isFull(): raise RuntimeError('pushfront: list is full')
	# 	for i in range(self.numItems,0,-1):
	# 		self.items[i] = self.items[i-1]
	# 	self.items[0] = item
	# 	self.numItems += 1

	def add(self, item: int) -> None:
		if self.isFull(): raise RuntimeError('pushback: list is full')
		self.items[self.numItems] = item
		a = sorted(self.items[0:self.numItems + 1])		
		for i in range(0, self.numItems + 1):
			self.items[i] = a[i]
		self.numItems += 1
	
	def popfront(self) -> int:
		if not self: raise RuntimeError('popback: list is empty')
		ret = self.items[0]
		self._shiftLeft(0)
		return ret
	
	def peekfront(self) -> int:
		if not self: raise RuntimeError('peekfront: list is empty')
		return self.items[0]
	
	def peekback(self) -> int:
		if not self: raise RuntimeError('peekback: list is empty')
		return self.items[self.numItems-1]

	def _search(self, item: int, startIdx: int = 0) -> Optional[int]:
		for i in range(startIdx, self.numItems):
			if self.items[i]==item: return i
		return None

	def search(self, item: int, startIdx: int = 0) -> Optional[int]:
		self.items.sort()
		start = startIdx
		end = self.numItems

		while start <= end:
			mid = (start + end) // 2
			if self.items[mid] == item:
				return mid
			elif self.items[mid] < item:
				start = mid + 1
			else:
				end = mid - 1

		return None

	def find(self, item: int, startIdx: int = 0) -> Optional[int]:
		if self.search(item) != None: return True
		return False

	def __contains__(self, item: int) -> bool:
		return self._search(item) is not None

	def _shiftLeft(self, itemLoc: int) -> None:
		for i in range(itemLoc, self.numItems-1):
			self.items[i] = self.items[i+1] 
		self.numItems -= 1

	def removeFirst(self, item: int) -> None:
		itemLoc = self._search(item)
		if itemLoc is not None: self._shiftLeft(itemLoc)
	
	def removeAll(self, item: int) -> None:
		itemLoc = self._search(item)
		while itemLoc is not None:
			self._shiftLeft(itemLoc)
			itemLoc = self._search(item, itemLoc)

	def __iter__(self) -> Iterator:
		self.it = 0
		return self
	
	def __next__(self) -> int:
		if self.it>=self.numItems: raise StopIteration
		self.it += 1
		return self.items[self.it-1]