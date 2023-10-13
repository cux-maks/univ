# @copyright 한국기술교육대학교 컴퓨터공학부 자료구조및실습
# @version 2022년도 2학기
# @author 김상진
# @file tree.py
# 일반 트리 노드: 자식 수의 제한이 없음
# 노드 레이블(값)은 정수로 가정

from collections import deque
from collections.abc import Iterator

class Node:
	def __init__(self, key: int) -> None:
		self.key: int = key
		self.childs = []

	def numOfChilds(self) -> int:
		return len(self.childs)
	
	def addChild(self, child) -> None:
		if child is not None:
			self.childs.append(child)

	def __getitem__(self, index):
		if isinstance(index, int):
			return self.childs[index]	
		else: 
			raise TypeError(f'Index must be int, not {type(index).__name__}')

	def __setitem__(self, index, key) -> None:
		if isinstance(index, int):
			self.childs[index].key = key	
		else: 
			raise TypeError(f'Index must be int, not {type(index).__name__}')

	def __delitem__(self, index) -> None:
		if isinstance(index, int):
			del self.childs[index]	
		else: 
			raise TypeError(f'Index must be int, not {type(index).__name__}')
	
	def search_using_BFS(self, key: int) -> bool:
		Q = deque()
		Q.append(self)
		while Q:
			curr = Q.popleft()
			if curr.key == key: return True
			for child in curr.childs:
				Q.append(child)
		return False
		'''
		visited = []
		queue = deque()
		queue.append(self.childs)
		if key == self.key: return True
		while queue:
			n = queue.popleft()
			for i in n:
				if i not in visited:
					queue.append(i.childs)
					visited.append(i)
				if i.key == key: return True
		return False
		'''

	def search_using_DFS(self, key: int) -> bool:
		S = []
		S.append(self)
		while S:
			curr = S.pop()
			if curr.key == key: return True
			for child in curr.childs:
				S.append(child)
		return False
		'''
		visited = []
		stack = []
		for x in self.childs: stack.append(x)
		if key == self.key: return True
		while stack:
			n = stack.pop()
			if n.key == key: return True
			if n not in visited:
				visited.append(n)
				for x in n.childs: stack.append(x)
		return False
		'''

	def search_using_recursiveDFS(self, key: int) -> bool:
		found = False
		def recursiveDFS(node, key: int):
			nonlocal found
			if node.key == key: 
				found = True
				return
			for child in node.childs:
				recursiveDFS(child, key)
		recursiveDFS(self, key)
		return found
		'''
		if key == self.key: return True
		if self.childs:
			for x in self.childs:
				x.search_using_rescursiveDFS(key)
		return False
		'''

	# BFS 기반 반복자
	def __iter__(self) -> Iterator:
		self.queue = deque()
		self.queue.append(self)
		return self
	
	def __next__(self) -> int:
		if not self.queue: raise StopIteration
		curr = self.queue.popleft()
		for child in curr.childs:
			self.queue.append(child)
		return curr.key
	
	def debugPrint(self, level: int) -> None:
		print(f'Node: {self.key}, childs:')
		for node in self.childs:
			print('\t'*level, end='')
			node.debugPrint(level+1)