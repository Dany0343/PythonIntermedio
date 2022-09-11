def divisors(num):
    try:
        if num < 0:
            raise ValueError("Solo se pueden ingresar números positivos")
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors

    except ValueError as ve:
        return ve

def run():
    try:
        num = int(input("Introduce un numero: "))
        print(divisors(num))
        print("El programa terminó")
        
    except ValueError:
        print("Solo se admiten Strings")


if __name__ == '__main__':
    run()