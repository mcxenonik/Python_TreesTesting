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


    def print_inorder(self):
        self._inorder(self.root)


    # A utility function to do inorder traversal of BST
    def _inorder(self, root):
        if root is not None:
            self._inorder(root.left_child)
            print(root.value)
            self._inorder(root.right_child)


    # Given a non-empty binary
    # search tree, return the node
    # with minimum key value
    # found in that tree. Note that the
    # entire tree does not need to be searched
    def _minValueNode(self, node):
        current = node
    
        # loop down to find the leftmost leaf
        while(current.left_child is not None):
            current = current.left_child
    
        return current


    def deleteNode(self, value):
        if value is not None:
            self.root = self._deleteNode(self.root, value)

    # Given a binary search tree and a key, this function
    # delete the key and returns the new root
    def _deleteNode(self, root, value):
        # Base Case
        if root is None:
            return root
    
        # If the key to be deleted
        # is smaller than the root's
        # key then it lies in  left subtree
        if value < root.value:
            root.left_child = self._deleteNode(root.left_child, value)
    
        # If the kye to be delete
        # is greater than the root's key
        # then it lies in right subtree
        elif(value > root.value):
            root.right_child = self._deleteNode(root.right_child, value)
    
        # If key is same as root's key, then this is the node
        # to be deleted
        else:
    
            # Node with only one child or no child
            if root.left_child is None:
                temp = root.right_child
                root = None
                return temp
    
            elif root.right_child is None:
                temp = root.left_child
                root = None
                return temp
    
            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self._minValueNode(root.right_child)
    
            # Copy the inorder successor's
            # content to this node
            root.value= temp.value
    
            # Delete the inorder successor
            root.right_child = self._deleteNode(root.right_child, temp.value)
    
        # self.root = root

        return root


    def print_tree(self):
        quene = []
        quene.append(self.root)
        while len(quene) != 0 :
            node = quene[0]
            if node.left_child == None:
                ll = '-'
            else:
                ll = node.left_child.value
            if node.right_child == None:
                rr = '-'
            else:
                rr = node.right_child.value
            print('  {n}  \n _|_ \n|   |\n{l}   {r}\n==========='.format(n = node.value, l = ll, r = rr))
            quene.pop(0)
            if node.left_child != None:
                quene.append(node.left_child)
            if node.right_child != None:
                quene.append(node.right_child)
        print('\n') 