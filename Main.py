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

    bst_tree.print_inorder()

    print("DELETE")
    bst_tree.deleteNode(100)

    # bst_tree.print_inorder()
    bst_tree.print_tree()