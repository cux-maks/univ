# @copyright 한국기술교육대학교 컴퓨터공학부 자료구조및실습
# @version 2022년도 2학기
# @author 김상진
# @file unsortedlinkedlist.py
# 중복 허용, 단일 연결구조를 이용한 비정렬 리스트
# head만 유지, 해싱 구현을 위한 최소 연산만 포함
from typing import List, Union
from collections.abc import Iterator

class Node:
	def __init__(self, item: int=0, next = None):
		self.item = item
		self.next = next

class SingleLinkedList:
	
	def __init__(self) -> None:
		self.clear()

	def __len__(self) -> int:
		return self.numItems

	def clear(self) -> None:
		self.numItems = 0
		self.head = None
	
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

	def remove(self, item: int) -> bool:
		dummy = Node(None, self.head)
		prev = dummy
		curr = self.head
		while curr:
			if curr.item == item:
				self._removeNode(prev, curr)
				self.head = dummy.next
				return True;
			prev = curr
			curr = curr.next
		return False

	def __iter__(self) -> Iterator:
		self.it = self.head
		return self
	
	def __next__(self) -> int:
		if not self.it: raise StopIteration
		ret = self.it.item
		self.it = self.it.next
		return ret