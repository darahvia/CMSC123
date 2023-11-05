class SLLNode:
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
	def __init__(self):
		self.size = 0
		self.frontNode = SLLNode(None)
		self.frontNode.setNext(SLLNode(None))

	def getSize(self):
		return self.size

	def isEmpty(self):
		return (self.size == 0)

class SLLQueue(SLL):
	def front(self):
		if self.size == 0:
			return SLLNode(None)
		else:
			return self.frontNode


	def enqueue(self, value):
		newNode = SLLNode(value)
		if self.isEmpty():
			self.frontNode = newNode
		else:
			currentNode = self.frontNode
			while currentNode.getNext() is not None:	#loop until last node is found
				currentNode = currentNode.getNext()
			currentNode.setNext(newNode)

		self.size += 1

	def dequeue(self):
		if self.isEmpty():
			raise Exception
		else:
			dequeuedNode = self.frontNode				#store the frontNode
			self.frontNode = self.frontNode.getNext()	#make the frontNode to be the next node of the previous frontNode
			dequeuedNode.setNext(SLLNode(None))
			self.size -= 1
			return dequeuedNode
		