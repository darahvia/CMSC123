class DLLNode:
	# Insert the 'DLLNode' class you created in Lab1, since they should be the same
	def __init__(self, value):
		self.value = value
		self.nextNode = None
		self.prevNode = None

	def setValue(self,value):
		# REQUIRED

	def getValue(self):
		# REQUIRED

	def setNext(self,nextNode):
		# REQUIRED

	def getNext(self):
		# REQUIRED

	def setPrev(self,prevNode):
		# REQUIRED

	def getPrev(self):
		# REQUIRED

class DLL:
	# Insert the 'DLL' class you created in Lab1, since they should be the same
	def __init__(self):
		self.size = 0
		self.headNode = DLLNode(None)
		self.tailNode = self.headNode
		self.tailNode.setNext(None)
		self.headNode.setPrev(None)

	def getSize(self):
		# returns the size of the queue
		# REQUIRED

	def isEmpty(self):
		# The isEmpty() operation returns true if the queue is empty and false if the queue is not empty
		# REQUIRED

class DLLDeque(DLL):
	# Note that class "DLLQueue" inherits the class "DLL" attributes and methods

	def first(self):
		# The first() operation returns a reference value to the first element of the deque, but doesn’t remove it
		# REQUIRED

	def last(self):
		# The last() operation returns a reference value to the last element of the deque, but doesn’t remove it
		# REQUIRED

	def insertFirst(self, value):
		# The insertFirst() operation inserts an element at the front of the deque
		# REQUIRED

	def insertLast(self, value):
		# The insertLast() operation inserts an element at the end of the deque
		# REQUIRED

	def removeFirst(self):
		# The removeFirst() operation removes the element at the front of the deque
		# This should also return the 'DLLNode' that was removed
		# REQUIRED

	def removeLast(self):
		# The removeLast() operation removes the element at the end of the deque
		# This should also return the 'DLLNode' that was removed
		# REQUIRED