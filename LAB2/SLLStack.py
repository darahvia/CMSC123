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
		# self.topNode.setNext(SLLNode(None))

	def isEmpty(self):
		return (self.size == 0)

class SLLStack(SLL):

	def top(self):
		if self.size == 0:
			return SLLNode(None)
		return self.topNode.getNext()


	def push(self, value):
		newNode = SLLNode(value)
		newNode.setNext(self.topNode.getNext())
		self.topNode.setNext(newNode)
		self.size += 1
		
		

	def pop(self):
		if self.isEmpty():
			raise ValueError

		poppedNode = self.topNode.getNext()
		self.topNode.setNext(poppedNode.getNext())
		self.size -= 1
		return poppedNode
