string = input('Enter a string: ')

def isPalindrome(str):
    if str == str[::-1]:
        return 'It is a palindrome'
    else:
        return 'It is not a palindrome'

print(isPalindrome(string))