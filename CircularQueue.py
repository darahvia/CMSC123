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
		self.contents = [None]*self.capacity
		self.DEFAULT_EXPANSION = 5
		self.frontIndex = Element(None)
		self.rearIndex = Element(None)
		
	def getSize(self):
		return self.frontIndex - self.rearIndex
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
		for i in range (0, self.getSize):
			self.contents[i] = self.contents[self.frontIndex.geIndex()]
		# The wrapAround() operation resets the Array back where head is at index 0
		# Note: You will only use this function when capacity is full and you wish to enqueue()
		# REQUIRED

class CircularQueue(Array):
	# Note that class "CircularQueue" inherits the class "Array" attributes and methods

	def front(self):
		# The front() operation returns a reference value to the front element of the queue, but doesn’t remove it
		# REQUIRED\
		return self.frontIndex.getValue()

	def enqueue(self, value):
		newElement = Element(value)
		if self.size < self.capacity:
			self.contents += [newElement]
		else:
			self.rearIndex = 
		# The enqueue() operation inserts an element at the end of the queue
		# If the capacity is full, you are not allowed to enqueue() an element to the queue
		# REQUIRED

	def dequeue(self):
		# The dequeue() operation removes the element at the front of the queue
		# This should also return the 'Element' that was removed
		# REQUIRED