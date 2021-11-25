from Node import Node

class BinarySearchTree2:
    def __init__(self, values = None):
        self.root = None

        if (values is not None):
            for value in values:
                self.addNode(value)


#PRINT_TREE############################################################

    def printBetterTree(self):
        lines = self._build_tree_string(self.root, 0, False, "-")[0]

        print("\n" + "\n".join((line.rstrip() for line in lines)))

    def _build_tree_string(self, root, curr_index, include_index=False, delimiter="-"):

        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if include_index:
            node_repr = "{}{}{}".format(curr_index, delimiter, root.value)
        else:
            node_repr = str(root.value)

        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths, and root repr positions
        l_box, l_box_width, l_root_start, l_root_end = self._build_tree_string(
            root.left, 2 * curr_index + 1, include_index, delimiter
        )
        r_box, r_box_width, r_root_start, r_root_end = self._build_tree_string(
            root.right, 2 * curr_index + 2, include_index, delimiter
        )

        # Draw the branch connecting the current root node to the left sub-box
        # Pad the line with whitespaces where necessary
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(" " * (l_root + 1))
            line1.append("_" * (l_box_width - l_root))
            line2.append(" " * l_root + "/")
            line2.append(" " * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        # Draw the representation of the current root node
        line1.append(node_repr)
        line2.append(" " * new_root_width)

        # Draw the branch connecting the current root node to the right sub-box
        # Pad the line with whitespaces where necessary
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append("_" * r_root)
            line1.append(" " * (r_box_width - r_root + 1))
            line2.append(" " * r_root + "\\")
            line2.append(" " * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        # Combine the left and right sub-boxes with the branches drawn above
        gap = " " * gap_size
        new_box = ["".join(line1), "".join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else " " * l_box_width
            r_line = r_box[i] if i < len(r_box) else " " * r_box_width
            new_box.append(l_line + gap + r_line)

        # Return the new box, its width and its root repr positions
        return new_box, len(new_box[0]), new_root_start, new_root_end


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
        if (value is None):
            return
        elif (self.root is None):
            self.root = Node(value)
        else:
            self._addNode(self.root, value)


    def _addNode(self, currentNode, value):
        if (value < currentNode.value):
            if (currentNode.left == None):
                currentNode.left = Node(value)
            else:
                self._addNode(currentNode.left, value)
        elif (value > currentNode.value):
            if (currentNode.right == None):
                currentNode.right = Node(value)
            else:
                self._addNode(currentNode.right, value)

#FIND_NODE#############################################################

    def findNode(self, value):
        if (self.root is not None and value is not None):
            return self._findNode(self.root, value)
        else:
            return None


    def _findNode(self, currentNode, value):
        if (value == currentNode.value):
            return currentNode
        elif (value < currentNode.value and currentNode.left != None):
            return self._findNode(currentNode.left, value)
        elif (value > currentNode.value and currentNode.right != None):
            return self._findNode(currentNode.right, value)
        else:
            return None

#DELETE_NODE###########################################################

    def deleteNode(self, value):
        if (value is not None):
            self.root = self._deleteNode(self.root, value)


    def _deleteNode(self, currentNode, value):
        if (currentNode is None):
            return currentNode
        elif (value < currentNode.value):
            currentNode.left = self._deleteNode(currentNode.left, value)
        elif (value > currentNode.value):
            currentNode.right = self._deleteNode(currentNode.right, value)
        else:  
            if (currentNode.left is None):
                return currentNode.right
            elif (currentNode.right is None):
                return currentNode.left
    
            # Get the inorder successor (smallest in the right subtree)
            temp_node = self._getMinValueNodeIter(currentNode.right)
    
            # Copy the inorder successor's content to this node
            currentNode.value= temp_node.value
    
            # Delete the inorder successor
            currentNode.right = self._deleteNode(currentNode.right, temp_node.value)

        return currentNode
