list = [10, 5, 2, 7, 8, 7]
maxVal =list[0]
for i in range(0, len(list)):
    if maxVal< list[i]:
        maxVal= list[i]

    if __name__ == "__main__":
        print(maxVal)