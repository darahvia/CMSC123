class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key


class DLLNode:
    def __init__(self, entry, nextNode=None, prevNode=None):
        self.entry = entry
        self.nextNode = None
        self.prevNode = None

    def getEntry(self):
        return self.entry

    def setEntry(self, entry):
        self.entry = entry

    def getNext(self):
        return self.nextNode

    def setNext(self, node):
        self.nextNode = node

    def getPrev(self):
        return self.prevNode

    def setPrev(self, node):
        self.prevNode = node


class UnsortedPQ:
    def __init__(self):
        self.size = 0
        self.headNode = self.tailNode = DLLNode(None)

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def find_min(self):
        if self.isEmpty():
            return None

        curr = self.headNode
        minNode = self.headNode
        minEntry = self.headNode.getEntry()

        while curr is not None:
            currEntry = curr.getEntry()

            if currEntry.getKey() < minEntry.getKey():
                minEntry = currEntry
                minNode = curr

            curr = curr.getNext()

        return minNode

    def insert(self, entry):
        key = entry.getKey()
        value = entry.getValue()
        newNode = DLLNode(entry)

        # check if key already exists
        curr = self.headNode
        while not self.isEmpty() and curr is not None:
            currEntry = curr.getEntry()

            # if found override entry
            if currEntry.getKey() == key:
                currEntry.setValue(value)

                return

            curr = curr.getNext()

        newNode.setPrev(self.tailNode)
        self.tailNode.setNext(newNode)
        self.tailNode = newNode

        if self.isEmpty():
            self.headNode = newNode

        self.size += 1

    def remove_min(self):
        if self.isEmpty():
            raise Exception("Priority Queue is empty.")

        minNode = self.find_min()
        minEntry = minNode.getEntry()

        # remove the entry from the list
        before = minNode.getPrev()
        after = minNode.getNext()

        if minNode == self.headNode:
            self.headNode = after

        if minNode == self.tailNode:
            self.tailNode = before

        if before:
            before.setNext(after)

        if after:
            after.setPrev(before)

        minNode.setNext(None)
        minNode.setPrev(None)

        self.size -= 1

        if self.isEmpty():
            self.headNode = self.tailNode = DLLNode(None)

        return minEntry

    def min(self):
        if self.isEmpty():
            raise Exception("Priority Queue is empty.")

        minNode = self.find_min()
        minEntry = minNode.getEntry()

        return minEntry

    def display(self):
        curr = self.headNode
        while curr:
            if curr.getEntry():
                print(curr.getEntry().getKey(), curr.getEntry().getValue(), end=", ")
            curr = curr.getNext()
        print()


class SortedPQ:
    def __init__(self):
        self.size = 0
        self.headNode = self.tailNode = DLLNode(None)

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insert(self, entry):
        key = entry.getKey()
        value = entry.getValue()
        newNode = DLLNode(entry)

        if self.isEmpty():
            self.headNode = newNode
            self.tailNode = self.headNode
            self.size += 1

            return

        self.size += 1

        # if key smaller than head key
        # make new entry the new head
        firstKey = self.headNode.getEntry().getKey()
        if key < firstKey:
            self.headNode.setPrev(newNode)
            newNode.setNext(self.headNode)
            self.headNode = newNode

            return

        # we don't need to check head anymore
        curr = self.headNode
        while curr:
            currEntry = curr.getEntry()

            # check if key already exists
            # if found override entry
            if currEntry.getKey() == key:
                currEntry.setValue(value)

                # not a new entry
                self.size -= 1

                return

            currKey = currEntry.getKey()
            before = curr.getPrev()

            if key < currKey:
                # before -> newNode -> curr
                before.setNext(newNode)
                newNode.setPrev(before)

                newNode.setNext(curr)
                curr.setPrev(newNode)

                return

            curr = curr.getNext()

        # that means key should be largest in the list
        self.tailNode.setNext(newNode)
        newNode.setPrev(self.tailNode)

        self.tailNode = newNode

    def remove_min(self):
        if self.isEmpty():
            raise Exception("Priority Queue is empty.")

        self.size -= 1

        minNode = self.headNode
        minEntry = minNode.getEntry()

        after = minNode.getNext()
        self.headNode = after

        if after:
            after.setPrev(None)

        minNode.setPrev(None)
        minNode.setNext(None)

        if self.isEmpty():
            self.headNode = self.tailNode = DLLNode(None)

        return minEntry

    def min(self):
        if self.isEmpty():
            raise Exception("Priority Queue is empty.")

        minNode = self.headNode
        minEntry = minNode.getEntry()

        return minEntry

