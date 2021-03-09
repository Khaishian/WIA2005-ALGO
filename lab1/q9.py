import random

def randomGuess():
    ran = random.randint(1, 9)
    num = int(input('Guess the number[1-9]: '))
    while True:
        if num == ran:
            print('Correct! It is ' + str(ran))
            return
        elif num < ran:
            print('Too low!')
        else:
            print('Too High!')
        num = int(input('Guess the number again[1-9]: '))

randomGuess()