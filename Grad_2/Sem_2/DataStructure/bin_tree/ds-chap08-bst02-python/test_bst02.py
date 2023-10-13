import unittest
from bst02 import BST, TreeTraversal

class TestBST(unittest.TestCase):

	# @unittest.skip
	def test_init(self):
		bst = BST()
		self.assertFalse(bst)
		self.assertEqual(bst.height(), -1)
		self.assertEqual(len(bst), 0)

	# @unittest.skip
	def test_add(self):
		bst = BST()
		bst.add(3)
		bst.add(5)
		bst.add(1)
		self.assertEqual(len(bst), 3)
		bst.setIteratorType(TreeTraversal.PREORDER)
		output = [x for x in bst]
		self.assertEqual(output, [3,1,5])

		bst.clear()
		bst.add(1)
		bst.add(3)
		bst.add(5)
		self.assertEqual(len(bst), 3)
		bst.setIteratorType(TreeTraversal.PREORDER)
		output = [x for x in bst]
		self.assertEqual(output, [1,3,5])

		bst.clear()
		bst.add(5)
		bst.add(3)
		bst.add(1)
		self.assertEqual(len(bst), 3)
		bst.setIteratorType(TreeTraversal.PREORDER)
		output = [x for x in bst]
		self.assertEqual(output, [5,3,1])

	# @unittest.skip
	def test_initList(self):
		bst = BST([4,1,3,6,5,2])
		self.assertEqual(len(bst), 6)
		output = [x for x in bst]
		self.assertEqual(output, [1,2,3,4,5,6]) 

	# @unittest.skip
	def test_heightTest(self):
		bst = BST()
		bst.add(1)
		bst.add(3)
		bst.add(5)
		self.assertEqual(bst.height(), 2)

		bst.clear()
		bst.add(7)
		bst.add(5)
		bst.add(3)
		bst.add(1)	
		self.assertEqual(bst.height(), 3)

		bst.clear()
		bst.add(5)
		bst.add(7)
		bst.add(3)
		bst.add(1)	
		self.assertEqual(bst.height(), 2)
		output = [x for x in bst]
		self.assertEqual(output, [1,3,5,7]) 

	# @unittest.skip
	def test_find(self):
		bst = BST([7,1,3,9,10,4,2])
		self.assertEqual(len(bst), 7)
		self.assertTrue(7 in bst)
		self.assertTrue(1 in bst)
		self.assertTrue(3 in bst)
		self.assertTrue(9 in bst)
		self.assertTrue(10 in bst)
		self.assertTrue(4 in bst)
		self.assertTrue(2 in bst)
		self.assertFalse(0 in bst)
		self.assertFalse(5 in bst)
		self.assertFalse(8 in bst)
		self.assertFalse(11 in bst)
		bst = BST()
		self.assertFalse(0 in bst)

	# @unittest.skip
	def test_traversal(self):
		bst = BST([60,45,63,41,55,65])
		bst.setIteratorType(TreeTraversal.PREORDER)
		output = [x for x in bst]
		self.assertEqual(output, [60,45,41,55,63,65])
		bst.setIteratorType(TreeTraversal.INORDER)
		output = [x for x in bst]
		self.assertEqual(output, [41,45,55,60,63,65])
		bst.setIteratorType(TreeTraversal.POSTORDER)
		output = [x for x in bst]
		self.assertEqual(output, [41,55,45,65,63,60])
		
		bst = BST([50,40,55,45,52,62,43,47,60,65])
		bst.setIteratorType(TreeTraversal.PREORDER)
		output = [x for x in bst]
		self.assertEqual(output, [50,40,45,43,47,55,52,62,60,65])
		bst.setIteratorType(TreeTraversal.INORDER)
		output = [x for x in bst]
		self.assertEqual(output, [40,43,45,47,50,52,55,60,62,65])
		bst.setIteratorType(TreeTraversal.POSTORDER)
		output = [x for x in bst]
		self.assertEqual(output, [43,47,45,40,52,60,65,62,55,50])

	# @unittest.skip
	def test_next(self):
		bst = BST(7,1,3,9,10,4,2,8)
		self.assertEqual(bst.getNext(3), 4)
		self.assertRaises(ValueError, bst.getNext, 6)
		self.assertEqual(bst.getNext(4), 7)
		self.assertEqual(bst.getNext(7), 8)
		self.assertEqual(bst.getNext(9), 10)
		self.assertEqual(bst.getNext(10), 10)
	
	# @unittest.skip
	def test_prev(self):
		bst = BST(7,1,3,9,10,4,2,8)
		self.assertEqual(bst.getPrev(3), 2)
		self.assertRaises(ValueError, bst.getPrev, 5)
		self.assertEqual(bst.getPrev(4), 3)
		self.assertEqual(bst.getPrev(7), 4)
		self.assertEqual(bst.getPrev(9), 8)
		self.assertEqual(bst.getPrev(1), 1)

	def test_remove(self):
		bst = BST(7,1,3,9,10,4,2,8)
		bst.remove(10)
		self.assertEqual(len(bst),7)
		bst.setIteratorType(TreeTraversal.PREORDER)
		output = [x for x in bst]
		self.assertEqual(output,[7,1,3,2,4,9,8])
		bst.remove(1)
		self.assertEqual(len(bst),6)
		output = [x for x in bst]
		self.assertEqual(output,[7,3,2,4,9,8])
		bst.remove(7)
		self.assertEqual(len(bst),5)
		output = [x for x in bst]
		self.assertEqual(output,[4,3,2,9,8])

	# @unittest.skip
	def test_rangeSearch(self):
		bst = BST(6,7,2,3,10,1,19,20)
		keys = bst.rangeSearch(4,19)
		self.assertEqual(keys,[6,7,10,19]) 
		keys = bst.rangeSearch(2,18)
		self.assertEqual(keys,[2,3,6,7,10])
		keys = bst.rangeSearch(2,10)
		self.assertEqual(keys,[2,3,6,7,10])
		keys = bst.rangeSearch(20,30)
		self.assertEqual(keys,[20])
		keys = bst.rangeSearch(-5,3)
		self.assertEqual(keys,[1,2,3])

	# @unittest.skip
	def test_nearestNeighbors(self):
		bst = BST(6,7,2,3,10,1,19,20)
		prevKey, nextKey = bst.nearestNeighbors(4)
		self.assertEqual(prevKey, 3)
		self.assertEqual(nextKey, 6)
		prevKey, nextKey = bst.nearestNeighbors(2)
		self.assertEqual(prevKey, 1)
		self.assertEqual(nextKey, 3)
		prevKey, nextKey = bst.nearestNeighbors(1)
		self.assertFalse(prevKey)
		self.assertEqual(nextKey, 2)
		prevKey, nextKey = bst.nearestNeighbors(20)
		self.assertEqual(prevKey, 19)
		self.assertFalse(nextKey)
		prevKey, nextKey = bst.nearestNeighbors(21)
		self.assertEqual(prevKey, 20)
		self.assertFalse(nextKey)
		prevKey, nextKey = bst.nearestNeighbors(-5)
		self.assertFalse(prevKey)
		self.assertEqual(nextKey, 1)

	# @unittest.skip
	def test_balanceTree(self):
		bst = BST(1,2,3,4,5,6,7)
		self.assertEqual(bst.height(),6)
		bst.balanceTree()
		self.assertEqual(bst.height(),2)
		
unittest.main()