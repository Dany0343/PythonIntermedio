def run():
    dict = {}

    for i in range(1, 101):
        if i % 3 != 0:
            dict[i] = i ** 3

    print(dict)

    # Comprehensions
    dict2 = {}
    print("Comprehensions")
    dict2 = {i: i ** 3 for i in range(1, 101) if i % 3 != 0}
    print(dict2)

    #reto
    dict3 = {}
    print("Reto")
    dict3 = {i: i ** 0.5 for i in range(1, 10001)}
    print(dict3)

if __name__ == '__main__':
    run()