# @copyright 헌귝기술교육대학교 컴퓨터공학부 자료구조및실습
# @version 2022년도 2학기
# @author: 김상진
# hashing_lab.py
# chaining 기법, 동적 배열
from typing import List, Union
from collections import Iterator
from unsortedlinkedlist import SingleLinkedList

class HashTable:
	def __init__(self, capacity = 7):
		self.capacity = capacity
		self.numItems = 0
		self.table = [None]*self.capacity
		for i in range(capacity):
			self.table[i] = SingleLinkedList()
	
	def __len__(self):
		return self.numItems
	
	def _getKeyList(self):
		keyList = []
		for bucketList in self.table:
			for key in bucketList:
				keyList.append(key)
		return keyList

	def _increaseCapacity(self):
		keyList = self._getKeyList()
		self.capacity = self.capacity*2+1
		self.table = [None]*self.capacity
		for i in range(self.capacity):
			self.table[i] = SingleLinkedList()
		for key in keyList:
			index = self.hash(key)
			self.table[index].pushfront(key)

	def add(self, key: str):
		if self.contains(key): return
		index = self.hash(key)
		self.table[index].pushfront(key)
		self.numItems += 1
		if self.numItems/self.capacity>0.7 or len(self.table[index])>=3:
			self._increaseCapacity()
	
	def contains(self, key: str):
		if not self: return False
		index = self.hash(key)
		if len(self.table[index]) >= 3: self._increaseCapacity()
		return key in self.table[index]
	
	def remove(self, key: str):
		if not self: return
		index = self.hash(key)
		if self.table[index].remove(key):
			self.numItems -= 1
	
	def debugPrint(self):
		print('\nhash table: ')
		for i, keyList in enumerate(self.table):
			if len(keyList)>0: 
				output = [key for key in keyList]
				print(i,':', ", ".join(output))
			else: print(i,':')
	
	def hash(self, key) -> int:
		return key.__hash__() % self.capacity
	
	def __iter__(self):
		self.visited = 0
		self.cursor = 0
		self.it = None
		self._moveForward()
		return self

	def _moveForward(self):
		while self.cursor<self.capacity:
			if len(self.table[self.cursor])>0:
				self.cursor += 1
				self.it = self.table[self.cursor-1].__iter__()
				break
			self.cursor += 1

	def __next__(self):
		if self.visited>=self.numItems: raise StopIteration
		try:
			ret = self.it.__next__()
			self.visited += 1
			return ret
		except Exception as e:
			self._moveForward()
		return self.__next__()