from random import randint

from AVLTree import AVLTree
from BinarySearchTree import BinarySearchTree

# from binarytree import tree, bst, heap, Node


if __name__ == "__main__":
    arr = [randint(1, 1000) for i in range(50)]
    # arr = [20, 30, 40, 50, 60, 70, 80]
    # arr = [50, 30, 20, 40, 70, 60, 80]

#########################################################

    print("TREE GENERATED")
    bst_tree = BinarySearchTree(arr)
    bst_tree.printBetterTree()
    # bst_tree.printLevelorder()
    # bst_tree.printTree()

    # print("FIND")
    # print(bst_tree.findNode(60).value)

    # print("DELETE")
    # bst_tree.deleteNode(50)
    bst_tree.printBetterTree()
    # bst_tree.printLevelorder()
    # bst_tree.printTree()

    # print("ADD")
    # bst_tree.addNode(45)
    bst_tree.printBetterTree()
    # bst_tree.printLevelorder()
    # bst_tree.printTree()

#########################################################

    print("TREE GENERATED")
    avl_tree = AVLTree(arr)
    avl_tree.printBetterTree()
    # avl_tree.printLevelorder()
    # avl_tree.printTree()

    # print("FIND")
    # print(avl_tree.findNode(60).value)

    # print("DELETE")
    # avl_tree.deleteNode(50)
    # avl_tree.printBetterTree()
    # avl_tree.printLevelorder()
    # avl_tree.printTree()

    # print("ADD")
    # avl_tree.addNode(45)
    # avl_tree.printBetterTree()
    # avl_tree.printLevelorder()
    # avl_tree.printTree()

  