# @copyright 한국기술교육대학교 컴퓨터공학부 자료구조및실습
# @version 2022년도 2학기
# @author 김상진 
# 이진 탐색 트리
# 부모 포인터를 유지함
# 최적화 및 모듈화 (findNode 중심)
# 가능한 모든 메소드를 재귀적으로 구현
from typing import List, Tuple, Callable, Optional
from collections.abc import Iterator
from enum import Enum

class Node:
	def __init__(self, key: int) -> None:
		self.key = key
		self.left = None
		self.right = None
		self.parent = None # 추가 

class TreeTraversal(Enum):
	INORDER=0
	PREORDER=1
	POSTORDER=2

class BST:
	def __init__(self, *initList: int) -> None:
		values: List[int] = initList[0] \
			if len(initList) == 1 and isinstance(initList[0], list) \
			else list(initList)
		self.clear()
		if values: 
			for key in values: self.add(key) 

	def __len__(self) -> int:
		#return self.numNodes
		return self._numberOfNodes(self.root)
	
	def _numberOfNodes(self, node: Node) -> int:
		if node is None: return 0
		return self._numberOfNodes(node.left)+self._numberOfNodes(node.right)+1
	
	def height(self) -> int:
		return self._computeHeight(self.root)
	
	def _computeHeight(self, node: Node) -> int:
		if node is None: return -1
		return max(self._computeHeight(node.left), self._computeHeight(node.right))+1
	
	def clear(self) -> None:
		self.root = None
		self.numNodes = 0
		self.traversalMethod = TreeTraversal.INORDER

	def add(self, key: int) -> None:
		newNode = Node(key)
		if not self: 
			self.root = newNode
		else:
			parent = self._findNode(self.root, key)
			if parent.key == key: return
			if parent.key > key: parent.left = newNode
			else: parent.right = newNode
			newNode.parent = parent # 추가
		self.numNodes += 1 

	def __contains__(self, key: int) -> bool:
		if not self: return False
		return self._findNode(self.root, key).key==key

	def _findNode(self, node: Node, key: int) -> Node: # 변경
		if node.key==key: return node
		nextNode = node.left if node.key>key else node.right
		return self._findNode(nextNode, key) if nextNode else node

	def remove(self, key: int) -> None:
		if not self: return
		delNode = self._findNode(self.root, key) # 변경
		if delNode.key!=key: return
		if delNode.left and delNode.right:
			prevNode = self._getLeftPredecessor(delNode)
			delNode.key = prevNode.key
			delNode = prevNode
		self._removeChild(delNode)
		self.numNodes -= 1

	# 변경
	def _removeChild(self, node: Node) -> None:
		grandChild = node.left if node.left else node.right
		parent = node.parent
		if parent:
			if parent.key >= node.key: parent.left = grandChild # 변경 > ==> >=
			else: parent.right = grandChild
		else:
			self.root = grandChild
		# 이 위치에 추가하여야 root의 parent 연결의 갱신도 처리됨
		if grandChild: grandChild.parent = parent # 추가

	def _getLeftPredecessor(self, node: Node) -> Node: # 변경
		node = node.left
		while node.right: node = node.right
		return node
	
	def _getRightSuccessor(self, node: Node) -> Node:
		node = node.right
		while node.left: node = node.left
		return node

	# 변경
	def _searchParents(self, node: Node, key: int, cmp: Callable[[int,int], bool]) -> Node:
		while node:
			if cmp(node.key, key): return node
			node = node.parent
		return None

	def getPrev(self, key: int) -> int:
		if not self: raise RuntimeError('BST is empty')
		foundNode = self._findNode(self.root, key) # 변경
		if foundNode.key != key: raise ValueError(f'{key} does not exists')
		prevNode = self._getPrevNode(foundNode, key) # 변경
		return prevNode.key if prevNode else key

	def _getPrevNode(self, node: Node, key: int) -> Node:
		if node and node.left:
			return self._getLeftPredecessor(node) # 변경
		else:
			prevNode = self._searchParents(node, key, lambda x,y: x<y) # 변경
			return prevNode if prevNode else None

	def getNext(self, key: int) -> int:
		if not self: raise RuntimeError('BST is empty')
		foundNode = self._findNode(self.root, key) # 변경
		if foundNode.key != key: raise ValueError(f'{key} does not exists')
		nextNode = self._getNextNode(foundNode, key) # 변경
		return nextNode.key if nextNode else key

	def _getNextNode(self, node: Node, key: int) -> Node:
		if node and node.right:
			return self._getRightSuccessor(node)
		else:
			nextNode = self._searchParents(node, key, lambda x,y: x>y) # 변경
			return nextNode if nextNode else None

	def rangeSearch(self, lo: int, hi: int) -> List[int]:
		if lo>hi: raise ValueError('Illegal argument')
		if not self: return []
		keys = []
		self._rangeSearch(self.root, lo, hi, keys)
		return keys

	def _rangeSearch(self, node: Node, lo: int, hi: int, visitedOrder: List[int]) -> None:
		if node.left and node.key>=lo:
			self._rangeSearch(node.left, lo, hi, visitedOrder)
		if node.key>=lo and node.key<=hi: visitedOrder.append(node.key)
		if node.right and node.key<=hi:
			self._rangeSearch(node.right, lo, hi, visitedOrder)

	def nearestNeighbors(self, key: int) -> Tuple[int, int]:
		node = self._findNode(self.root, key) # 변경
		prevNode = self._getPrevNode(node, key) # 변경
		nextNode = self._getNextNode(node, key) # 변경
		prevKey = prevNode.key if prevNode else None
		nextKey = nextNode.key if nextNode else None
		return prevKey, nextKey

	def balanceTree(self) -> None:
		keys: List[int] = []
		self.inorder(self.root, keys)
		self.clear()
		self._constructBalanceTree(keys,0,len(keys)-1)

	def _constructBalanceTree(self, keys: list, lo: int, hi: int) -> None:
		if lo==hi: self.add(keys[lo])
		elif lo+1==hi:
			self.add(keys[lo])
			self.add(keys[hi])
		else:
			mid = (lo+hi)//2
			self.add(keys[mid])
			self._constructBalanceTree(keys, lo, mid-1)
			self._constructBalanceTree(keys, mid+1, hi)

	def inorder(self, node: Node, visitedOrder: List[int]) -> None:
		if node.left: self.inorder(node.left, visitedOrder)
		visitedOrder.append(node.key)
		if node.right: self.inorder(node.right, visitedOrder)

	def preorder(self, node: Node, visitedOrder: List[int]) -> None:
		visitedOrder.append(node.key)
		if node.left: self.preorder(node.left, visitedOrder)
		if node.right: self.preorder(node.right, visitedOrder)
	
	def postorder(self, node: Node, visitedOrder: List[int]) -> None:
		if node.left: self.postorder(node.left, visitedOrder)
		if node.right: self.postorder(node.right, visitedOrder)
		visitedOrder.append(node.key)			

	def setIteratorType(self, traversalMethod: TreeTraversal) -> None:
		self.traversalMethod = traversalMethod

	def __iter__(self) -> Iterator:
		self.it: int = 0
		self.keys: List[int] = []
		if self.traversalMethod==TreeTraversal.INORDER:
			self.inorder(self.root, self.keys)
		elif self.traversalMethod==TreeTraversal.PREORDER:
			self.preorder(self.root, self.keys)
		else:
			self.postorder(self.root, self.keys)
		return self

	def __next__(self) -> int:
		if self.it>=self.numNodes: raise StopIteration
		self.it += 1
		return self.keys[self.it-1]
