class Element:
	# Insert the 'Element' class you created in Lab1, since they should be the same
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
		self.size = 0 				# The 'size' attribute must not exceed the 'capacity'		
		self.capacity = capacity
		self.contents = [None] * self.capacity
		self.DEFAULT_EXPANSION = 5
		self.frontIndex = 0
		self.rearIndex = 0
		
	def getSize(self):
		return self.size
		# returns the size of the queue
		# Note that the size is based on frontIndex and rearIndex
		# REQUIRED


	def getCapacity(self):
		return self.capacity
		# returns the capacity of the queue
		# REQUIRED


	def isEmpty(self):
		return (self.size == 0)
		# The isEmpty() operation returns true if the queue is empty and false if the queue is not empty
		# REQUIRED


	def expand(self):
		# The expand() operation increases the capacity when necessary
		self.capacity += self.DEFAULT_EXPANSION
		self.contents += ([None]*self.DEFAULT_EXPANSION)

	def wrapAround(self):
		newContents = [None] * self.capacity
		for i in range (self.capacity):
			self.contents[i] = self.contents[(self.frontIndex + i) % self.capacity]
		self.contents = newContents
		self.frontIndex = 0
		self.rearIndex = self.size - 1
		
		# The wrapAround() operation resets the Array back where head is at index 0
		# Note: You will only use this function when capacity is full and you wish to enqueue()
		# REQUIRED

class CircularQueue(Array):
	
	# Note that class "CircularQueue" inherits the class "Array" attributes and methods

	def front(self):
		# The front() operation returns a reference value to the front element of the queue, but doesn’t remove it
		# REQUIRED
		if self.isEmpty():
			return Element(None)
		else:
			return self.contents[self.frontIndex]

	def enqueue(self, value):

		# if self.isEmpty():
		# 	newElement = Element(value, self.rearIndex)
		# 	self.contents += [newElement]
		# 	self.size += 1


		if self.size < self.capacity:
			newElement = Element(value, self.rearIndex)
			self.contents[self.rearIndex] = newElement
			self.rearIndex = (self.rearIndex + 1) % self.capacity
			self.size += 1
			
		else:
			self.expand()
			self.wrapAround()
			self.enqueue(value)
			

		
		# The enqueue() operation inserts an element at the end of the queue
		# If the capacity is full, you are not allowed to enqueue() an element to the queue
		# REQUIRED
	def dequeue(self):
		if self.isEmpty():
			raise Exception
		else:
			dequeuedElement = self.contents[self.frontIndex]				#store the first element to dequeuedElement
			self.contents[self.frontIndex] = None
			self.frontIndex = (self.frontIndex + 1) % self.capacity
			self.size -= 1
			return dequeuedElement
	