# High order functions filter
def run():
    myList = [1, 2, 3, 4, 5, 6, 7]
    
    odd = list(filter(lambda x: x % 2 != 0, myList)) # Filter recibe dos argumentos una función y un iterable, por si misma no devuelve una lista, devuelve un iterador
    print(odd)


if __name__ == '__main__':
    run()