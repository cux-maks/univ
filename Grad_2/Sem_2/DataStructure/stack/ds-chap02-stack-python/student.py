
class Student:
	def __init__(self, name, number, year):
		self.name = name
		self.number = number
		self.year = year

	def __repr__(self):
		return f'({self.name}, {self.number}, {self.year})'