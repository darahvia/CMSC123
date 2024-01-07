class DLLNode:
    def __init__(self, value):
        self.value = value
        self.parentNode = None
        self.nextNode = None
        self.prevNode = None
    
    def setParent(self, parentNode):
        self.parentNode = parentNode

    def getValue(self):
        return self.value
    
    def setNext(self, child):
        self.nextNode = child

    def getNext(self):
        return self.nextNode

    def setPrev(self, child):
        self.prevNode = child
    
    def getPrev(self):
        return self.prevNode
    
class DLLBinaryTree:
    def __init__(self):
        self.rootNode = None
        self.size = 0

    def setRoot(self, value):
        self.rootNode = DLLNode(value)

    def getRoot(self):
        return self.rootNode

    def setLeft(self, parentNode, value):
        child = DLLNode(value)
        child.setParent(parentNode)
        parentNode.setPrev(child)

    def setRight(self, parentNode, value):
        child = DLLNode(value)
        child.setParent(parentNode)
        parentNode.setNext(child)

def inorderTraversal(node):
    output = []
    if node is not None:
        left = node.getPrev()
        right = node.getNext()

        output.extend(inorderTraversal(left))

        value = node.getValue()
        output.append(value)

        output.extend(inorderTraversal(right))
    
    return output


def preorderTraversal(node):
    output = []
    if node is not None:
        left = node.getPrev()
        right = node.getNext()

        value = node.getValue()
        output.append(value)

        output.extend(preorderTraversal(left))
        output.extend(preorderTraversal(right))

    return output


def postorderTraversal(node):
    output = []
    if node is not None:
        left = node.getPrev()
        right = node.getNext()

        output.extend(postorderTraversal(left))
        output.extend(postorderTraversal(right))

        value = node.getValue()
        output.append(value)

    return output

# Create an instance of the DLLBinaryTree
linkedtree = DLLBinaryTree()
linkedtree.setRoot(1)
root = linkedtree.getRoot()

linkedtree.setLeft(root, 2)
linkedtree.setLeft(root.getPrev(), 4)
linkedtree.setRight(root.getPrev().getPrev(), 5)

linkedtree.setRight(root, 3)

inorder = inorderTraversal(root)
preorder = preorderTraversal(root)
postorder  = postorderTraversal(root)

print("Inorder Traversal:", inorder)
print("Preorder Traversal:", preorder)
print("Postorder Traversal:", postorder)