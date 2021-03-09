a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def commonElem(a, b):
    common = []
    [(common.append(i)) for i in a if i in b and i not in common]
    return common

# def commonElem(a, b):
#     common = []
#     for i in a:
#         for j in b:
#             if i == j and not checkDupes(i, common):
#                 common.append(i)
#     return common
#
# def checkDupes(a, list):
#     for i in list:
#         if i == a:
#             return True
#     return False

print(commonElem(a, b))
