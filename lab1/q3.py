a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def filterLess5(list):
    a = []
    for i in list:
        if i < 5:
            a.append(i)
    return a

print(filterLess5(a))
