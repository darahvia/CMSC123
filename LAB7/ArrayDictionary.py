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

class Array:
	def __init__(self, capacity=100):
		self.capacity = capacity
		self.contents = [None]*capacity
		self.size = 0 
		
	def getSize(self):
		return self.size

	def getCapacity(self):
		return self.capacity		

	def isEmpty(self):
		return self.size == 0		

class ArrayDictionary(Array):
	
	def insert(self, key, value):
		newEntry = Entry(key, value)
		currentEntryIndex = 0
	
		while currentEntryIndex < self.size and newEntry.getKey() >= self.contents[currentEntryIndex].getKey():	#finds the index where the new entry should be inserted
			currentEntryIndex += 1

		for i in range (self.size, currentEntryIndex, -1):	#makes space for the new entry
			self.contents[i] = self.contents[i - 1]		#shift right

		self.contents[currentEntryIndex] = newEntry
		self.size += 1

	def remove(self, entry):
		if self.isEmpty():
			raise Exception("empty")
		else:
			for i in range(self.size):
				if self.contents[i].getKey() == entry.getKey() and self.contents[i].getValue() == entry.getValue():
					removedEntry = self.contents[i]

					for j in range(i, self.size - 1):			#shifts the elements after the removed entry
						self.contents[j] = self.contents[j + 1]		#shift left

					self.contents[self.size - 1] = None
					self.size -= 1

					return removedEntry
			raise Exception("not found")		

	def find(self, key):
		if self.isEmpty():
			raise Exception
		else:
			for i in range(self.size):
				if self.contents[i].getKey() == key:
					return self.contents[i]
			raise Exception("not found")	

	# Iterator Methods
	def find_all(self, key):
		for i in range(self.size):
			if self.contents[i].getKey() == key:
				print(f"({self.contents[i].getKey()}: {self.contents[i].getValue()})", end=" ")
		# iterates through the existing entries in the dictionary and prints all the entries (in the format "key:value") with the specified key in order
		
	def entries(self):
		for i in range(self.size):
			print(f"{self.contents[i].getKey()} : {self.contents[i].getValue()}")
		# iterates through the existing entries in the dictionary and prints all the entries (in the format "key:value") in order
		
