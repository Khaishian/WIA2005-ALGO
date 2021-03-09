number = int(input('Enter a number: '))

def divisor(num):
    list =[]
    for i in range(num):
        if num%(i+1) == 0:
            list.append(i+1)
    return list

print(divisor(number))