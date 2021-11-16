from BinarySearchTree import BinarySearchTree

class AVLTree(BinarySearchTree):
    def _addNode(self, currentNode, val):
        super()._addNode(currentNode, val)
        self.rebalance(currentNode)


    def getHeight(self, currentNode):
        if currentNode is None:
            return 0
        return max(self.getHeight(currentNode.left_child), self.getHeight(currentNode.right_child)) + 1


    def getBalance(self, currentNode):
        if currentNode is None:
            return 0
        return self.getHeight(currentNode.left_child) - self.getHeight(currentNode.right_child)


    def leftRotate(self, currentNode):
        if currentNode.right_child is not None:
            right = currentNode.right_child
            currentNode.right_child = right.left_child
            right.left_child = currentNode


    def rightRotate(self, currentNode):
        if currentNode.left_child is not None:
            left = currentNode.left_child
            currentNode.left_child = left.right_child
            left.right_child = currentNode


    def rebalance(self, currentNode):
        if self.getBalance(currentNode) < -1:
            if self.getBalance(currentNode.right_child) < 0:
                self.leftRotate(currentNode)
            else:
                self.rightRotate(currentNode)
                self.leftRotate(currentNode)

        elif self.getBalance(currentNode) > 1:
            if self.getBalance(currentNode.left_child) > 0:
                self.rightRotate(currentNode)
            else:
                self.leftRotate(currentNode)
                self.rightRotate(currentNode)