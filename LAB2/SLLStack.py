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
		self.topNode = SLLNode(None)
		self.topNode.setNext(SLLNode(None))

	def isEmpty(self):
		return (self.size == 0)

class SLLStack(SLL):

	def top(self):
		if self.size == 0:
			return SLLNode(None)
		else:
			return self.topNode


	def push(self, value):
		newNode = SLLNode(value)
		if self.isEmpty():
			self.topNode = newNode
		else:
			newNode.setNext(self.topNode)
			self.topNode = newNode
		self.size += 1
		
		

	def pop(self):
		if self.isEmpty():
			raise ValueError
		else:
			poppedNode = self.topNode
			self.topNode = self.topNode.getNext()
			self.size -= 1
			return poppedNode
