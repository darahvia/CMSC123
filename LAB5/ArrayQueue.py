class Element:
	# Insert the 'Element' class you created in Lab2, since they should be the same
	def __init__(self, value, index = 0):
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
		self.size = 0 				# The 'size' attribute must not exceed the 'capacity'		
		self.capacity = capacity
		self.DEFAULT_EXPANSION = 5
		
	def getSize(self):
		return self.size

	def getCapacity(self):
		return self.capacity

	def isEmpty(self):
		return (self.size == 0)

	def expand(self):
		self.capacity += self.DEFAULT_EXPANSION

class ArrayQueue(Array):
	def front(self):
		if self.isEmpty():
			return Element(None)
		return self.contents[0]				#return reference to the first element(front of the queue)


	def enqueue(self, value):
		if (self.size < self.capacity):
			newElement = Element(value, self.size)
			self.contents  += [newElement]
			self.size += 1
			return
		else:
			raise Exception		#exceeds the capcaity


	def dequeue(self):
		if self.isEmpty():
			raise Exception
		else:
			dequeuedElement = self.contents[0]				#store the first element to dequeuedElement
			for i in range(1, self.size):
				self.contents[i - 1] = self.contents[i]		#shift the elements to the left
			self.size -= 1
			return dequeuedElement
			

