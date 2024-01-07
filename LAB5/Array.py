 #Laboratory Exercise #1: Arrays and Linked Lists
class Element:
    def __init__ (self, value, index):
        self.value = value
        self.index = index
    
    def setValue(self, value):
        self.value = value
    
    def getValue(self):
        return self.value       
    
class Array:
    def __init__ (self):
        self.contents = []
        self.size = 0
        
    def addElement(self, value):
        newNode = Element(value, self.size)
        self.contents.append(newNode)
        self.size += 1

    def removeElement(self, index):
        if not self.isEmpty() and 0 <= index < self.size:
            while index < self.size - 1:
                self.contents[index].setValue((self.contents[index+1]).getValue())      #shift the elements (right of the removed element) tot he left
                index += 1
            self.size -= 1
        else:
            return      #if index not found, list empty
    
    def isEmpty(self):
        return (self.size == 0)










