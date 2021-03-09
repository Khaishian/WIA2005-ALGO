str = input("Enter a sentence: ")

def reverse(str):
    x = str.split()
    rev = ""
    while len(x) > 0:
        rev += x.pop(-1) + " "
    return rev

print(reverse(str))