# @copyright 한국기술교육대학교 컴퓨터공학부 자료구조및실습
# @version 2022년도 2학기
# @author 김상진
# 범용 스택 자료구조
from collections.abc import Iterator

class Stack:
	def __init__(self, *initList, capacity: int = 0):
		if capacity<0: raise ValueError('init: capacity<0')
		values = initList[0] if len(initList) == 1 and isinstance(initList[0], list) else list(initList)
		self.capacity = max(len(values), capacity)
		self.buf = [None]*self.capacity
		self.buf[:len(values)] = values
		self.top = len(values)
	
	def __len__(self) -> int:
		return self.top
	
	def peek(self):
		if not self: raise RuntimeError()
		return self.buf[self.top - 1]
	
	def pop(self):
		if not self: raise RuntimeError()
		return_Value = self.buf[self.top - 1]
		self.buf[self.top - 1] = None
		self.top -= 1
		return return_Value
	
	def push(self, item: int) -> None:
		if self.top == self.capacity: self.increaseCapacity()
		self.buf[self.top] = item
		self.top += 1
	
	def increaseCapacity(self) -> None:
		if self.capacity==0:
			self.capacity = 1
			self.buf = [None]
		else:
			self.buf += [None]*self.capacity
			self.capacity *= 2

	def __iter__(self) -> Iterator:
		return self.StackIterator(self.top-1, self.buf)

	class StackIterator:
		def __init__(self, startLoc: int, buf) -> None:
			self.it = startLoc
			self.buf = buf

		def __next__(self):
			if self.it<0: raise StopIteration
			self.it -= 1
			return self.buf[self.it+1]

	'''
	def __iter__(self):
		self.it = self.top-1
		return self
	
	def __next__(self):
		if self.it<0: raise StopIteration
		self.it -= 1
		return self.buf[self.it+1]
	'''