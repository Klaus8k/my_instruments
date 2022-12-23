import sys
sys.setrecursionlimit(5000)

n = input()
tree_parents = input()
tree_parents = [int(i) for i in tree_parents.split()]

# n = 10
# tree_parents = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]
# n = 5
# tree_parents = [-1, 0, 4, 0, 3]
# tree_parents = [4, -1, 4, 1, 1]

result = []
parent_sons = {}

def sons_dict(x):
    son = 0
    if len(x) == 1:
        result.append(1)
    for parent in x:
        if parent in parent_sons.keys():
            parent_sons[parent].append(son)
        else:
            parent_sons[parent] = [son,]
        son += 1



def search(parent, sons_list, higth=1):

    if parent in parent_sons.keys():
        higth += 1
        result.append(higth)
        # print(higth)
        # print(parent_sons[parent])
        for i in sons_list:
            if i in parent_sons.keys():
                sons_list = parent_sons[i]
                search(i, sons_list , higth)
        
    return higth

# tree_parents = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]

def serach_2(index = 0):
    count += 1
    for i in tree_parents:
        index = tree_parents.index(i) 
        if index in tree_parents:
            serach_2(index)
        else:
            result.append(count)
            count = 0
            
        




# {9: [0, 5, 6, 7, -1], 7: [1], 5: [2, 3], 2: [4, 8]}
# {9: [0, 5, 6, 7], 7: [1], 5: [2, 3], 2: [4, 8], -1: [9]}

sons_dict(tree_parents)
# print(parent_sons)


for i in parent_sons.keys():
    if len(parent_sons.keys()) == 1:
        result.append(1)
        
    if i == -1:
        parent_start = parent_sons[i][0]
        search(parent_start ,parent_sons[parent_start])

print(max(result))