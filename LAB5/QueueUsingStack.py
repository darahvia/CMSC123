import ArrayStack
class QueueUsingStack:
    def __init__(self):
        self.stack1 = ArrayStack.ArrayStack()  # For enqueueing
        self.stack2 = ArrayStack.ArrayStack() # For dequeuing

    def enqueue(self, value):
        # Push the element onto stack1
        self.stack1.push(value)

    def dequeue(self):
        if self.stack2.isEmpty():
            # If stack2 is empty, pop elements from stack1 and push onto stack2
            while not self.stack1.isEmpty():
                value = self.stack1.pop().getValue()
                self.stack2.push(value)

        if self.stack2.isEmpty():
            raise Exception("Queue is empty")

        # Pop the element from stack2
        return self.stack2.pop().getValue()

    def front(self):
        if self.stack2.isEmpty():
            if self.stack1.isEmpty():
                raise Exception("Queue is empty")
            else:
                # If stack2 is empty, pop elements from stack1 and push onto stack2
                while not self.stack1.isEmpty():
                    value = self.stack1.pop().getValue()
                    self.stack2.push(value)

        return self.stack2.top().getValue()
    
    def display(self):
        display_list = []

        # First, pop elements from stack1 and push onto stack2
        while not self.stack1.isEmpty():
            value = self.stack1.pop().getValue()
            self.stack2.push(value)

        # Then, pop elements from stack2 and push onto stack1 while building the display_list
        while not self.stack2.isEmpty():
            value = self.stack2.pop().getValue()
            self.stack1.push(value)
            display_list.append(str(value))

        print("Queue:", " ".join(display_list))


# Example code using the display method
queue = QueueUsingStack()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.display()  # Output: Queue: 1 2 3

queue.dequeue()
queue.enqueue(4)

queue.display()  # Output: Queue: 2 3 4


