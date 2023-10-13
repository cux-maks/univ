# @copyright 한국기술교육대학교 컴퓨터공학부 자료구조및실습
# @version 2022년도 2학기
# @author 김상진
# @file unsortedlist01.h
# 중복 허용, 단일 연결구조를 이용한 비정렬 정수 리스트
# 두 개의 포인터를 이용하여 popBack, remove 연산 구현
# head만 유지, dummy 노드 사용, 코드 중복 제거
from typing import List, Union
from collections.abc import Iterator

class Node:
	def __init__(self, item: int=0, next = None):
		self.item = item
		self.next = next

class SingleUnsortedLinkedList:
	
	def __init__(self, *initList: int) -> None:
		values: List[int] = initList[0] \
			if len(initList) == 1 and isinstance(initList[0], list) \
			else list(initList)
		self.numItems: int = 0
		self.head = None
		if len(values)!=0: self._fromList(values)

	def __len__(self) -> int:
		return self.numItems

	def isFull(self) -> bool:
		return False

	def clear(self) -> None:
		self.numItems = 0
		self.head = None

	def _getNode(self, index: int):
		curr = self.head
		for i in range(index):
			curr = curr.next
		return curr

	def _getTail(self):
		return self._getNode(self.numItems-1)

	def _toList(self) -> List[int]:
		ret: List[int] = []
		curr = self.head
		for i in range(self.numItems):
			ret.append(curr.item)
			curr = curr.next
		return ret

	def _fromList(self, itemList: List[int]) -> None:
		self.numItems = len(itemList)
		self.head = None
		if len(itemList)!=0:
			self.head = curr = Node(itemList[0])
			for item in itemList[1:]:
				newNode = Node(item)
				curr.next = newNode
				curr = newNode

	def __getitem__(self, index: Union[int, slice]) -> Union[int, List[int]]:
		if isinstance(index, int):
			if abs(index)<self.numItems:
				node = self._getNode(index) if index>=0 \
					else self._getNode(self.numItems + index)
				return node.item
			else: raise IndexError('index out of range')
		elif isinstance(index, slice):
			return self._toList()[index]
		else: 
			raise TypeError('Index must be int or slice, not {}'.format(type(index).__name__))
	
	def __setitem__(self, index: Union[int, slice], item) -> None:
		if isinstance(index, int):
			if abs(index)<self.numItems:
				node = self._getNode(index) if index>=0 \
					else self._getNode(self.numItems + index)
				node.item = item
			else: raise IndexError('index out of range')
		elif isinstance(index, slice):
			tmp = self._toList()
			tmp[index] = item
			self._fromList(tmp)
		else: 
			raise TypeError('Index must be int, not {}'.format(type(index).__name__))
	
	def pushback(self, item: int) -> None:
		newNode = Node(item)
		if self: self._getTail().next = newNode
		else: self.head = newNode
		self.numItems += 1  
	
	def popback(self) -> int:
		if not self: raise RuntimeError('popback: list is empty')
		dummy = Node(-1, self.head)
		cnt = self.numItems
		curr = self.head
		while cnt - 1:
			curr = curr.next
			cnt -= 1
		curr.next = None
		self.head = dummy.next 
		self.numItems -= 1
		return curr.item 

	def peekback(self) -> int:
		if not self: raise RuntimeError('peekback: list is empty')
		return self._getTail().item	
	
	def pushfront(self, item: int) -> None:
		newNode = Node(item, self.head)
		self.head = newNode
		self.numItems += 1
	
	def popFront(self) -> int:
		if not self: raise RuntimeError('popfront: list is empty')
		ret = self.head.item
		self.head = self.head.next
		self.numItems -= 1
		return ret 

	def peekfront(self) -> int:
		if not self: raise RuntimeError('peekfront: list is empty')
		return self.head.item

	def __contains__(self, item: int) -> bool:
		curr = self.head
		while curr:
			if curr.item == item: return True
			curr = curr.next
		return False

	def _removeNode(self, prev, curr) -> None:
		prev.next = curr.next
		self.numItems -= 1

	def _removeNowNode(self, now) -> None:
		dummy = Node(-1, self.head)
		prev = dummy
		curr = self.head
		while curr:
			if curr == now:
				self._removeNode(prev, curr)
				self.head = dummy.next
				break
			prev = curr
			curr = curr.next

	def removeFirst(self, item: int) -> None:

		now = self.head

		while True:
			if now.item == item:
				self._removeNowNode(now)
				break
			now = now.next

	def removeAll(self, item: int) -> None:
		
		now = self.head

		while now:
			if now.item == item: self._removeNowNode(now)
			now = now.next

	def __iter__(self) -> Iterator:
		self.it = self.head
		return self
	
	def __next__(self) -> int:
		if not self.it: raise StopIteration
		ret = self.it.item
		self.it = self.it.next
		return ret