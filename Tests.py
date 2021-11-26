from random import sample

from BinarySearchTree import BinarySearchTree
from AVLTree import AVLTree
from Utils import Utils

# from binarytree import tree, bst, heap, Node


if __name__ == "__main__":
    # list_of_lists = Utils._generate_list_of_lists(1000000, 100000, 100000000)
    # list_of_lists = Utils._generate_list_of_lists(50, 10, 1000)
    
    # print("MAIN LENGTH:", len(list_of_lists))

    # for list in list_of_lists:
    #     print("LENGTH:", len(list))
    #     print(list)

#########################################################

    arr = sample(range(1, 100), 55)             # 55
    # arr = list_of_lists[-1]
    # arr = [23, 763, 26, 1, 74, 3, 765, 146, 95, 482, 326, 42, 841, 11, 327, 45, 643, 89]
    # arr = [20, 30, 40, 50, 60, 70, 80]
    # arr = [50, 30, 20, 40, 70, 60, 80]
    # arr = [5, 10]

#########################################################

    print("TREE GENERATED")
    bst_tree = BinarySearchTree(arr)
    bst_tree.printNumberOfNodes()
    bst_tree.printBetterTree()

    # print("FIND")
    # print(bst_tree.findNode(60).value)

    # print("DELETE")
    # bst_tree.deleteNode(50)
    # bst_tree.printBetterTree()

    # print("ADD")
    # bst_tree.addNode(45)
    # bst_tree.printBetterTree()

#########################################################

    print("TREE GENERATED")
    avl_tree = AVLTree(arr)
    avl_tree.printNumberOfNodes()
    avl_tree.printBetterTree()

    # print("FIND")
    # print(avl_tree.findNode(60).value)

    # print("DELETE")
    # avl_tree.deleteNode(50)
    # avl_tree.printBetterTree()

    # print("ADD")
    # avl_tree.addNode(45)
    # avl_tree.printBetterTree()

#########################################################
