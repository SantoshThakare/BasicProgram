
my_list = [10, 40, 50, 60, 100, 33, 46]
maximum = my_list[0]
minimum = my_list[0]
for number in my_list:
    if number > maximum:
        maximum = number
    elif number < minimum:
        minimum = number
print(f' the maximum number is :{maximum} \n& the minimum is {minimum} ')