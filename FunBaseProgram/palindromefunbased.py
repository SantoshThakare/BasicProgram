def palindrome(num):
    x1 = num[::-1]
    if x1 == num:
        print('palindrome')
    else:
        print('not a palindrome')


if __name__ == '__main__':
    print(palindrome('AArAA'))