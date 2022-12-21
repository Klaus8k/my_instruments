# put your python code here
# a = input()
a = '()[]}'
a = list(a)

match = {'(': ')',
         '[': ']',
         '{': '}'}


def match_brakes(stack):
    b = []
    count = 1
    for i in stack:
        count += 1

        print(i)
        if i in match.keys():
            b.append(i)
        elif i in match.values():
            for j in match.keys():
                if match[j] == i and j in b:
                    b.remove(j)
                else: break
            return count # С возвратом разобраться
        else:
            continue



print(match_brakes(a))
