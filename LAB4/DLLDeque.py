class DLLNode:
	def __init__(self, value):
		self.value = value
		self.nextNode = None
		self.prevNode = None

	def setValue(self,value):
		self.value = value

	def getValue(self):
		return self.value

	def setNext(self,nextNode):
		self.nextNode = nextNode

	def getNext(self):
		return self.nextNode

	def setPrev(self,prevNode):
		self.prevNode = prevNode

	def getPrev(self):
		return self.prevNode

class DLL:

	def __init__(self):
		self.size = 0
		self.headNode = DLLNode(None)
		self.tailNode = self.headNode
		self.tailNode.setNext(None)
		self.headNode.setPrev(None)

	def getSize(self):
		return self.size

	def isEmpty(self):
		return (self.getSize() == 0)


class DLLDeque(DLL):

	def first(self):
		return self.headNode

	def last(self):
		return self.tailNode


	def insertFirst(self, value):
		newNode = DLLNode(value)
		newNode.setNext(self.headNode)
		newNode.setPrev(None)
		self.headNode.setPrev(newNode)
		self.headNode = newNode
		self.size += 1

	def insertLast(self, value):
		newNode = DLLNode(value)
		newNode.setPrev(self.tailNode)
		newNode.setNext(None)
		self.tailNode.setNext(newNode)
		self.tailNode = newNode
		self.size += 1

	def removeFirst(self):
		if self.isEmpty():
			raise ValueError
		else:
			firstNode = self.headNode
			self.headNode = firstNode.getNext()
			firstNode.setNext(None)
			self.size -= 1
			return firstNode

	def removeLast(self):
		if self.isEmpty():
			raise ValueError
		else:
			lastNode = self.tailNode
			self.tailNode = lastNode.getPrev()
			lastNode.setPrev(None)
			self.size -= 1
			return lastNode
