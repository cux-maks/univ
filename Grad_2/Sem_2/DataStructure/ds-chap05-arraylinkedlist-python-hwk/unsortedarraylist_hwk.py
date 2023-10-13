# @copyright 한국기술교육대학교 컴퓨터공학부 자료구조및실습
# @version 2022년도 2학기
# @author 김상진
# @file unsortedarraylist.py
# 중복 허용, 동적 배열 기반 단일 연결구조를 이용한 비정렬 정수 리스트
# 두 개의 포인터를 이용하여 popBack, remove 연산 구현
# head와 tail 유지, 코드 중복 제거
from typing import List, Union
from collections.abc import Iterator

class Node:
	def __init__(self, item: int=0, next: int=-1) -> None:
		self.item = item
		self.next = next
	def __repr__(self) -> str:
		return f'({self.item}, {self.next})'

class UnsortedArrayLinkedList:
	
	def __init__(self, *initList: int, capacity: int = 10) -> None:
		self.numItems: int = 0
		self.head: int = -1
		self.tail: int = -1
		self.free: int = 0
		self.capacity: int = 0
		self.nodes: List[Node] = []

		values: List[int] = initList[0] \
			if len(initList) == 1 and isinstance(initList[0], list) \
			else list(initList)
		if len(values)!=0:
			self.numItems = self.capacity = len(values)
			self.free = -1
			self.head = 0
			for i, n in enumerate(values):
				self.nodes.append(Node(n, i+1))
			self.nodes[self.numItems-1].next = -1
			self.tail = self.numItems-1
		if self.capacity<capacity:
			self.free = self.capacity
			j: int = self.free
			for i in range(capacity-self.capacity):
				self.nodes.append(Node(-1,j+1))
				j += 1
			self.capacity = capacity
			self.nodes[self.capacity-1].next = -1

	def __len__(self) -> int:
		return self.numItems

	def isFull(self) -> bool:
		return False

	def clear(self) -> None:
		for i in range(self.capacity):
			self.nodes[i].next = i+1
		self.nodes[self.capacity-1].next = -1
		self.head = self.tail = -1
		self.free = self.numItems = 0

	def increaseCapacity(self):
		self.free = self.capacity
		nextIdx: int = self.free+1
		for i in range(self.capacity):
			self.nodes.append(Node(-1,nextIdx))
			nextIdx += 1
		self.capacity *= 2
		self.nodes[self.capacity-1].next = -1

	def _getNodeIndex(self, index: int):
		curr: int = self.head
		for i in range(index):
			curr = self.nodes[curr].next
		return curr

	def _toList(self) -> List[int]:
		ret: List[int] = []
		curr: int = self.head
		while curr!=-1: 
			ret.append(self.nodes[curr].item)
			curr = self.nodes[curr].next
		return ret

	def __getitem__(self, index):
		if isinstance(index, int):
			if abs(index)<self.numItems:
				loc = self._getNodeIndex(index) if index>=0 \
					else self._getNodeIndex(self.numItems + index)
				return self.nodes[loc].item
			else: raise IndexError('index out of range')
		elif isinstance(index, slice):
			return self._toList()[index]
		else: 
			raise TypeError('Index must be int, not {}'.format(type(index).__name__))
	
	def __setitem__(self, index, item):
		if isinstance(index, int):
			if abs(index)<self.numItems:
				loc = self._getNodeIndex(index) if index>=0 \
					else self._getNodeIndex(self.numItems + index)
				self.nodes[loc].item = item
			else: raise IndexError('index out of range')
		elif isinstance(index, slice):
			tmp = self._toList()
			tmp[index] = item
			self.clear()
			for n in tmp: self.pushback(n)
		else: 
			raise TypeError('Index must be int, not {}'.format(type(index).__name__))
	
	def pushback(self, item: int) -> None:
		if self.numItems==self.capacity: self.increaseCapacity()
		if self.numItems==0:
			self.pushfront(item)
		else:
			newNodeIdx: int = self.free
			self.free = self.nodes[self.free].next
			self.nodes[newNodeIdx].item = item
			self.nodes[newNodeIdx].next = -1

			self.nodes[self.tail].next = newNodeIdx
			self.tail = newNodeIdx
			self.numItems += 1
	
	def _pushNodeToFreeList(self, index: int):
		self.nodes[index].next = self.free
		self.free = index
		self.numItems -= 1

	def popback(self) -> int:
		if not self: raise RuntimeError('popback: list is empty')
		prev: int = -1
		curr: int = self.head
		while self.nodes[curr].next!=-1:
			prev = curr
			curr = self.nodes[curr].next
		ret = self.nodes[self.tail].item
		self._pushNodeToFreeList(curr)

		if prev!=-1: 
			self.nodes[prev].next = -1
			self.tail = prev
		else: self.head = -1
		
		return ret
	
	def pushfront(self, item: int) -> None:
		if self.numItems==self.capacity: self.increaseCapacity()
		newNodeIdx: int = self.free
		self.free = self.nodes[self.free].next
		self.nodes[newNodeIdx].item = item
		self.nodes[newNodeIdx].next = self.head

		if self.head==-1: self.tail = newNodeIdx
		self.head = newNodeIdx
		self.numItems += 1
	
	def popfront(self) -> int:
		if not self: raise RuntimeError('popfront: list is empty')
		frontIdx: int = self.head
		ret: int = self.nodes[self.head].item
		self.head = self.nodes[self.head].next
		self._pushNodeToFreeList(frontIdx)
		if self.head==-1: self.tail = -1
		return ret

	def peekfront(self) -> int:
		if not self: raise RuntimeError('peekfront: list is empty')
		return self.nodes[self.head].item

	def peekback(self) -> int:
		if not self: raise RuntimeError('peekback: list is empty')
		return self.nodes[self.tail].item

	def __contains__(self, key: int) -> bool:
		curr: int = self.head
		while curr!=-1:
			if self.nodes[curr].item==key: return True
			curr = self.nodes[curr].next
		return False

	def removeNode(self, prev: int, curr: int) -> None:
		if curr==self.tail:
			self.tail = -1 if curr==self.head else prev
		if prev==-1: self.head = self.nodes[curr].next
		else: self.nodes[prev].next = self.nodes[curr].next
		self._pushNodeToFreeList(curr)

	def removeFirst(self, item: int) -> None:
		if not self: return
		prev: int = -1
		curr: int = self.head
		while curr!=-1:
			if self.nodes[curr].item==item: 
				self.removeNode(prev, curr)
				break
			prev = curr
			curr = self.nodes[curr].next

	def removeAll(self, item: int) -> None:
		if not self: return
		prev: int = -1
		curr: int = self.head
		while curr!=-1:
			if self.nodes[curr].item==item: 
				nextIdx = self.nodes[curr].next
				self.removeNode(prev, curr)
				curr = nextIdx
			else:
				prev = curr
				curr = self.nodes[curr].next

	def removeRange(self, fromIdx: int, toIdx: int) -> None:
		if fromIdx < 0 or fromIdx >= toIdx or fromIdx >= self.numItems: 
			raise IndexError('')
		dummy = Node(-1, self.head)
		prev = dummy
		curr = self.head
		for i in range(fromIdx):
			prev = curr
			curr = curr.next
		if toIdx == self.numItems:
			self.numItems = fromIdx
			prev.next = None
			self.tail = None if self.numItems==0 else prev
		else:
			for i in range(fromIdx, toIdx): curr = curr.next
			self.numItems -= toIdx-fromIdx
			prev.next = curr
		self.head = dummy.next

	def partition(self, item: int) -> None:
		if self.numItems == 0: return
		right = None
		left = None
		curr = self.head
		while curr:
			if curr.item < item:
				if left:
					left.next = curr
					left = curr
				else: self.head = left = curr
			else:
				if right: 
					self.tail.next = curr
					self.tail = curr
				else: self.tail = right = curr
			curr = curr.next
		self.tail.next = None
		if left: left.next = right
		else: self.head = right

	def __iter__(self) -> Iterator:
		self.it = self.head
		return self
	
	def __next__(self) -> int:
		if self.it == -1: raise StopIteration
		ret = self.nodes[self.it].item
		self.it = self.nodes[self.it].next
		return ret

	def print_me(self):
		for _ in range(self.numItems): print(self.nodes[_].item, end = ' ')