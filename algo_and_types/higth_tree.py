n = 10
x = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]
# n = 5
# x = [-1, 0, 4, 0, 3]

sons = {}

def req():
    count = 0
    for i in x:

        if i in sons.keys():
            sons[i].append(count)
        elif i == -1:
            sons[count].append(-1)
        else:
            sons[i] = [count,]
        count += 1

def search(sons_list): # Здесь рекурсивную функцию для обхода списков сыновей
    
    for i in sons_list:
        search(sons[i])

req()
    
for i in sons.values():
    if -1 in i:
        i.remove(-1)
        search(i)    
    




print(sons)
