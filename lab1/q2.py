number = int(input('Enter a number: '))

def isEven(num):
    if num % 2 == 0:
        return 'It is an even number'
    else:
        return 'It is an odd number'

print(isEven(number))
