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


class DLLNode:
    def __init__(self, entry, nextNode=None, prevNode=None):
        self.entry = entry
        self.nextNode = nextNode
        self.prevNode = prevNode

    def setEntry(self, entry):
        self.entry = entry

    def getEntry(self):
        return self.entry

    def setNext(self, nextNode):
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode

    def setPrev(self, prevNode):
        self.prevNode = prevNode

    def getPrev(self):
        return self.prevNode


class DLLMap:
    def __init__(self):
        self.size = 0
        self.headNode = self.tailNode = DLLNode(None)

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def find_node(self, key):
        currentNode = self.headNode

        while currentNode is not None:
            if currentNode.getEntry() is not None and currentNode.getEntry().getKey() == key:
                return currentNode
            currentNode = currentNode.getNext()
        return None

    def get(self, key):
        foundNode = self.find_node(key)
        if foundNode is not None:
            return foundNode.getEntry().getValue()
        return None


    def put(self, key, value):
        exitingNode = self.find_node(key)
        if exitingNode is not None:
            exitingNode.getEntry().setValue(value)  # Overwrite existing entry value
        else:
            newNode = DLLNode(Entry(key, value))
            if self.isEmpty():      
                self.headNode = newNode    
                self.tailNode = newNode
            else:                               #add to tail
                self.tailNode.setNext(newNode)
                newNode.setPrev(self.tailNode)
                self.tailNode = newNode
            self.size += 1


    def remove(self, key):
        removeNode = self.find_node(key)
        if removeNode is not None:
            prevNode = removeNode.getPrev()
            nextNode = removeNode.getNext()

            if prevNode:
                prevNode.setNext(nextNode)
            else:
                self.headNode = nextNode    #head

            if nextNode:
                nextNode.setPrev(prevNode)
            else:
                self.tailNode = prevNode      #tail
            self.size -= 1
            
            removeNode.setNext(None)
            removeNode.setPrev(None)
            return removeNode.getEntry()
        raise Exception("not found")
        

    def keys(self):
        currentNode = self.headNode
        while currentNode is not None:
            if currentNode.getEntry().getKey() is not None:
                print(currentNode.getEntry().getKey())
            currentNode = currentNode.getNext()

    def values(self):
        currentNode = self.headNode
        while currentNode is not None:
            if currentNode.getEntry() is not None:
                print(currentNode.getEntry().getValue())
            currentNode = currentNode.getNext()

    def entries(self):
        currentNode = self.headNode
        while currentNode is not None:
            if currentNode.getEntry() is not None:
                entry = currentNode.getEntry()
                print(f"{entry.getKey()}:{entry.getValue()}")
            currentNode = currentNode.getNext()
