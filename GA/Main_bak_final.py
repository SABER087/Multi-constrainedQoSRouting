# coding=utf-8
# Author:Lixinming
from os import system
from sys import argv


class GlobalInfo:
    data_list = {
        # coef  Pc    Pm
        "new":
            [
                [0.3, 0.9, 0.1],
                [0.3, 0.9, 0.2],
                [0.3, 0.9, 0.3],
                [0.3, 0.9, 0.4],
                [0.3, 0.8, 0.1],
                [0.3, 0.8, 0.2],
                [0.3, 0.8, 0.3],
                [0.3, 0.8, 0.4],
                [0.3, 0.7, 0.1],
                [0.3, 0.7, 0.2],
                [0.3, 0.7, 0.3],
                [0.3, 0.7, 0.4],
                [0.3, 0.6, 0.1],
                [0.3, 0.6, 0.2],
                [0.3, 0.6, 0.3],
                [0.3, 0.6, 0.4],

                [0.4, 0.9, 0.1],
                [0.4, 0.9, 0.2],
                [0.4, 0.9, 0.3],
                [0.4, 0.9, 0.4],
                [0.4, 0.8, 0.1],
                [0.4, 0.8, 0.2],
                [0.4, 0.8, 0.3],
                [0.4, 0.8, 0.4],
                [0.4, 0.7, 0.1],
                [0.4, 0.7, 0.2],
                [0.4, 0.7, 0.3],
                [0.4, 0.7, 0.4],
                [0.4, 0.6, 0.1],
                [0.4, 0.6, 0.2],
                [0.4, 0.6, 0.3],
                [0.4, 0.6, 0.4],

                [0.5, 0.9, 0.1],
                [0.5, 0.9, 0.2],
                [0.5, 0.9, 0.3],
                [0.5, 0.9, 0.4],
                [0.5, 0.8, 0.1],
                [0.5, 0.8, 0.2],
                [0.5, 0.8, 0.3],
                [0.5, 0.8, 0.4],
                [0.5, 0.7, 0.1],
                [0.5, 0.7, 0.2],
                [0.5, 0.7, 0.3],
                [0.5, 0.7, 0.4],
                [0.5, 0.6, 0.1],
                [0.5, 0.6, 0.2],
                [0.5, 0.6, 0.3],
                [0.5, 0.6, 0.4],

                [0.6, 0.9, 0.1],
                [0.6, 0.9, 0.2],
                [0.6, 0.9, 0.3],
                [0.6, 0.9, 0.4],
                [0.6, 0.8, 0.1],
                [0.6, 0.8, 0.2],
                [0.6, 0.8, 0.3],
                [0.6, 0.8, 0.4],
                [0.6, 0.7, 0.1],
                [0.6, 0.7, 0.2],
                [0.6, 0.7, 0.3],
                [0.6, 0.7, 0.4],
                [0.6, 0.6, 0.1],
                [0.6, 0.6, 0.2],
                [0.6, 0.6, 0.3],
                [0.6, 0.6, 0.4],

                [0.7, 0.9, 0.1],
                [0.7, 0.9, 0.2],
                [0.7, 0.9, 0.3],
                [0.7, 0.9, 0.4],
                [0.7, 0.8, 0.1],
                [0.7, 0.8, 0.2],
                [0.7, 0.8, 0.3],
                [0.7, 0.8, 0.4],
                [0.7, 0.7, 0.1],
                [0.7, 0.7, 0.2],
                [0.7, 0.7, 0.3],
                [0.7, 0.7, 0.4],
                [0.7, 0.6, 0.1],
                [0.7, 0.6, 0.2],
                [0.7, 0.6, 0.3],
                [0.7, 0.6, 0.4],

                [0.8, 0.9, 0.1],
                [0.8, 0.9, 0.2],
                [0.8, 0.9, 0.3],
                [0.8, 0.9, 0.4],
                [0.8, 0.8, 0.1],
                [0.8, 0.8, 0.2],
                [0.8, 0.8, 0.3],
                [0.8, 0.8, 0.4],
                [0.8, 0.7, 0.1],
                [0.8, 0.7, 0.2],
                [0.8, 0.7, 0.3],
                [0.8, 0.7, 0.4],
                [0.8, 0.6, 0.1],
                [0.8, 0.6, 0.2],
                [0.8, 0.6, 0.3],
                [0.8, 0.6, 0.4],

                [0.9, 0.9, 0.1],
                [0.9, 0.9, 0.2],
                [0.9, 0.9, 0.3],
                [0.9, 0.9, 0.4],
                [0.9, 0.8, 0.1],
                [0.9, 0.8, 0.2],
                [0.9, 0.8, 0.3],
                [0.9, 0.8, 0.4],
                [0.9, 0.7, 0.1],
                [0.9, 0.7, 0.2],
                [0.9, 0.7, 0.3],
                [0.9, 0.7, 0.4],
                [0.9, 0.6, 0.1],
                [0.9, 0.6, 0.2],
                [0.9, 0.6, 0.3],
                [0.9, 0.6, 0.4],
            ],

        # r Pc Pm
        "old":
            [
                [2.0, 0.9, 0.1],
                [2.0, 0.9, 0.2],
                [2.0, 0.9, 0.3],
                [2.0, 0.9, 0.4],
                [2.0, 0.8, 0.1],
                [2.0, 0.8, 0.2],
                [2.0, 0.8, 0.3],
                [2.0, 0.8, 0.4],
                [2.0, 0.7, 0.1],
                [2.0, 0.7, 0.2],
                [2.0, 0.7, 0.3],
                [2.0, 0.7, 0.4],
                [2.0, 0.6, 0.1],
                [2.0, 0.6, 0.2],
                [2.0, 0.6, 0.3],
                [2.0, 0.6, 0.4],

                [3.0, 0.9, 0.1],
                [3.0, 0.9, 0.2],
                [3.0, 0.9, 0.3],
                [3.0, 0.9, 0.4],
                [3.0, 0.8, 0.1],
                [3.0, 0.8, 0.2],
                [3.0, 0.8, 0.3],
                [3.0, 0.8, 0.4],
                [3.0, 0.7, 0.1],
                [3.0, 0.7, 0.2],
                [3.0, 0.7, 0.3],
                [3.0, 0.7, 0.4],
                [3.0, 0.6, 0.1],
                [3.0, 0.6, 0.2],
                [3.0, 0.6, 0.3],
                [3.0, 0.6, 0.4],

                [4.0, 0.9, 0.1],
                [4.0, 0.9, 0.2],
                [4.0, 0.9, 0.3],
                [4.0, 0.9, 0.4],
                [4.0, 0.8, 0.1],
                [4.0, 0.8, 0.2],
                [4.0, 0.8, 0.3],
                [4.0, 0.8, 0.4],
                [4.0, 0.7, 0.1],
                [4.0, 0.7, 0.2],
                [4.0, 0.7, 0.3],
                [4.0, 0.7, 0.4],
                [4.0, 0.6, 0.1],
                [4.0, 0.6, 0.2],
                [4.0, 0.6, 0.3],
                [4.0, 0.6, 0.4],

                [5.0, 0.9, 0.1],
                [5.0, 0.9, 0.2],
                [5.0, 0.9, 0.3],
                [5.0, 0.9, 0.4],
                [5.0, 0.8, 0.1],
                [5.0, 0.8, 0.2],
                [5.0, 0.8, 0.3],
                [5.0, 0.8, 0.4],
                [5.0, 0.7, 0.1],
                [5.0, 0.7, 0.2],
                [5.0, 0.7, 0.3],
                [5.0, 0.7, 0.4],
                [5.0, 0.6, 0.1],
                [5.0, 0.6, 0.2],
                [5.0, 0.6, 0.3],
                [5.0, 0.6, 0.4],
            ]
    }


if __name__ == "__main__":
    test_file = ""
    if len(argv)!=2:
        test_file = "test03_new"
    else:
        test_file = argv[1]
    # print test_file
    # exit(0)
    input_list = None
    input_list = GlobalInfo.data_list["new"]
    # print input_list
    for input in input_list:
        s = ""
        for param in input:
            s += (" " + str(param))
            system("python ga_statistics_with_calculate_fitness_new.py" + s + " "+test_file)

    input_list = GlobalInfo.data_list["old"]
    # print input_list
    for input in input_list:
        s = ""
        for param in input:
            s += (" " + str(param))

            system("python ga_statistics_with_calculate_fitness_old.py" + s + " "+test_file)