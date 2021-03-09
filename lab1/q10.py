num = int(input('Enter a number: '))

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            print(i, "x", num // i, "=", num)
            return False
    return True

if isPrime(num):
    print('It is a prime number')
else:
    print('It is not a prime number')

