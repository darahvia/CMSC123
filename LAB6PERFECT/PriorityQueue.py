class Entry:
	def __init__(self, key, value):
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

class DLLNode:
	# Note: This 
	def __init__(self, entry, nextNode=None, prevNode=None):
		self.entry = entry
		self.nextNode = nextNode
		self.prevNode = prevNode

	def setEntry(self,entry):
		self.entry = entry

	def getEntry(self):
		# REQUIRED
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
		self.headNode = self.tailNode = DLLNode(None)

	def getSize(self):
		# returns the size of the queue
		# REQUIRED
		return self.size

	def isEmpty(self):
		# The isEmpty() operation returns true if the queue is empty and false if the queue is not empty
		# REQUIRED
		if self.size == 0:
			return True
		else:
			return False

	def find_min(self):
		# REQUIRED
		if self.isEmpty():														#no min since empty
			raise Exception ("Empty Queue")
		else:
			minimum = self.headNode.getEntry()									#set head as min
			current = self.headNode.getNext()									#current as the next node of head
			while current is not None:	
				if minimum.getKey() > current.getEntry().getKey():				#if min still has > value
					minimum = current.getEntry()								#set min to current
				current = current.getNext()										#current to neext node			
			return minimum

	def insert(self, entry):
		# REQUIRED
		node = DLLNode(entry)
		if self.isEmpty():
			self.headNode = self.tailNode = node								#1 node only
		else:
			current = self.headNode												#set current as the headnode		
			while current is not None:
				if current.getEntry().getKey() == entry.getKey():				#overwrite
					current.setEntry(entry)
					return
				current = current.getNext()
			self.tailNode.setNext(node)											#since unsorted just add sa tailnode
			node.setPrev(self.tailNode)
			self.tailNode = node
		self.size += 1

	def remove_min(self):
		# REQUIRED
		if self.isEmpty():
			raise Exception ("Empty Queue")
		minimum = self.min()
		if self.size == 1:														#if only 1 node
			self.headNode = self.tailNode = DLLNode(None)
		else:
			current = self.headNode										
			while current is not None:
				if current.getEntry() == minimum:								#min at head
					if current.getPrev() is None:
						self.headNode = current.getNext()						#set next node of head to be the new head
					else:
						current.getPrev().setNext(current.getNext())			#middle
					if current.getNext() is None: 								#min at tail
						self.tailNode = current.getPrev()						
					else:
						current.getNext().setPrev(current.getPrev())			#middle
				current = current.getNext()
		self.size -= 1
		return minimum

	def min(self):
		if self.isEmpty():
			raise Exception("Empty Queue")
		return self.find_min()													

class SortedPQ():
	def __init__(self):
		self.size = 0
		self.headNode = self.tailNode = DLLNode(Entry(None, None))

	def getSize(self):
		# returns the size of the queue
		# REQUIRED
		return self.size 

	def isEmpty(self):
		# The isEmpty() operation returns true if the queue is empty and false if the queue is not empty
		# REQUIRED
		if self.size == 0:
			return True
		else:
			return False

	def insert(self, entry):
		# make sure that the priority queue is always sorted whene inserting an entry
		# REQUIRED
		node = DLLNode(entry)
		if self.isEmpty():
			self.headNode = self.tailNode = node
		elif node.getEntry().getKey() <= self.headNode.getEntry().getKey():						#insert at start
			# if node.getEntry().getKey() == self.headNode.getEntry().getKey():					#overwrite
			# 	self.headNode.setEntry(entry)
			# 	return
			node.setNext(self.headNode)
			self.headNode.setPrev(node)
			self.headNode = node
		elif node.getEntry().getKey() >= self.tailNode.getEntry().getKey():						#insert at end
			# if node.getEntry().getKey() == self.tailNode.getEntry().getKey():					#overwrite
			# 	self.tailNode.setEntry(entry)
			# 	return
			node.setPrev(self.tailNode)
			self.tailNode.setNext(node)
			self.tailNode = node
		else:																					#insert at middle
			current = self.headNode.getNext()
			while current is not None and node.getEntry().getKey() > current.getEntry().getKey():
				current = current.getNext()		
			# if current is not None and node.getEntry().getKey() == current.getEntry().getKey():	#overwrite
			# 	current.setEntry(entry)
			# 	return
			node.setPrev(current.getPrev())
			current.getPrev().setNext(node)
			node.setNext(current)
			current.setPrev(node)
		self.size += 1

	def remove_min(self):
		# REQUIRED
		if self.isEmpty():
			raise Exception ("Empty Queue")
		min = self.min()
		if self.size == 1:											#only 1 node
			self.headNode = self.tailNode = DLLNode(None)
		else:														#removing headnode
			self.headNode.getNext().setPrev(None)
			self.headNode = self.headNode.getNext()
		self.size -= 1
		return min

	def min(self):
		# REQUIRED
		if self.isEmpty():
			raise Exception ("Empty Queue")
		else:
  			return self.headNode.getEntry()							#getting entry of headnode