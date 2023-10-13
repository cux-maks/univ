import unittest
from heapsort import heapsort

class TestPriorityQueue(unittest.TestCase):
	
	#@unittest.skip
	def test_heapsort01(self):
		nums = [1,5,2,9,4,6,8,3,7]
		expected = [1,2,3,4,5,6,7,8,9]
		heapsort(nums)
		self.assertEqual(nums, expected)
	
	#@unittest.skip
	def test_heapsort02(self):
		nums = [1,5,2,9,4,6,8,3,7]
		expected = [9,8,7,6,5,4,3,2,1]
		heapsort(nums,cmp=lambda x,y: x>y)
		self.assertEqual(nums, expected)	

unittest.main()