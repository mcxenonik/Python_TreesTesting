import matplotlib.pyplot as plt
from random import sample

import time
import gc


class Utils():
    def __init__(self):
        pass
    
    
    @staticmethod
    def generate_list_of_lists(max_number_of_ele=10000, step_number_of_ele=1000, values_range=30000):
        table = sample(range(1, values_range), max_number_of_ele)
        list_of_lists = []

        for number_of_ele in range(step_number_of_ele, len(table) + step_number_of_ele, step_number_of_ele):
            list_of_lists.append(table[:number_of_ele])

        return list_of_lists


    def _draw_plot(tree_name, function_name, xpoints, ypoints):
        figure1 = plt.figure()
        plt.plot(xpoints, ypoints, marker='o')
        plt.title(tree_name + "_" + function_name)
        plt.xlabel("Number of elements")
        plt.ylabel("Process time [s]")
        plt.savefig(tree_name + "_" + function_name + ".png")
        # plt.show()
        plt.close(figure1)

        # plt.semilogy(xpoints, ypoints, marker='o', label=tree_name)
        plt.plot(xpoints, ypoints, marker='o', label=tree_name)
        plt.title("All trees" + "_" + function_name)
        plt.xlabel("Number of elements")
        plt.ylabel("Process time [s]")
        plt.legend(loc="upper left")
        plt.savefig("All trees" + "_" + function_name + ".png")
        # plt.show()


    def _measure_time(tree, function, argument):
        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        function(tree, argument)
        stop = time.process_time()

        if (gc_old): 
            gc.enable()

        return stop - start


    @staticmethod
    def start_measurements(tree, function, list_of_lists):
        tree_name = str(tree())
        function_name = function.__name__
        xpoints = []
        ypoints = []

        print(tree_name, function_name, "\n--------------")

        if (function_name == "createTree"):
            created_tree = tree()
        else:
            created_tree = tree().createTree(list_of_lists[-1])
        

        for list_of_elements in list_of_lists:     
            if (function_name == "createTree"):
                process_time = Utils._measure_time(created_tree, function, list_of_elements)
            else:
                process_time = 0
                for element in list_of_elements:
                    process_time += Utils._measure_time(created_tree, function, element)

            ypoints.append(process_time)
            xpoints.append(len(list_of_elements))

            print("PROCESS TIME:", format(process_time, '.10f'), "FOR", len(list_of_elements), "ELEMENTS")

        Utils._draw_plot(tree_name, function_name, xpoints, ypoints)

