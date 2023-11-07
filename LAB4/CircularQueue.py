class Element:

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
		self.size = 0 		
		self.capacity = capacity
		self.contents = [None] * self.capacity
		self.DEFAULT_EXPANSION = 5
		self.frontIndex = 0
		self.rearIndex = 0
		
	def getSize(self):
		return self.size

	def getCapacity(self):
		return self.capacity
	
	def isEmpty(self):
		return (self.size == 0)

	def expand(self):
		# The expand() operation increases the capacity when necessary
		self.capacity += self.DEFAULT_EXPANSION
		self.contents += ([None]*self.DEFAULT_EXPANSION)

	def wrapAround(self):
		for i in range (self.capacity):
			self.contents[i] = self.contents[(self.frontIndex + i) % self.capacity]		#reset the array by shifting
		self.frontIndex = 0				#update the front and rear index
		self.rearIndex = self.size									


class CircularQueue(Array):
	
	def front(self):
		if self.isEmpty():
			return Element(None)
		else:
			return self.contents[self.frontIndex]

	def enqueue(self, value):

		if self.size < self.capacity:
			newElement = Element(value, self.rearIndex)		
			self.contents[self.rearIndex] = newElement					#add the element
			self.rearIndex = (self.rearIndex + 1) % self.capacity		#update the rear element
			self.size += 1
			
		else:
			self.expand()												
			self.wrapAround()
			self.enqueue(value)											#call enqueue function after expand and wrap around
			
	def dequeue(self):
		if self.isEmpty():
			raise Exception												#EmptyQueueError
		else:
			dequeuedElement = self.contents[self.frontIndex]			
			self.contents[self.frontIndex] = None						#set the frontIndex to None
			self.frontIndex = (self.frontIndex + 1) % self.capacity 	#move the front index
			self.size -= 1									
			return dequeuedElement		
