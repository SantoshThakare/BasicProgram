def replace(name):

    sentence = "Hello <<Username>> ,How are you ?"
    change = sentence.replace('<<Username>>', name)
    return change


if __name__ == '__main__':
    userName = input("Enter Username :")
    print(replace(userName))