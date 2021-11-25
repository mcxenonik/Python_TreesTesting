from BinarySearchTree import BinarySearchTree

class AVLTree(BinarySearchTree):
    def __init__(self, values = None):
        super().__init__(values)


    # def _addNode(self, currentNode, value):
    #     super()._addNode(currentNode, value)
    #     self.rebalance(currentNode)


    # def _deleteNode(self, currentNode, value):
    #     super()._deleteNode(currentNode, value)
    #     self.rebalance(currentNode)


    def _addNode(self, currentNode, value):
        currentNode = super()._addNode(currentNode, value)
        currentNode = self.rebalance(currentNode, value)

        return currentNode


    def _deleteNode(self, currentNode, value):
        currentNode = super()._deleteNode(currentNode, value)
        currentNode = self.rebalance(currentNode, value)

        return currentNode


    # def getHeight(self, node):
    #     if (node is not None):
    #         return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
    #     else:
    #         return 0


    # def getBalance(self, node):
    #     if (node is not None):
    #         return self.getHeight(node.left) - self.getHeight(node.right)
    #     else:
    #         return 0


    def getHeight(self, node):
        if (node is not None):
            return node.height
        else:
            return 0


    def getBalance(self, node):
        if (node is not None):
            return self.getHeight(node.right) - self.getHeight(node.left)
        else:
            return 0


    # def leftRotate(self, currentNode):
    #     if (currentNode.right_child is not None):
    #         right = currentNode.right_child
    #         currentNode.right_child = right.left_child
    #         right.left_child = currentNode


    # def rightRotate(self, currentNode):
    #     if (currentNode.left_child is not None):
    #         left = currentNode.left_child
    #         currentNode.left_child = left.right_child
    #         left.right_child = currentNode


    def leftRotate(self, node):
        y = node.right
        t3 = y.left

        y.left = node
        node.right = t3

        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) + 1

        return y


    def rightRotate(self, node):
        y = node.left
        t3 = y.right

        y.right = node
        node.left = t3

        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) + 1

        return y


    # def rebalance(self, node):
    #     if (self.getBalance(node) < -1):
    #         if (self.getBalance(node.right) < 0):
    #             self.leftRotate(node)
    #         else:
    #             self.rightRotate(node)
    #             self.leftRotate(node)
    #     elif (self.getBalance(node) > 1):
    #         if (self.getBalance(node.left) > 0):
    #             self.rightRotate(node)
    #         else:
    #             self.leftRotate(node)
    #             self.rightRotate(node)


    def rebalance(self, currentNode, value):
        if (currentNode is None):
            return None

        currentNode.height = max(self.getHeight(currentNode.left), self.getHeight(currentNode.right)) + 1

        balance = self.getBalance(currentNode)

        if (balance < -1 and value < currentNode.left.value):
            return self.rightRotate(currentNode)
        elif (balance > 1 and value > currentNode.right.value):
            return self.leftRotate(currentNode)
        elif (balance < -1 and value > currentNode.left.value):
            currentNode.left = self.leftRotate(currentNode.left)
            return self.rightRotate(currentNode)
        elif (balance > 1 and value < currentNode.right.value):
            currentNode.right = self.rightRotate(currentNode.right)
            return self.rightRotate(currentNode)
        else:
            return currentNode
