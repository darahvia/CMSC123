class SLLNode:
	# Insert the 'SLLNode' class you created in Lab2, since they should be the same
	def __init__(self, value):
		self.value = value
		self.nextNode = None

	def setValue(self,value):
		self.value = value

	def getValue(self):
		return self.value
	
	def setNext(self,nextNode):
		self.nextNode = nextNode

	def getNext(self):
		return self.nextNode

class SLL:
	# Insert the 'SLL' class you created in Lab2, since they should be the same
	def __init__(self):
		self.size = 0
		self.frontNode = SLLNode(None)
		self.frontNode.setNext(SLLNode(None))

	def getSize(self):
		return self.size

	def isEmpty(self):
		return (self.size == 0)
		# The isEmpty() operation returns true if the queue is empty and false if the queue is not empty
		# REQUIRED

class SLLQueue(SLL):
	# Note that class "SLLQueue" inherits the class "SLL" attributes and methods

	def front(self):
		if self.size == 0:
			return SLLNode(None)
		else:
			return self.frontNode
		
		# The front() operation returns a reference value to the front element of the queue, but doesn’t remove it
		# REQUIRED

	def enqueue(self, value):
		newNode = SLLNode(value)
		if self.isEmpty():
			self.frontNode = newNode
		else:
			currentNode = self.frontNode
			while currentNode.getNext() is not None:
				currentNode = currentNode.getNext()
			currentNode.setNext(newNode)

		self.size += 1
		
		# The enqueue() operation inserts an element at the end of the queue
		# If the capacity is full, you are not allowed to enqueue() an element to the queue
		# REQUIRED

	def dequeue(self):
		# The dequeue() operation removes the element at the front of the queue
		# This should also return the 'Element' that was removed
		# REQUIRED
		if self.isEmpty():
			raise Exception
		else:
			dequeuedNode = self.frontNode
			self.frontNode = self.frontNode.getNext()
			self.size -= 1
			return dequeuedNode
		