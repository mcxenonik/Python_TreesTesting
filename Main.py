from Utils import Utils

from AVLTree import AVLTree
from BinarySearchTree import BinarySearchTree

from AVLTree2 import AVLTree2
from BinarySearchTree2 import BinarySearchTree2

# from binarytree import tree, bst, heap, Node


def run(list_of_lists):
    # Utils.start_measurements(BinarySearchTree, "createTree", list_of_lists)

    # Utils.start_measurements(AVLTree, "createTree", list_of_lists)

    # Utils.start_measurements(BinarySearchTree, "findNode", list_of_lists)

    # Utils.start_measurements(AVLTree, "findNode", list_of_lists)

    Utils.start_measurements(BinarySearchTree, "deleteNode", list_of_lists)

    Utils.start_measurements(AVLTree, "deleteNode", list_of_lists)


if __name__ == "__main__":
    list_of_lists = Utils._generate_list_of_lists(1000000, 100000, 100000000)
    
    run(list_of_lists)