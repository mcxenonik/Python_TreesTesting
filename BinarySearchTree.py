from Node import Node

class BinarySearchTree:
    def __init__(self, values = None):
        self.root = None
        if values is not None:
            for value in values:
                self.addNode(value)


    def addNode(self, val):
        if self.root == None:
            self.root = Node(val)
        return self._addNode(self.root, val)


    def _addNode(self, currentNode, val):
        if val < currentNode.value:
            if currentNode.left_child == None:
                currentNode.left_child = Node(val)
            else:
                self._addNode(currentNode.left_child, val)
        elif val > currentNode.value:
            if currentNode.right_child == None:
                currentNode.right_child = Node(val)
            else:
                self._addNode(currentNode.right_child, val)
        else:
            currentNode.quantity += 1


    def findNode(self, val):
        if self.root == None:
            return None
        return self._findNode(self.root, val)


    def _findNode(self, currentNode, val):
        if val == currentNode.value:
            return currentNode
        elif val < currentNode.value and currentNode.left_child != None:
            self._findNode(currentNode.left_child, val)
        elif val > currentNode.value and currentNode.right_child != None:
            self._findNode(currentNode.right_child, val)
        else:
            return None