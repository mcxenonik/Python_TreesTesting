from BinarySearchTree import BinarySearchTree
from Node import Node


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
            # node.right = Node(111)
            return None

        y = node.right
        t2 = y.left

        y.left = node                                                                           # WYKONAJ ROTACJE
        node.right = t2

        node.height = max(self._getHeight(node.left), self._getHeight(node.right)) + 1          # ZAKTUALIZUJ WYSOKOŚCI
        y.height = max(self._getHeight(y.left), self._getHeight(y.right)) + 1

        return y                                                                                # ZWRÓĆ NOWY WĘZEŁ


    def _rightRotate(self, node):
        if (node.left is None):
            # node.left = Node(222)
            return None

        y = node.left
        t3 = y.right

        y.right = node                                                                          # WYKONAJ ROTACJE
        node.left = t3

        node.height = max(self._getHeight(node.left), self._getHeight(node.right)) + 1          # ZAKTUALIZUJ WYSOKOŚCI
        y.height = max(self._getHeight(y.left), self._getHeight(y.right)) + 1

        return y                                                                                # ZWRÓĆ NOWY WĘZEŁ


    def _rebalance(self, node, value):
        if (node is None):
            return None

        node.height = max(self._getHeight(node.left), self._getHeight(node.right)) + 1          # ZAKTUALIZUJ WYSOKOŚĆ

        balance = self._getBalance(node)                                                        # ZWRÓĆ WSÓŁCZYNNIK WYWAŻENIA

        if (balance < -1 and value < node.left.value):                                          # PRZYPADEK LEFT LEFT
            return self._rightRotate(node)
        elif (balance > 1 and value > node.right.value):                                        # PRZYPADEK RIGHT RIGHT
            return self._leftRotate(node)
        elif (balance < -1 and value > node.left.value):                                        # PRZYPADEK LEFT RIGHT
            node.left = self._leftRotate(node.left)
            return self._rightRotate(node)
        elif (balance > 1 and value < node.right.value):                                        # PRZYPADEK RIGHT LEFT
            node.right = self._rightRotate(node.right)
            return self._leftRotate(node)
        else:
            return node                                                                         # WĘZEŁ WYWAŻONY -> ZWRÓĆ NIEZMIENIONY WĘZEŁ
