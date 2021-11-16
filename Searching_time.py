from random import randint
from matplotlib import pyplot as plt 
import timeit
from functools import partial

from AVLTree import AVLTree
from BinarySearchTree import BinarySearchTree

arr = [randint(1, 3000) for i in range(11000)]
list_of_lists = []
number_of_elements = []
bst_creation_time = []
avl_creation_time = []
bst_finding_time = []
avl_finding_time = []

for n in range(0, len(arr) - 1, 1000):
    list_of_lists.append(arr[:n])

for n in list_of_lists:
    number_of_elements.append(len(n))

avl_tree = AVLTree(arr)
bst_tree = BinarySearchTree(arr)


for small_list in list_of_lists:
    bst_time = partial(BinarySearchTree, small_list)
    bst_creation_time.append(timeit.timeit(bst_time, number=1))
    avl_time = partial(AVLTree, small_list)
    avl_creation_time.append(timeit.timeit(avl_time, number=1))

    bst_find = 0
    avl_find = 0
    for element in small_list:
        search_bst = partial(bst_tree.findNode, element)
        bst_find += timeit.timeit(search_bst, number=1)
        search_avl = partial(avl_tree.findNode, element)
        avl_find += timeit.timeit(search_avl, number=1)
    bst_finding_time.append(bst_find)
    avl_finding_time.append(avl_find)



with open("trees_output.txt", "w") as out:
    time_iterator = 0
    for small_list in list_of_lists:
        out.write("Number of elements: {:d}\n".format(len(small_list)))
        out.write("Binary Search Tree construdction time: {:f}s\n".format(bst_creation_time[time_iterator]))
        out.write("AVL Tree construdction time: {:f}s\n".format(avl_creation_time[time_iterator]))
        out.write("Binary Search Tree search time: {:f}s\n".format(bst_finding_time[time_iterator]))
        out.write("AVL Tree search time: {:f}s\n".format(avl_finding_time[time_iterator]))
        out.write("\n\n")
        time_iterator += 1


fig1, ax1 = plt.subplots(nrows = 2, ncols = 1, figsize = (6, 7))
fig1.suptitle("Trees' Creation Time", fontsize = 16)
ax1[0].plot(number_of_elements, bst_creation_time, "b")
ax1[1].plot(number_of_elements, avl_creation_time, "g")

ax1[0].set_ylabel("Time in seconds of creating BST Tree")
ax1[1].set_ylabel("Time in seconds of creating AVL Tree")

ax1[0].set_xlabel("Number of elements in tree")
ax1[1].set_xlabel("Number of elements in tree")


fig2, ax2 = plt.subplots(nrows = 2, ncols = 1, figsize = (6, 7))
fig2.suptitle("Trees' Searching Time", fontsize = 16)
ax2[0].plot(number_of_elements, bst_finding_time, "b")
ax2[1].plot(number_of_elements, avl_finding_time, "g")

ax2[0].set_ylabel("Time in seconds of finding the node in BST Tree")
ax2[1].set_ylabel("Time in seconds of finding the node in AVL Tree")

ax2[0].set_xlabel("Number of elements in tree")
ax2[1].set_xlabel("Number of elements in tree")

plt.show()