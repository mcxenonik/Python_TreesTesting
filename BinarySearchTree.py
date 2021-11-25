from Node import Node

class BinarySearchTree:
    def __init__(self, values = None):
        self.root = None

        if (values is not None):
            for value in values:
                self.addNode(value)

#PRINT_TREE############################################################

    def printTree(self):
        queue = [self.root]
        
        print("TREE:")

        while (len(queue) != 0):
            node = queue.pop(0)

            if (node.left is not None):
                ll = node.left.value
                queue.append(node.left)
            else:
                ll = '-'

            if (node.right is not None):
                rr = node.right.value
                queue.append(node.right)
            else:
                rr = '-'
        
            print('  {n}  \n _|_ \n|   |\n{l}   {r}\n==========='
                  .format(n = node.value, l = ll, r = rr))

        print('\n')


    def printLevelorder(self):
        queue = [self.root]

        print("LEVELORDER:")

        while (len(queue) != 0):
            node = queue.pop(0)

            if (node is not None):
                print(node.value)

                queue.append(node.left)
                queue.append(node.right)


    def printInorder(self):
        print("INORDER:")

        self._printInorder(self.root)


    def _printInorder(self, root):
        if (root is not None):
            self._printInorder(root.left)
            print(root.value)
            self._printInorder(root.right)

#MINIMUM_VALUE#########################################################

    def _getMinValueNodeIter(self, node):
        currentNode = node
    
        while (currentNode.left is not None):
            currentNode = currentNode.left
    
        return currentNode

    def _getMinValueNodeRec(self, currentNode):
        if (currentNode.left is None):
            return currentNode
        else:
            return self._getMinValueNodeRec(currentNode.left)

#ADD_NODE##############################################################

    def addNode(self, value):
        if (value is not None):
            self.root = self._addNode(self.root, value)


    def _addNode(self, currentNode, value):
        if (currentNode is None):
            return Node(value)
        elif (value < currentNode.value):
            currentNode.left = self._addNode(currentNode.left, value)
        elif (value > currentNode.value):
            currentNode.right = self._addNode(currentNode.right, value)
        else:
            currentNode.quantity += 1

        return currentNode


    # def addNode(self, value):
    #     if (value is None):
    #         return
    #     elif (self.root is None):
    #         self.root = Node(value)
    #     else:
    #         self._addNode(self.root, value)


    # def _addNode(self, currentNode, value):
    #     if (value < currentNode.value):
    #         if (currentNode.left == None):
    #             currentNode.left = Node(value)
    #         else:
    #             self._addNode(currentNode.left, value)
    #     elif (value > currentNode.value):
    #         if (currentNode.right == None):
    #             currentNode.right = Node(value)
    #         else:
    #             self._addNode(currentNode.right, value)
    #     else:
    #         currentNode.quantity += 1

#FIND_NODE#############################################################

    def findNode(self, value):
        if (self.root is not None and value is not None):
            return self._findNode(self.root, value)
        else:
            return None


    def _findNode(self, currentNode, value):
        if (currentNode is None):
            return None
        elif (value < currentNode.value):
            return self._findNode(currentNode.left, value)
        elif (value > currentNode.value):
            return self._findNode(currentNode.right, value)
        else:
            return currentNode


    # def _findNode(self, currentNode, value):
    #     if (value == currentNode.value):
    #         return currentNode
    #     elif (value < currentNode.value and currentNode.left != None):
    #         return self._findNode(currentNode.left, value)
    #     elif (value > currentNode.value and currentNode.right != None):
    #         return self._findNode(currentNode.right, value)
    #     else:
    #         return None

#DELETE_NODE###########################################################

    def deleteNode(self, value):
        if (value is not None):
            self.root = self._deleteNode(self.root, value)


    def _deleteNode(self, currentNode, value):
        if (currentNode is None):
            return None
        elif (value < currentNode.value):
            currentNode.left = self._deleteNode(currentNode.left, value)
        elif (value > currentNode.value):
            currentNode.right = self._deleteNode(currentNode.right, value)
        else:
            if (currentNode.left is None):
                return currentNode.right
            elif (currentNode.right is None):
                return currentNode.left

            temp_node = currentNode

            currentNode = self._getMinValueNodeRec(temp_node.right)

            currentNode.right = self._deleteMinValueNode(temp_node.right)

            currentNode.left = temp_node.left

        return currentNode
    

    # def _deleteNode(self, currentNode, value):
    #     if (currentNode is None):
    #         return currentNode
    #     elif (value < currentNode.value):
    #         currentNode.left = self._deleteNode(currentNode.left, value)
    #     elif (value > currentNode.value):
    #         currentNode.right = self._deleteNode(currentNode.right, value)
    #     else:  
    #         if (currentNode.left is None):
    #             return currentNode.right
    #         elif (currentNode.right is None):
    #             return currentNode.left
    
    #         # Get the inorder successor (smallest in the right subtree)
    #         temp_node = self._getMinValueNodeIter(currentNode.right)
    
    #         # Copy the inorder successor's content to this node
    #         currentNode.value= temp_node.value
    
    #         # Delete the inorder successor
    #         currentNode.right = self._deleteNode(currentNode.right, temp_node.value)

    #     return node


    def _deleteMinValueNode(self, currentNode):
        if (currentNode.left is None):
            return currentNode.right

        currentNode.left = self._deleteMinValueNode(currentNode.left)

        return currentNode

