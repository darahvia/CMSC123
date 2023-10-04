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
		
import random
def SLLStackTest():
 
	score = 0
	TOTAL = 50
	testSLL = SLLStack()
	
	try:
		if testSLL.isEmpty():
			score+=1
	except:
		print("Error: Problem initializing stack")

	randNums1 = []
	try:
		for i in range(10):
			randNums1.append(random.random())
			testSLL.push(randNums1[i])
		
		if testSLL.size == 10:
			score+=2

		i = 0
		current = testSLL.top()
		while current:
			if current.getValue() == randNums1[10-(i+1)]:
				score+=1
				current = current.getNext()
				i+=1
	except:
		print("Error: push() not working properly")
	##########
	try:
		for i in range(10):
			removed = testSLL.pop()
			top = testSLL.top()

			if top.getValue() != removed.getValue():
				score+=2										#########last iteration wla ga work
			if removed.getValue() == randNums1[10-(i+1)]:
				score+=1									####### last iteration wala ga work


	except:
		print("Error: pop() not working properly")
	
	# Empty SLL Test

	print("size = ", testSLL.size)
	try:
		if testSLL.isEmpty():
			score+=1
		if (testSLL.top().getValue() == None):		####################### does not gawork
			print("2")
			score+=2
	except:
		print("Error: pop() not working properly [does not empty SLL]")
	try:
		testSLL.pop()
		print("Error: pop() still working even if SLL is empty")
	except:
		score+=3

	# Return Value Test
	try:
		rand = random.random()
		testSLL.push(rand)
		x = testSLL.pop()
		testSLL.push(x.getValue())
		if testSLL.top().getValue() == rand:
			score+=1
	except:
		print("Error: top(), push(), or pop() not working after SLL became empty")

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")
		
SLLStackTest()