def run():
    myList = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x ** 2, myList))
    print(squares)


if __name__ == '__main__':
    run()