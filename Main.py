import matplotlib.pyplot as plt

from BinarySearchTree import BinarySearchTree
from AVLTree import AVLTree
from Utils import Utils


def run(list_of_lists):
    Utils.start_measurements(BinarySearchTree, BinarySearchTree.createTree, list_of_lists)

    Utils.start_measurements(AVLTree, AVLTree.createTree, list_of_lists)

    plt.close()

    Utils.start_measurements(BinarySearchTree, BinarySearchTree.findNode, list_of_lists)

    Utils.start_measurements(AVLTree, AVLTree.findNode, list_of_lists)

    plt.close()

    # list_of_lists = Utils.generate_list_of_lists(10000, 100000, 10000)

    Utils.start_measurements(BinarySearchTree, BinarySearchTree.deleteNode, list_of_lists)

    Utils.start_measurements(AVLTree, AVLTree.deleteNode, list_of_lists)

    
if __name__ == "__main__":
    # list_of_lists = Utils.generate_list_of_lists(500000, 600000, 10000)
    # list_of_lists = Utils.generate_list_of_lists(400000, 500000, 10000)
    # list_of_lists = Utils.generate_list_of_lists(100000, 1000000, 100000)
    # list_of_lists = Utils.generate_list_of_lists(10000, 500000, 10000)
    # list_of_lists = Utils.generate_list_of_lists(1000, 200000, 1000)
    list_of_lists = Utils.generate_list_of_lists(10000, 200000, 10000)
    # list_of_lists = Utils.generate_list_of_lists(1000, 10000, 1000)
    # list_of_lists = Utils.generate_list_of_lists(100, 10000, 100)
    # list_of_lists = Utils.generate_list_of_lists(100, 1000, 100)
    # list_of_lists = Utils.generate_list_of_lists(10, 100, 10)
    # list_of_lists = Utils.generate_list_of_lists(10, 50, 10)

    run(list_of_lists)

