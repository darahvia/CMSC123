
class Element:
	def __init__(self, value, index = None):
		self.value = value
		self.index = index

	def setValue(self,value):
		self.value = value

	def getValue(self):
		return self.value

	def getIndex(self):
		return self.index

class Array:
	def __init__(self, capacity=10):
		self.contents = []
		self.size = 0 					
		self.capacity = capacity
		self.DEFAULT_EXPANSION = 5

	def getCapacity(self):
		return self.capacity

	def isEmpty(self):
		return (self.size) == 0

	def expand(self):
		self.capacity += self.DEFAULT_EXPANSION

class ArrayStack(Array):


	def top(self):
		if not self.contents:
			return None
		return self.contents[-1]


	def push(self, value):
		if (self.size < self.capacity):
			newElement = Element(value, self.size)
			self.contents += [newElement]
			self.size += 1
			return
		else:
			raise ValueError		#array is full, cannot accept more elements

		
	def pop(self):
		poppedElement = self.contents[-1]
		self.contents = self.contents[:-1]
		self.size -= 1
		return poppedElement