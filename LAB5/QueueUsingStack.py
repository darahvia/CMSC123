import SLLStack
class QueueUsingStack:
    def __init__(self):
        self.mainStack = SLLStack.SLLStack() 
        self.tempStack = SLLStack.SLLStack() 

    def enqueue(self, value):
        self.mainStack.push(value)                                          # Push the element onto mainStack

    def dequeue(self):

        if self.mainStack.isEmpty():
            return

        else:
            while not self.mainStack.isEmpty():                             
                self.tempStack.push(self.mainStack.pop().getValue())        #pop elements from mainStack to tempStack to reverse
    
            dequeuedNode = self.tempStack.pop().getValue()
            while not self.tempStack.isEmpty():                                 #push back to main queue but without the dequeued node
                self.mainStack.push(self.tempStack.pop().getValue())
            return dequeuedNode

    def front(self):
        if self.mainStack.isEmpty():
            return "Queue is empty."

        else:
            while not self.mainStack.isEmpty():                             #same implementation with dequeue but does not remove
                self.tempStack.push(self.mainStack.pop().getValue())
        
            frontNode = self.tempStack.top().getValue()
            while not self.tempStack.isEmpty():
                self.mainStack.push(self.tempStack.pop().getValue())
            return frontNode
    
    def display(self):
        displayList = []
        if self.mainStack.isEmpty():
            print("Queue is empty.")
            
        else:
            while not self.mainStack.isEmpty():                                 # Move all elements from mainStack to tempStack and build the displayList
                self.tempStack.push(self.mainStack.pop().getValue())

            while not self.tempStack.isEmpty():                                 #pop the tempStack so that it will follow the sequence of nodes
                node = self.tempStack.pop().getValue()
                displayList.append(str(node))
                self.mainStack.push(node)
            print("Queue:", " ".join(displayList))
            

        
        

# Example code using the display method
queue = QueueUsingStack()

# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
queue.display()
print(queue.front())

queue.dequeue()
queue.enqueue(4)

queue.display()
print(queue.front())

