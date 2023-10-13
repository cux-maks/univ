import unittest
from hashing_lab_sol import HashTable

class TestHeap(unittest.TestCase):
	def test_add(self):
		fruits = ["peach","grape","orange","kiwi","mango",
			"tomato","melon","cherry","lemon","plum"]
		H = HashTable()
		for fruit in fruits:
			H.add(fruit)
		self.assertEqual(len(H), 10)
		H.add("mango")
		self.assertEqual(len(H), 10)
		for fruit in fruits:
			self.assertTrue(H.contains(fruit))
		#H.debugPrint()

	def test_remove(self):
		fruits = ["peach","grape","orange","kiwi","mango","melon","lemon"]
		H = HashTable()
		for fruit in fruits:
			H.add(fruit)
		self.assertEqual(len(H), 7)
		H.remove("peach")
		self.assertEqual(len(H), 6)
		H.remove("kiwi")
		self.assertEqual(len(H), 5)
		self.assertTrue(H.contains("melon"))
		H.remove("lemon")
		H.remove("peach")
		H.add("cherry")
		self.assertEqual(len(H), 5)
		#H.debugPrint()
		self.assertFalse(H.contains("kiwi"))
		self.assertFalse(H.contains("lemon"))
		self.assertFalse(H.contains("peach"))
		self.assertTrue(H.contains("orange"))

	
	def test_iterator(self):
		H = HashTable()
		fruits = ["apple","peach","grape","orange","mango","lemon","cherry"]
		test_set = set()
		for fruit in fruits:
			H.add(fruit)
			test_set.add(fruit)
		self.assertEqual(len(H), len(fruits))
		self.assertEqual(len(H), len(test_set))
		#H.debugPrint()
		count = 0
		for fruit in fruits:
			self.assertTrue(fruit in test_set)
			count += 1
		self.assertEqual(len(H), count)	


unittest.main()