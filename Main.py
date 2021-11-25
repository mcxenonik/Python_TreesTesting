from random import randint

from Utils import Utils

from AVLTree import AVLTree
from BinarySearchTree import BinarySearchTree

from AVLTree2 import AVLTree2
from BinarySearchTree2 import BinarySearchTree2

# from binarytree import tree, bst, heap, Node


if __name__ == "__main__":
    # arr = [randint(1, 1000) for i in range(55)]             # 55
    # arr = [20, 30, 40, 50, 60, 70, 80]
    # arr = [50, 30, 20, 40, 70, 60, 80]

#########################################################

    # print("TREE GENERATED")
    # bst_tree = BinarySearchTree(arr)
    # bst_tree.printBetterTree()

    # print("FIND")
    # print(bst_tree.findNode(60).value)

    # print("DELETE")
    # bst_tree.deleteNode(50)
    # bst_tree.printBetterTree()

    # print("ADD")
    # bst_tree.addNode(45)
    # bst_tree.printBetterTree()

#########################################################

    # print("TREE GENERATED")
    # avl_tree = AVLTree(arr)
    # avl_tree.printBetterTree()

    # print("FIND")
    # print(avl_tree.findNode(60).value)

    # print("DELETE")
    # avl_tree.deleteNode(50)
    # avl_tree.printBetterTree()

    # print("ADD")
    # avl_tree.addNode(45)
    # avl_tree.printBetterTree()

#########################################################

    list_of_lists = Utils._generate_list_of_lists(1000000, 100000, 100000000)

    # print("MAIN LENGTH:", len(list_of_lists))

    # for list in list_of_lists:
    #     print("LENGTH:", len(list))
    #     print(list)

    Utils.start_measurements(BinarySearchTree, "create", list_of_lists)

    Utils.start_measurements(AVLTree, "create", list_of_lists)