from random import randint
from matplotlib import pyplot as plt 
import timeit
from functools import partial

from AVLTree import AVLTree
from BinarySearchTree import BinarySearchTree


if __name__ == "__main__":
    # arr = [randint(1, 1000) for i in range(10)]
    arr = [50, 30, 20, 40, 70, 60, 80]

    bst_tree = BinarySearchTree(arr)
    bst_tree.printLevelorder()
    # bst_tree.printInorder()
    # bst_tree.printTree()

    print("FIND")
    print(bst_tree.findNode(60).value)

    print("DELETE")
    bst_tree.deleteNode(30)
    bst_tree.printLevelorder()
    # bst_tree.printInorder()
    # bst_tree.printTree()

    print("FIND")
    print(bst_tree.findNode(80).value)

  