class Entry:
	def __init__(self, key = None, value = None):
		self.key = key
		self.value = value

	def setKey(self,key):
		self.key = key

	def getKey(self):
		return self.key

	def setValue(self,value):
		self.value = value

	def getValue(self):
		return self.value

class DLLNode(Entry):
	# Note: This 
	def __init__(self, entry, nextNode=None, prevNode=None):
		self.entry = entry
		self.nextNode = nextNode
		self.prevNode = prevNode

	def setEntry(self,value):
		self.entry = value

	def getEntry(self):
		return self.entry

	def setNext(self,nextNode):
		self.nextNode = nextNode

	def getNext(self):
		return self.nextNode

	def setPrev(self,prevNode):
		self.prevNode = prevNode

	def getPrev(self):
		return self.prevNode	

class UnsortedPQ():

	def __init__(self):
		self.size = 0
		self.headNode = self.tailNode = DLLNode(Entry())

	def getSize(self):
		return self.size

	def isEmpty(self):
		return (self.size == 0)

	def find_min(self):
		if self.isEmpty():
			return None
		else:
			minEntry = self.headNode.getEntry()
			currentNode = self.headNode.getNext()
			while currentNode is not None:
				if currentNode.getEntry().getKey() < minEntry.getKey():
					minEntry = currentNode.getEntry()
				currentNode = currentNode.getNext()

			return minEntry

	def insert(self, entry):
		newNode = DLLNode(entry)
		if self.isEmpty():
			self.headNode.setEntry(newNode.getEntry())
			self.tailNode.setEntry(newNode.getEntry())
		else:
			newNode.setPrev(self.tailNode)
			self.tailNode.setNext(newNode)
			self.tailNode = newNode
		self.size += 1


	def remove_min(self):
		if self.isEmpty():
			raise Exception("Priority Queue is empty")
		
		minEntry = self.find_min()
		minNode = None
		
		# Find the node containing the minimum entry
		currentNode = self.headNode
		while currentNode is not None:
			if currentNode.getEntry() == minEntry:
				minNode = currentNode
				break
			currentNode = currentNode.getNext()

		prevNode = minNode.getPrev()
		nextNode = minNode.getNext()

		if prevNode is not None:
			prevNode.setNext(nextNode)

		if nextNode is not None:
			nextNode.setPrev(prevNode)

		minNode.setPrev(None)
		minNode.setNext(None)

		self.size -= 1

		return minEntry

	def min(self):
		if self.isEmpty():
			return None
		else:
			return self.find_min()

class SortedPQ():
	def __init__(self):
		self.size = 0
		self.headNode = self.tailNode = DLLNode(Entry())

	def getSize(self):
		return self.size
	
	def isEmpty(self):
		return (self.size == 0)

	def insert(self, entry):
		newNode = DLLNode(entry)
		if self.isEmpty():
			self.headNode = self.tailNode = newNode
		
		elif newNode.getEntry().getKey() <= self.headNode.getEntry().getKey():		#smallest
			newNode.setNext(self.headNode)
			self.headNode.setPrev(newNode)
			self.headNode = newNode
		
		elif newNode.getEntry().getKey() >= self.tailNode.getEntry().getKey():		#largest
			newNode.setPrev(self.tailNode)
			self.tailNode.setNext(newNode)
			self.tailNode = newNode

		else: 	#middle
			currentNode = self.headNode
			while currentNode is not None and currentNode.getEntry().getKey() < newNode.getEntry().getKey():
				currentNode = currentNode.getNext()

			newNode.setPrev(currentNode.getPrev())
			newNode.setNext(currentNode)
			currentNode.getPrev().setNext(newNode)
			currentNode.setPrev(newNode)
		self.size += 1



	def remove_min(self):
		if self.isEmpty():
			raise Exception
		minNode = self.min()
		if self.size == 1:
			self.headNode = self.tailNode = DLLNode(Entry())
		else:
			self.headNode.getNext().setPrev(None)
			self.headNode = self.headNode.getNext()
			# self.headNode = self.headNode.getNext()
			# self.headNode.setPrev(None)
		self.size -= 1
		return minNode
		

	def min(self):
		if self.isEmpty():
			raise Exception ("Empty Queue")
		else:
			return self.headNode.getEntry()