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

        new_entry = Entry(key, value)
        currentkey_Index = 0

        # find position within array and greater than currentkey
        while (currentkey_Index < self.size and 
               new_entry.getKey() > self.contents[currentkey_Index].getKey()):
            
            currentkey_Index += 1

        # shift elements to right, start from end of array to currentkey_index
        for i in range(self.size, currentkey_Index, -1):
            self.contents[i] = self.contents[i - 1]

        self.contents[currentkey_Index] = new_entry
        self.size += 1

    def remove(self, entry):

        # find entry with the key and value
        for i in range(self.size):
            if (self.contents[i].getKey() == entry.getKey() and 
            self.contents[i].getValue() == entry.getValue()):
                
                remove_entry = self.contents[i]

                # shift elements to left, start from [i] to end of array
                for j in range(i, self.size - 1):
                    self.contents[j] = self.contents[j + 1]

                # set last duplicate to none
                self.contents[self.size - 1] = None
                self.size -= 1

                return remove_entry

        raise Exception("Empty") 

    def find(self, key):
        # find entry with specific key

        for i in range(self.size):
            if (self.contents[i].getKey() == key):

                return self.contents[i]
            
        raise Exception("Empty") 

    def find_all(self, key):
        # print entries with key     

        for i in range(self.size):
            if self.contents[i].getKey() == key:

                print(f"({self.contents[i].getKey()}: {self.contents[i].getValue()})", end=" ")

    def entries(self):
        # print all entries

        print("\n") 
        for i in range(self.size):

            print(f"({self.contents[i].getKey()}: {self.contents[i].getValue()})", end=" ")
