class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value


class HashTableLP:
    def __init__(self, slots=30):
        self.slots = slots
        self.table = [None] * slots
        self.size = 0

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.slots

    def isEmpty(self):
        return self.size == 0

    def get(self, key):
        index = HashFunction(key, self.slots)
        initialIndex = index
        while self.table[index] is not None:
            if self.table[index].getKey() == key:
                return self.table[index]
            index = (index + 1) % self.slots        #next
            if index == initialIndex:
                break                   #finish traversing
        return None

    def put(self, key, value):
        index = HashFunction(key, self.slots)
        while self.table[index] is not None:
            if self.table[index].getKey() == key:
                return self.table[index]
            index = (index + 1) % self.slots    
            if self.size >= self.getCapacity():
                raise Exception("reached capacity")

        self.table[index] = Entry(key, value)
        self.size += 1

    def remove(self, key):
        index = HashFunction(key, self.slots)
        initialIndex = index
        while self.table[index] is not None:
            if self.table[index].getKey() == key:
                removeEntry = self.table[index]
                self.table[index] = None
                self.size -= 1
                return removeEntry
            index = (index + 1) % self.slots
            if index == initialIndex:       #already searched everyhing
                break
        return None

    def keys(self):
        for i in range(self.slots):
            if self.table[i] is not None:
                print(self.table[i].getKey())
        

    def values(self):
        for i in range(self.slots):
            if self.table[i] is not None:
                print(self.table[i].getValue())
        

    def entries(self):
        for i in range(self.slots):
            if self.table[i] is not None:
                print(f"Index {i}: {self.table[i].getKey()} : {self.table[i].getValue()}")


class SLLNode:
    def __init__(self, entry, nextNode):
        self.entry = entry
        self.nextNode = nextNode

    def setEntry(self, entry):
        self.entry = entry

    def getEntry(self):
        return self.entry

    def setNext(self, nextNode):
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode


class SLL:
    def __init__(self):
        self.size = 0
        self.frontNode = SLLNode(None, None)

    def isEmpty(self):
        return self.size == 0

    def addNode(self, entry):
        newNode = SLLNode(entry, self.frontNode)
        self.frontNode = newNode

    def removeNode(self, entry):
        currentNode = self.frontNode
        previousNode = None
        if self.isEmpty():
            return None
        else:
            while currentNode is not None:              #lab1
                if currentNode.getEntry() == entry:
                    if previousNode is None:            #head is to be removed
                        self.frontNode = currentNode.getNext()
                    else:
                        previousNode.setNext(currentNode.getNext())
                    return
                previousNode = currentNode
                currentNode = currentNode.getNext()


class HashTableSC:
    def __init__(self, slots=100):
        self.slots = slots
        self.table = [None] * slots
        self.size = 0

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.slots

    def isEmpty(self):
        return self.size == 0

    def get(self, key):
        index = HashFunction(key, self.slots)
        sll = self.table[index]     #find index of the key 
        if sll is not None:     
            node = sll.frontNode    #traverse until the key is found
            while node is not None : 
                entry = node.getEntry()
                if entry is not None and entry.getKey() == key: 
                    return entry
                node = node.getNext()  
        return None  

    def put(self, key, value):
        index = HashFunction(key, self.slots)

        if self.table[index] is None:
            self.table[index] = SLL()  #create a new SLL if the slot is empty
        if self.size >= self.getCapacity():
            raise Exception("exceeds capacity")
        self.table[index].addNode(Entry(key, value))
        self.size += 1

    def remove(self, key):
        index = HashFunction(key, self.slots)
        sll = self.table[index]     #find the linked list where the key is found
        if sll is not None:
            currentNode = sll.frontNode     #traverse
            while currentNode is not None:
                entry = currentNode.getEntry()
                if entry is not None and entry.getKey() == key:
                    sll.removeNode(currentNode.getEntry())
                    self.size -= 1
                    return currentNode.getEntry()
                currentNode = currentNode.getNext()

    def keys(self):
        for sll in self.table:
            if sll is not None and sll.frontNode is not None:
                currentNode = sll.frontNode
                while currentNode is not None:
                    entry = currentNode.getEntry()
                    if entry is not None:
                        print(entry.getKey())
                    currentNode = currentNode.getNext()

    def values(self):
        for sll in self.table:
            if sll is not None and sll.frontNode is not None:
                currentNode = sll.frontNode
                while currentNode is not None:
                    entry = currentNode.getEntry()
                    if entry is not None:
                        print(entry.getValue())
                    currentNode = currentNode.getNext()

    def entries(self):
        for i in range(self.slots):
            print(f"Chain {i}: ", end="")
            sll = self.table[i]
            if sll is not None and sll.frontNode is not None:
                currentNode = sll.frontNode
                while currentNode is not None:
                    entry = currentNode.getEntry()
                    if entry is not None:
                        print(f"[{entry.getKey()} : {entry.getValue()}]", end=" -> ")
                    currentNode = currentNode.getNext()
            print("None")


def HashFunction(key, capacity):
    if type(key) == int:
        return key % capacity
    elif type(key) == str:
        return (sum(ord(char) for char in key)) % capacity

def main():

    #create a hash table with linear probing
    print("Linear Probing")
    hashTableLP = HashTableLP(slots=30)

    #insert key-value pairs
    hashTableLP.put("Jala", "Anik Anik Gurlie")
    hashTableLP.put("Piage", "Genius gamer")
    hashTableLP.put("Emman", "Music Enthusiast")
    hashTableLP.put("Nicole", "Palainom") 
    hashTableLP.put("Angelique", "Manang of all")
    hashTableLP.put("Jullene", "Kezia's bff")
    hashTableLP.put("Vinz", "adios")
    hashTableLP.put("Aimee", "Reader")
    hashTableLP.put("Jansen", "Councilor")
    hashTableLP.put("Gerianne", "Mother")
    hashTableLP.put("Albin", "Miagawanon")
    hashTableLP.put("Leanne", "Blondie") 
    hashTableLP.put("Duranne", "My Crush")
    hashTableLP.put("Apong", "Damo Crush")
    hashTableLP.put("Jayvee", "May Blue Tumbler")
    hashTableLP.put("RJ", "Chinita Gurlie") 
    hashTableLP.put("Khanne", "KE YN")
    hashTableLP.put("Yvonne", "Furry")
    hashTableLP.put("Rian", "Gym Rat")
    hashTableLP.put("Angela", "CMS")
    hashTableLP.put("Jullyanne", "Basketball Player") 
    hashTableLP.put("Christine", "Power Dresser")
    hashTableLP.put("Earl", "Rich Kid")
    hashTableLP.put("Christalie", "Kopiko")
    hashTableLP.put("Kezia", "Cool Bass Girlie")
    hashTableLP.put("Shaina", "Kiatan")
    hashTableLP.put("Khean", "Side Quest Acads") 
    hashTableLP.put("Paolo", "Gwapo")
    hashTableLP.put("Patrick", "My Homie")
    hashTableLP.put("Nica", "My Favorite Realest")

    # #add beyond capacity
    # hashTableLP.put("Darah", "MEEE")

    #print the entries
    print("\nEntries in the hash table:")
    hashTableLP.entries()
    print("Size: ", hashTableLP.getSize())

    #print the keys
    print("\n\nKeys in the hash table:")
    hashTableLP.keys()

    #print the values
    print("\n\nValues in the hash table:")
    hashTableLP.values()

    #retrive values by keys
    print("\n\nRetrieve values by keys:")
    print("Value for 'Duranne':", hashTableLP.get("Duranne").getValue())
    print("Value for 'Yvonne':", hashTableLP.get("Yvonne").getValue())

    #remove entries
    print("\n\nRemove entry with key 'Duranne', 'Yvonne', 'Jansen', 'Rian':")
    removedValue = hashTableLP.remove("Duranne").getValue()
    print("Removed value for 'Duranne' :", removedValue)
    removedValue = hashTableLP.remove("Yvonne").getValue()
    print("Removed value for 'Yvonne':", removedValue)
    removedValue = hashTableLP.remove("Jansen").getValue()
    print("Removed value for 'Jansen':", removedValue)
    removedValue = hashTableLP.remove("Rian").getValue()
    print("Removed value for 'Rian':", removedValue)
    # hashTableLP.remove("Darah").getValue()
    

    #print the updated entries
    print("\n\nEntries in the hash table after removal:")
    hashTableLP.entries()
    print("Size: ", hashTableLP.getSize())



    #create a hash table with separate chaining
    print("\n\nSeparate Chaining")
    hashTableSC = HashTableSC(slots=30)
    #insert some key-value pairs
    hashTableSC.put("Jala", "Anik Anik Gurlie")
    hashTableSC.put("Piage", "Genius gamer")
    hashTableSC.put("Emman", "Music Enthusiast")
    hashTableSC.put("Nicole", "Palainom") 
    hashTableSC.put("Angelique", "Manang of all")
    hashTableSC.put("Jullene", "Kezia's bff")
    hashTableSC.put("Vinz", "adios")
    hashTableSC.put("Aimee", "Reader")
    hashTableSC.put("Jansen", "Councilor")
    hashTableSC.put("Gerianne", "Mother")
    hashTableSC.put("Albin", "Miagawanon")
    hashTableSC.put("Leanne", "Blondie") 
    hashTableSC.put("Duranne", "My Crush")
    hashTableSC.put("Apong", "Damo Crush")
    hashTableSC.put("Jayvee", "May Blue Tumbler")
    hashTableSC.put("RJ", "Chinita Gurlie") 
    hashTableSC.put("Khanne", "KE YN")
    hashTableSC.put("Yvonne", "Furry")
    hashTableSC.put("Rian", "Gym Rat")
    hashTableSC.put("Angela", "CMS")
    hashTableSC.put("Jullyanne", "Basketball Player") 
    hashTableSC.put("Christine", "Power Dresser")
    hashTableSC.put("Earl", "Rich Kid")
    hashTableSC.put("Christalie", "Kopiko")
    hashTableSC.put("Kezia", "Cool Bass Girlie")
    hashTableSC.put("Shaina", "Kiatan")
    hashTableSC.put("Khean", "Side Quest Acads") 
    hashTableSC.put("Paolo", "Gwapo")
    hashTableSC.put("Patrick", "My Homie")
    hashTableSC.put("Nica", "My Favorite Realest") 
    

    # #exceeds capacity
    # hashTableSC.put("Darah", "MEEE")
    
    #print the entries
    print("\nEntries in the hash table:")
    hashTableSC.entries()
    print("Size: ", hashTableSC.getSize())

    #print the keys
    print("\n\nKeys in the hash table:")
    hashTableSC.keys()

    #print the values
    print("\n\nValues in the hash table:")
    hashTableSC.values()

    #retrive values by keys
    print("\n\nRetrieve values by keys:")
    print("Value for 'Duranne':", hashTableSC.get("Duranne").getValue())
    print("Value for 'Yvonne':", hashTableSC.get("Yvonne").getValue())

    #remove entries
    print("\n\nRemove entry with key 'Duranne', 'Yvonne', 'Jansen', 'Rian':")
    removedValue = hashTableSC.remove("Duranne").getValue()
    print("Removed value for 'Duranne' :", removedValue)
    removedValue = hashTableSC.remove("Yvonne").getValue()
    print("Removed value for 'Yvonne':", removedValue)
    removedValue = hashTableSC.remove("Jansen").getValue()
    print("Removed value for 'Jansen':", removedValue)
    removedValue = hashTableSC.remove("Rian").getValue()
    print("Removed value for 'Rian':", removedValue)
    # hashTableLP.remove("Darah").getValue()

    #print the updated entries
    print("\n\nEntries in the hash table after removal:")
    hashTableSC.entries()
    print("Size: ", hashTableSC.getSize())

main()
