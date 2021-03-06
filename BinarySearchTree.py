from Node import Node


class BinarySearchTree:
    def __init__(self, values = None):
        self.root = None
        self.numberOfNodes = 0

        self.createTree(values)


    def __str__(self):
        return "BinarySearchTree"

#CREATE_TREE###########################################################

    def createTree(self, values):
        if (values is not None):
            for value in values:
                self.addNode(value)

        return self

#NUMBER_OF_NODES#######################################################

    def getNumberOfNodes(self):
        return self.numberOfNodes

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


    def printNumberOfNodes(self):
        print("NUMBER_OF_NODES:", self.getNumberOfNodes())

#ADD_NODE##############################################################

    def addNode(self, value):
        if (value is not None):
            self.root = self._addNode(self.root, value)


    def _addNode(self, currentNode, value):                                 
        if (currentNode is None):                                           # KORZE?? PUSTY -> UTW??RZ NOWY W??ZE??
            self.numberOfNodes += 1
            return Node(value)
        elif (value < currentNode.value):                                   # KORZE?? ZA DU??Y -> WYKONAJ DODANIE W??Z??A NA LEWYM PODDRZEWIE
            currentNode.left = self._addNode(currentNode.left, value)
        elif (value > currentNode.value):                                   # KORZE?? ZA MA??Y -> WYKONAJ DODANIE W??Z??A NA PRAWYM PODDRZEWIE
            currentNode.right = self._addNode(currentNode.right, value)

        return currentNode                                                  # ZWR???? W??ZE?? (JE??LI WARTO???? ISTNIEJE W DRZEWIE W??ZE?? JEST NIEZMIENIONY)

#FIND_NODE#############################################################

    def findNode(self, value):
        if (self.root is not None and value is not None):
            return self._findNode(self.root, value)
        else:
            return None


    def _findNode(self, currentNode, value):
        if (currentNode is None):                                           # KORZE?? PUSTY -> BRAK W??Z??A W DRZEWIE
            return None
        elif (value < currentNode.value):                                   # KORZE?? ZA DU??Y -> SZUKAJ W LEWYM PODDRZEWIE
            return self._findNode(currentNode.left, value)
        elif (value > currentNode.value):                                   # KORZE?? ZA MA??Y -> SZUKAJ W PRAWYM PODDRZEWIE
            return self._findNode(currentNode.right, value)
        else:                                                               # KORZE?? R??WNY -> ZWR???? ZNALEZIONY W??ZE??
            return currentNode

#DELETE_NODE###########################################################

    def deleteNode(self, value):
        if (value is not None):
            self.root = self._deleteNode(self.root, value)


    def _deleteNode(self, currentNode, value):
        if (currentNode is None):                                               # KORZE?? PUSTY -> BRAK W??Z??A W DRZEWIE
            return None
        elif (value < currentNode.value):                                       # KORZE?? ZA DU??Y -> WYKONAJ USUWANIE W??Z??A NA LEWYM PODDRZEWIE
            currentNode.left = self._deleteNode(currentNode.left, value)
        elif (value > currentNode.value):                                       # KORZE?? ZA MA??Y -> WYKONAJ USUWANIE W??Z??A NA PRAWYM PODDRZEWIE
            currentNode.right = self._deleteNode(currentNode.right, value)
        else:                                                                   # KORZE?? R??WNY 
            if (currentNode.right is None):                                     # KORZE?? NIE MA DZIECI -> USU?? KORZE??
                self.numberOfNodes -= 1
                return currentNode.left
            if (currentNode.left is None):                                      # KORZE?? MA TYLKO JEDNO DZIECKO -> POD????CZ DZIECKO DO RODZICA KORZENIA I USU?? KORZE??
                self.numberOfNodes -= 1
                return currentNode.right

            temp_node = currentNode                                             # KORZE?? MA DW??JK?? DZIECI -> ZAST??P KORZE?? JEGO NAST??PNIKIEM (NAJMNIEJSZYM ELEMENTEM Z PRAWEGO PODDRZEWA)
                                                                                # PRAWE PODDRZEWO NAST??PNIKA PRZEPNIJ DO LEWEGO PODDRZEWA JEGO RODZICA
            currentNode = self._getMinValueNodeRec(temp_node.right)

            currentNode.right = self._deleteMinValueNode(temp_node.right)

            currentNode.left = temp_node.left

            self.numberOfNodes -= 1

        return currentNode
    

    def _deleteMinValueNode(self, currentNode):
        if (currentNode.left is None):
            return currentNode.right

        currentNode.left = self._deleteMinValueNode(currentNode.left)

        return currentNode

