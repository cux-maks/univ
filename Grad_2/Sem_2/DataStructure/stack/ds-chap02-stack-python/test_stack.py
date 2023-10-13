import unittest
from stack import Stack
from student import Student

class TestStack(unittest.TestCase):

	def test_init01(self):
		S = Stack()
		self.assertFalse(S)
		L = [3,5,7]
		for n in L:
			S.push(n)
		O = []
		while S:
			O.append(S.pop())
		O.reverse()
		self.assertListEqual(L, O)

	def test_init02(self):
		S = Stack()
		self.assertFalse(S)
		L = [Student('홍길동','202201',1),Student('성춘향','202101',2),Student('임꺽정','202202',1),Student('이몽룡','202102',2)]
		for s in L:
			S.push(s)
		O = []
		while S:
			O.append(S.pop())
		O.reverse()
		self.assertListEqual(L, O)

	def test_init03(self):
		S = Stack()
		L = [Student('홍길동','202201',1),Student('성춘향','202101',2),Student('임꺽정','202202',1),Student('이몽룡','202102',2)]
		for s in L:
			S.push(s)
		S.push(1)

	def test_init04(self):
		S = Stack(capacity=10)
		self.assertEqual(S.capacity, 10)
		self.assertFalse(S)
		L = [3,5,7,8,9]
		for n in L:
			S.push(n)
		O = []
		while S:
			O.append(S.pop())
		O.reverse()
		self.assertListEqual(L, O)	

	def test_init05(self):
		S = Stack(3,5,7,8,9)
		self.assertEqual(S.capacity, 5)
		self.assertEqual(len(S), 5)
		L = [9,8,7,5,3]
		O = []
		while S:
			O.append(S.pop())
		self.assertListEqual(L, O)	

	def test_init06(self):
		S = Stack(3,5,7,8,9, capacity=10)
		self.assertEqual(S.capacity, 10)
		self.assertEqual(len(S), 5)
		L = [9,8,7,5,3]
		O = []
		while S:
			O.append(S.pop())
		self.assertListEqual(L, O)	

	def test_init07(self):
		S = Stack([3,5,7,8,9], capacity=10)
		self.assertEqual(S.capacity, 10)
		self.assertEqual(len(S), 5)
		L = [9,8,7,5,3]
		O = []
		while S:
			O.append(S.pop())
		self.assertListEqual(L, O)	

	def test_init08(self):
		S = Stack(7, capacity=10)
		self.assertEqual(S.capacity, 10)
		self.assertEqual(len(S), 1)
		L = [7]
		O = []
		while S:
			O.append(S.pop())
		self.assertListEqual(L, O)					

	def test_iterator(self):
		S = Stack()
		L = [3,5,7,2,4,6,8]
		for n in L:
			S.push(n)
		O = []
		for n in S:
			O.append(n)
		O.reverse()
		self.assertListEqual(L, O)


unittest.main()