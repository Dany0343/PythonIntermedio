def run(): # Se pueden crear diccionarios dentro de listas y viceversa
    myList = [1, "hello", True, 4.5]
    myDict = {"firstName": "Oscar", "lastName": "Bucio"}

    superList = [
        {"firstName": "Oscar", "lastName": "Bucio"},
        {"firstName": "Miguel", "lastName": "Hernandez"},
        {"firstName": "Diego", "lastName": "Valdez"},
        {"firstName": "David", "lastName": "Alcazar"},
        {"firstName": "Alejandro", "lastName": "Martinez"},
    ]

    superDict = {
        "naturalNums": [1, 2, 3, 4, 5],
        "integerNums": [-1, -2, -3, -4, -5],
        "floatingNums": [1.1, 4.5, 6.43]
    }

    for key, value in superDict.items():
        print(key, "-", value)

    print("Super lista")

    for elemento in superList:
        print(elemento["firstName"], "-", elemento["lastName"])

    for element in superList:
        print(f"{element['firstName']} - {element['lastName']}")


if __name__ == '__main__': # El entry poing lo que hace es iniciar la función cuando se ejecuta el archivo
    run()