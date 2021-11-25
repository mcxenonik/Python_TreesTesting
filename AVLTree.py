from BinarySearchTree import BinarySearchTree

class AVLTree(BinarySearchTree):
    def __init__(self, values = None):
        super().__init__(values)


    def __str__(self):
        return "AVLTree"


    def _addNode(self, currentNode, value):
        currentNode = super()._addNode(currentNode, value)
        currentNode = self._rebalance(currentNode, value)

        return currentNode


    def _deleteNode(self, currentNode, value):
        currentNode = super()._deleteNode(currentNode, value)
        currentNode = self._rebalance(currentNode, value)

        return currentNode


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


    def _leftRotate(self, node):
        if (node.right is None):
            return None

        y = node.right
        t3 = y.left

        y.left = node
        node.right = t3

        node.height = max(self._getHeight(node.left), self._getHeight(node.right)) + 1
        y.height = max(self._getHeight(y.left), self._getHeight(y.right)) + 1

        return y


    def _rightRotate(self, node):
        if (node.left is None):
            return None

        y = node.left
        t3 = y.right

        y.right = node
        node.left = t3

        node.height = max(self._getHeight(node.left), self._getHeight(node.right)) + 1
        y.height = max(self._getHeight(y.left), self._getHeight(y.right)) + 1

        return y


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
