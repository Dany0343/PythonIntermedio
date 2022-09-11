def divisors(num):
    divisors = []
    assert num > 0, "Debes ingresar un número positivo"
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Introduce un numero: ") # No se castea, va directamente a la línea del assert
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num))) #Aqui si se castea
    print("El programa terminó")


if __name__ == '__main__':
    run()