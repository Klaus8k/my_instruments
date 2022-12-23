# n = 5
# tree_parents = [-1, 0, 4, 0, 3]
# tree_parents = [4, -1, 4, 1, 1]

import sys
sys.setrecursionlimit(20)

tree_parents = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]


def serach_2():
    for i in tree_parents:
        