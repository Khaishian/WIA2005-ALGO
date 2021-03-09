a = [5, 10, 15, 20, 25]

def firstLast(list):
    newList = []
    newList.append(list.pop(0))
    newList.append(list.pop(-1))
    return newList

print(firstLast(a))