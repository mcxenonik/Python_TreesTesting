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

    Utils.start_measurements(BinarySearchTree, BinarySearchTree.deleteNode, list_of_lists)

    Utils.start_measurements(AVLTree, AVLTree.deleteNode, list_of_lists)

    
if __name__ == "__main__":
    # list_of_lists = Utils.generate_list_of_lists(1000000, 100000, 5000000)
    list_of_lists = Utils.generate_list_of_lists(200000, 1000, 1000000)
    
    run(list_of_lists)
