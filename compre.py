def run():
    # numbers = []
    # for i in range(1, 101):
    #     if not (i % 3) == 0:
    #         numbers.append(i ** 2)

    # List comprehensions
    squares = [i ** 2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

    test = [i for i in range(1, 1000000) if (i % 4 == 0) and (i % 6 == 0) and (i % 9 == 0)]
    print(test)


if __name__ == '__main__':
    run()