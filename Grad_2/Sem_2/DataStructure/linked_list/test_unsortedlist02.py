import unittest
from unsortedlist02 import SingleUnsortedLinkedList

class TestUnsortedList(unittest.TestCase):

	def test_listinit(self):
		L = SingleUnsortedLinkedList()
		self.assertTrue(not L)
		self.assertFalse(L.isFull())

	def test_pushpop_back(self):
		L = SingleUnsortedLinkedList()
		L.pushback(3)
		L.pushback(5)
		L.pushback(7)
		L.pushback(3)
		self.assertEqual(len(L),4)
		output = []
		while L:
			output.append(L.popback())
		self.assertListEqual(output,[3,7,5,3])

		L = SingleUnsortedLinkedList()
		self.assertRaises(RuntimeError, L.popback)
		L.pushback(1)
		L.pushback(2)
		L.pushback(3)
		L.pushback(4)
		L.pushback(5)
		L.pushback(6)
		L.pushback(7)
		L.pushback(8)
		L.pushback(9)
		L.pushback(10)

	def test_pushpop_front(self):
		L = SingleUnsortedLinkedList()
		L.pushfront(3)
		L.pushfront(5)
		L.pushfront(7)
		L.pushfront(3)
		L.pushfront(7)
		self.assertEqual(len(L),5)
		output = []
		while L:
			output.append(L.popFront())
		self.assertListEqual(output,[7,3,7,5,3])
	
	def test_initList(self):
		L = SingleUnsortedLinkedList(1,2,3,4,5,6)
		self.assertEqual(len(L),6)
		self.assertEqual(L.peekfront(),1)
		self.assertEqual(L.peekback(),6)

		L = SingleUnsortedLinkedList([1,2,3,4,5,6,7,8,9,10])
		self.assertEqual(len(L),10)
		self.assertEqual(L.peekfront(),1)
		self.assertEqual(L.peekback(),10)

		L = SingleUnsortedLinkedList(1,2,3,4,5,6,7,8,9,10,11,12,13)
		self.assertEqual(len(L),13)
		self.assertEqual(L.peekfront(),1)
		self.assertEqual(L.peekback(),13)

	def test_find(self):
		L = SingleUnsortedLinkedList(3,3,5,7,9)
		self.assertTrue(3 in L)
		self.assertTrue(5 in L)
		self.assertTrue(7 in L)
		self.assertTrue(9 in L)
		self.assertFalse(1 in L)
		self.assertFalse(4 in L)
		self.assertFalse(6 in L)
		self.assertFalse(8 in L)
		self.assertFalse(11 in L)

	def test_removeFirst(self):
		L = SingleUnsortedLinkedList(3,5,7)
		L.removeFirst(3)
		self.assertEqual(len(L),2)
		self.assertEqual(L.peekfront(), 5)
		L.removeFirst(7)
		self.assertEqual(len(L),1)
		self.assertEqual(L.peekback(), 5)
		L.removeFirst(5)
		self.assertTrue(not L)
		L = SingleUnsortedLinkedList(3,5,7)
		L.removeFirst(5)
		self.assertEqual(len(L),2)
		self.assertEqual(L.peekfront(), 3)
		self.assertEqual(L.peekback(), 7)
		
	def test_removeAll(self):
		L = SingleUnsortedLinkedList(1,3,1,1,3,4,5,4,4,6)
		L.removeAll(3)
		self.assertFalse(3 in L)
		self.assertEqual(len(L),8)
		self.assertEqual(L.peekfront(), 1)
		self.assertEqual(L.peekback(), 6)
		L.removeAll(1)
		self.assertFalse(1 in L)
		self.assertEqual(len(L),5)
		self.assertEqual(L.peekfront(), 4)
		self.assertEqual(L.peekback(), 6)
		L.removeAll(5)
		self.assertEqual(len(L),4)
		self.assertFalse(5 in L)
		L.removeAll(4)
		self.assertEqual(len(L),1)
		self.assertFalse(4 in L)
		L.popback()
		L.pushback(3)
		L.pushfront(3)
		L.pushfront(3)
		self.assertEqual(len(L),3)
		L.removeAll(3)
		self.assertTrue(not L)

	def test_clear(self):
		L = SingleUnsortedLinkedList([1,3,4,1,2,6,8])
		self.assertEqual(len(L),7)
		L.clear()
		self.assertTrue(not L)
		L.pushback(4)
		self.assertEqual(len(L),1)
		self.assertEqual(L.peekback(),4)

	def test_iterator(self):
		L = SingleUnsortedLinkedList(1,3,1,1,3,4,5,4,4,6)
		output = [x for x in L]
		self.assertEqual(output, [1,3,1,1,3,4,5,4,4,6])

	#@unittest.skip
	def test_getitem01(self):
		L = SingleUnsortedLinkedList(1,2,3,4,5,6,7,8,9,10)
		self.assertEqual(L[2],3)
		self.assertEqual(L[-1],10)
		self.assertListEqual(L[:3],[1,2,3])
		self.assertListEqual(L[-2:],[9,10])
		self.assertListEqual(L[4::-1],[5,4,3,2,1])
		self.assertListEqual(L[-6:-3],[5,6,7])
		self.assertListEqual(L[:-5],[1,2,3,4,5])

	#@unittest.skip
	def test_getitem02(self):
		L = SingleUnsortedLinkedList(1,2,3,4,5)
		self.assertEqual(L[2],3)
		self.assertEqual(L[-1],5)
		self.assertListEqual(L[:3],[1,2,3])
		self.assertListEqual(L[-2:],[4,5])
		self.assertListEqual(L[4::-1],[5,4,3,2,1])
		self.assertListEqual(L[-6:-3],[1,2])
		self.assertListEqual(L[:-3],[1,2])
		self.assertRaises(IndexError, L.__getitem__, 5)
	
	#@unittest.skip
	def test_setitem(self):	
		L = SingleUnsortedLinkedList(1,2,3,4,5,6,7,8,9,10)
		L[5] = 0
		output = [x for x in L]
		self.assertListEqual(output, [1,2,3,4,5,0,7,8,9,10])
		L[5] = 6
		L[:5] = [0,0,0,0,0]
		output = [x for x in L]
		self.assertListEqual(output, [0,0,0,0,0,6,7,8,9,10])
		L[-5:] = [0,0,0,0,0]
		output = [x for x in L]
		self.assertListEqual(output, [0,0,0,0,0,0,0,0,0,0])
		L[0::2] = [1,2,3,4,5]
		output = [x for x in L]
		self.assertListEqual(output, [1,0,2,0,3,0,4,0,5,0])
		L[1:3] = [1]
		L.pushback(1)
		output = [x for x in L]
		self.assertListEqual(output, [1,1,0,3,0,4,0,5,0,1])
		self.assertEqual(len(L), 10)
		L[1:3] = [2,2,2]
		output = [x for x in L]
		self.assertListEqual(output, [1,2,2,2,3,0,4,0,5,0,1])
		self.assertEqual(len(L), 11)

		self.assertRaises(TypeError, 'L[:2] = [1.2, 3.3]')


unittest.main()