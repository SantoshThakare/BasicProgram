def fact(num):
    facto = 1
    if num < 0:
        print("does not exist -ve number")
    elif num == 0:
        print("factorial number 0 is : 1")

    else:
        for i in range (1,num+1):
            facto = facto * i
        print("factorial  is", num ,"is ", facto)


if __name__ == '__main__':
    fact(8)