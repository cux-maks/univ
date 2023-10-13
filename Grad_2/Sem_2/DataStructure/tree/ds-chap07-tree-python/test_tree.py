# 한국기술교육대학교 컴퓨터공학부 자료구조및실습
# @version 2022년도 2학기
# @author 김상진
# 일반 트리구조 테스트 프로그램
import unittest
from tree import Node
from copy import deepcopy

class TestTree(unittest.TestCase):
	
	def test_add_remove(self):
		root = Node(0)
		node1 = Node(1)
		node2 = Node(2)
		root.addChild(node1)
		root.addChild(node2)
		node1.addChild(Node(4))
		node1.addChild(Node(5))
		#root.debugPrint(1)
		self.assertEqual(root.numOfChilds(),2)
		self.assertEqual(root.numOfChilds(),2)
		del node1[0]
		self.assertEqual(node1.numOfChilds(),1)
		self.assertEqual(node1[0].key,5)	

	def test_iteratoR(self):
		root = Node(1)
		node1 = Node(2)
		node2 = Node(3)
		root.addChild(node1)
		root.addChild(node2)
		node1.addChild(Node(4))
		node1.addChild(Node(5))
		output = [key for key in root]
		self.assertEqual(output, [1,2,3,4,5])
	
	# @unittest.skip
	def test_searchBFS(self):
		root = Node(1)
		node1 = Node(2)
		node2 = Node(3)
		root.addChild(node1)
		root.addChild(node2)
		node1.addChild(Node(4))
		node3 = Node(5)
		node1.addChild(node3)
		node3.addChild(Node(7))
		node3.addChild(Node(8))
		node2.addChild(Node(6))

		self.assertTrue(root.search_using_BFS(1))
		self.assertTrue(root.search_using_BFS(3))
		self.assertTrue(root.search_using_BFS(4))
		self.assertTrue(root.search_using_BFS(5))
		self.assertTrue(root.search_using_BFS(6))
		self.assertTrue(root.search_using_BFS(8))
		self.assertFalse(root.search_using_BFS(0))
		
	# @unittest.skip
	def test_searchDFS(self):
		root = Node(1)
		node1 = Node(2)
		node2 = Node(3)
		root.addChild(node1)
		root.addChild(node2)
		node1.addChild(Node(4))
		node3 = Node(5)
		node1.addChild(node3)
		node3.addChild(Node(7))
		node3.addChild(Node(8))
		node2.addChild(Node(6))

		self.assertTrue(root.search_using_DFS(1))
		self.assertTrue(root.search_using_DFS(3))
		self.assertTrue(root.search_using_DFS(4))
		self.assertTrue(root.search_using_DFS(5))
		self.assertTrue(root.search_using_DFS(6))
		self.assertTrue(root.search_using_DFS(8))
		self.assertFalse(root.search_using_DFS(0))
	
	# @unittest.skip
	def test_search_recursiveDFS(self):
		root = Node(1)
		node1 = Node(2)
		node2 = Node(3)
		root.addChild(node1)
		root.addChild(node2)
		node1.addChild(Node(4))
		node3 = Node(5)
		node1.addChild(node3)
		node3.addChild(Node(7))
		node3.addChild(Node(8))
		node2.addChild(Node(6))

		self.assertTrue(root.search_using_rescursiveDFS(1))
		self.assertTrue(root.search_using_rescursiveDFS(3))
		self.assertTrue(root.search_using_rescursiveDFS(4))
		self.assertTrue(root.search_using_rescursiveDFS(5))
		self.assertTrue(root.search_using_rescursiveDFS(6))
		self.assertTrue(root.search_using_rescursiveDFS(8))
		self.assertFalse(root.search_using_rescursiveDFS(0))

	def test_deepcopy(self):
		root1 = Node(0)
		node1 = Node(1)
		node2 = Node(2)
		root1.addChild(node1)
		root1.addChild(node2)
		node1.addChild(Node(4))
		node1.addChild(Node(5))
		root2 = deepcopy(root1)
		root2.addChild(Node(6))
		del node1[0]
		node2.addChild(Node(6))
		self.assertEqual(root1.numOfChilds(),2)
		self.assertEqual(root2.numOfChilds(),3)
		self.assertEqual(root1[0].numOfChilds(),1)
		self.assertEqual(root2[0].numOfChilds(),2)
		self.assertEqual(root1[0][0].key,5)
		self.assertEqual(root2[0][0].key,4)	
		self.assertEqual(root1[1].numOfChilds(),1)
		self.assertEqual(root2[1].numOfChilds(),0)

unittest.main()