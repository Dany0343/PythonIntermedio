def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    num = int(input("Introduce un numero: "))
    print(divisors(num))
    print("El programa terminó")


if __name__ == '__main__':
    run()