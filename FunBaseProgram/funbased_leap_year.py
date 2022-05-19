def leap_year(year):

    if year % 100 != 0 and year % 4 == 0:
        print("{} is a leap year".format(year))
    elif year % 100 == 0 and year % 400 == 0:
        print("{} is century leap year".format(year))
    else:
        print("{} is not a leap year".format(year))

if __name__ == '__main__':
    input_year = int(input("Enter year :"))
    leap_year(input_year)