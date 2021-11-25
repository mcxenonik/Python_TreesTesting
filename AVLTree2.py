from BinarySearchTree2 import BinarySearchTree2

class AVLTree2(BinarySearchTree2):
    def __init__(self, values = None):
        super().__init__(values)


    def _addNode(self, currentNode, value):
        super()._addNode(currentNode, value)
        self.rebalance(currentNode)


    def _deleteNode(self, currentNode, value):
        super()._deleteNode(currentNode, value)
        self.rebalance(currentNode)


    def getHeight(self, node):
        if (node is not None):
            return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        else:
            return 0


    def getBalance(self, node):
        if (node is not None):
            return self.getHeight(node.left) - self.getHeight(node.right)
        else:
            return 0


    def leftRotate(self, currentNode):
        if (currentNode.right is not None):
            right = currentNode.right
            currentNode.right = right.left
            right.left = currentNode


    def rightRotate(self, currentNode):
        if (currentNode.left is not None):
            left = currentNode.left
            currentNode.left = left.right
            left.right = currentNode


    def rebalance(self, node):
        if (self.getBalance(node) < -1):
            if (self.getBalance(node.right) < 0):
                self.leftRotate(node)
            else:
                self.rightRotate(node)
                self.leftRotate(node)
        elif (self.getBalance(node) > 1):
            if (self.getBalance(node.left) > 0):
                self.rightRotate(node)
            else:
                self.leftRotate(node)
                self.rightRotate(node)
