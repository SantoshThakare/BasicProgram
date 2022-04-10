a = int(input('Enter the 1st Number\n'))
b = int(input('Enter the 2st Number\n'))
n = int(input('enter the element of elements\n'))

print(a, b, end=" ")
while n-2:
    c = a+b
    a = b
    b = c
    print(c, end=" ")
    n= n-1