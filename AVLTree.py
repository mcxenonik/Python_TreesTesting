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
        currentNode = self._rebalance(currentNode, value)

        return currentNode


    def _deleteNode(self, currentNode, value):
        currentNode = super()._deleteNode(currentNode, value)
        currentNode = self._rebalance(currentNode, value)

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


    def _getHeight(self, node):
        if (node is not None):
            return node.height
        else:
            return 0


    def _getBalance(self, node):
        if (node is not None):
            return self._getHeight(node.right) - self._getHeight(node.left)
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


    def _leftRotate(self, node):
        y = node.right
        t3 = y.left

        y.left = node
        node.right = t3

        node.height = max(self._getHeight(node.left), self._getHeight(node.right)) + 1
        y.height = max(self._getHeight(y.left), self._getHeight(y.right)) + 1

        return y


    def _rightRotate(self, node):
        y = node.left
        t3 = y.right

        y.right = node
        node.left = t3

        node.height = max(self._getHeight(node.left), self._getHeight(node.right)) + 1
        y.height = max(self._getHeight(y.left), self._getHeight(y.right)) + 1

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


    def _rebalance(self, node, value):
        if (node is None):
            return None

        node.height = max(self._getHeight(node.left), self._getHeight(node.right)) + 1

        balance = self._getBalance(node)

        if (balance < -1 and value < node.left.value):
            return self._rightRotate(node)
        elif (balance > 1 and value > node.right.value):
            return self._leftRotate(node)
        elif (balance < -1 and value > node.left.value):
            node.left = self._leftRotate(node.left)
            return self._rightRotate(node)
        elif (balance > 1 and value < node.right.value):
            node.right = self._rightRotate(node.right)
            return self._leftRotate(node)
        else:
            return node
