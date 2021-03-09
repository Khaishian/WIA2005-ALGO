a = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89,89]

def filterDupes(a):
    list = []
    [(list.append(i)) for i in a if i not in list]
    return list

print(filterDupes(a))