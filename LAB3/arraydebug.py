class Element:
	# Insert the 'Element' class you created in Lab2, since they should be the same
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
	# Insert the 'Array' class you created in Lab2, since they should be the same
	def __init__(self, capacity=10):
		self.contents = []
		self.size = 0 				# The 'size' attribute must not exceed the 'capacity'		
		self.capacity = capacity
		self.DEFAULT_EXPANSION = 5
		
	def getSize(self):
		return self.size

	def getCapacity(self):
		return self.capacity

	def isEmpty(self):
		return (self.size == 0)

	def expand(self):
		# The expand() operation increases the capacity when necessary
		self.capacity += self.DEFAULT_EXPANSION

class ArrayQueue(Array):
	# Note that class "ArrayQueue" inherits the class "Array" attributes and methods

	def front(self):
		if not self.contents:
			return None
		return self.contents[0]
		# The front() operation returns a reference value to the front element of the queue, but doesn’t remove it
		# REQUIRED

	def enqueue(self, value):
		if (self.size < self.capacity):
			newElement = Element(value, self.size)
			self.contents  += [newElement]
			self.size += 1
			return
		else:
			raise Exception
		# The enqueue() operation inserts an element at the end of the queue
		# If the capacity is full, you are not allowed to enqueue() an element to the queue
		# REQUIRED

	def dequeue(self):
		if self.isEmpty():
			raise Exception
		else:
			dequeuedElement = self.contents[0]
			for i in range(1,self.size):
				self.contents[i - 1] = self.contents[i]
			self.size -= 1
			return dequeuedElement
			
		# The dequeue() operation removes the element at the front of the queue
		# This should also return the 'Element' that was removed
		# REQUIRED

import random

# Array Queue Tester
def ArrayQueueTest():
	score = 0
	TOTAL = 50
	testArray = ArrayQueue()
	
	randNums = []

	for i in range(10):
		randNums.append(i)
		testArray.enqueue(randNums[i])
		score+=1

	try:
		for i in range(10):
			print(" ".join(map(str, [element.getValue() for element in testArray.contents[:testArray.getSize()]])))
 

			prevSize = testArray.getSize()
			
			removed = testArray.dequeue()
			print(removed.getValue())

			front = testArray.front()
			print(front.getValue())

			print("\n")

			if removed.getValue() != front.getValue():
				score+=0.5
				
			if testArray.getSize() == (prevSize - 1):
				score+=0.5
				
			if removed.getValue() == randNums[i]:
				score+=1
				
	except:
		print("Error: dequeue() not working properly")

	# Empty Stack Test
	if testArray.isEmpty():
		score+=2
		
		try:
			testArray.dequeue()
			print("Error: dequeue() still working even if array is empty")
		except:
			score+=3
			

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")
		
ArrayQueueTest()