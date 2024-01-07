import Array

class ArrayBinaryTree:
    def __init__(self):
        self.rootIndex = None
        self.array = Array.Array()

    def setRoot(self, value):
        if self.array.isEmpty():
            self.array.addElement(value)
            self.rootIndex = 0
        else:
            self.array.contents[self.rootIndex.setValue(value)]

    def getRoot(self):
        if not self.array.isEmpty():
            return self.array.contents[self.rootIndex].getValue()
        else:
            return None
        
    def setLeft(self, parentIndex, value):
        if not self.array.isEmpty():
            leftChildIndex = 2 * parentIndex + 1

            while leftChildIndex >= self.array.size:
                self.array.addElement(None)
            self.array.contents[leftChildIndex].setValue(value)

    def setRight(self, parentIndex, value):
        if not self.array.isEmpty():
            rightChildIndex = 2 * parentIndex + 2
            while rightChildIndex >= self.array.size:
                self.array.addElement(None)
            self.array.contents[rightChildIndex].setValue(value)

    def infixTraversal(self, currentIndex = None):
        if currentIndex is None:
            currentIndex = self.rootIndex
        
        if 0 <= currentIndex < self.array.size:
            self.infixTraversal(2 * currentIndex + 1)

            value = self.array.contents[currentIndex].getValue()
            print(value, end = " ")
            self.infixTraversal(2 * currentIndex + 2)

    def postfixTraversal(self, currentIndex=None):
        if currentIndex is None:
            # Start the traversal from the root if the current index is not provided
            currentIndex = self.rootIndex

        if 0 <= currentIndex < self.array.size:
            # Traverse the left subtree
            self.postfixTraversal(2 * currentIndex + 1)

            # Traverse the right subtree
            self.postfixTraversal(2 * currentIndex + 2)

            # Process the current node (print or do something else)
            value = self.array.contents[currentIndex].getValue()
            print(value, end=" ")
    def prefixTraversal(self, currentIndex=None):

        if currentIndex is None:
            # Start the traversal from the root if the current index is not provided
            currentIndex = self.rootIndex

        if 0 <= currentIndex < self.array.size:
            # Process the current node (print or do something else)
            value = self.array.contents[currentIndex].getValue()
            print(value, end=" ")

            # Traverse the left subtree
            self.prefixTraversal(2 * currentIndex + 1)

            # Traverse the right subtree
            self.prefixTraversal(2 * currentIndex + 2)

tree = ArrayBinaryTree()

# Setting up the tree
tree.setRoot(1)
tree.setLeft(0, 2)
tree.setRight(0, 3)
tree.setLeft(1, 5)
tree.setRight(1, 6)
tree.setLeft(2, 8)
tree.setRight(2, 7)
# Infix traversal

tree.infixTraversal()
print("\n")
tree.postfixTraversal()
print("\n")
tree.prefixTraversal()