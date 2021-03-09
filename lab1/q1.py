name = input("Enter name: ")
age = int(input("Enter age: "))

def ageCalc(age):
    year = 2021 - age + 100
    print('You will turn 100 at : ' + str(year))

ageCalc(age)

