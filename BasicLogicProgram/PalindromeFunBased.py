def palindrome(num):
    x1 = num[::-1]
    if x1 == num:
        print('palindrome')
    else:
        print('not a palindrome')

print(palindrome('AArAA'))