# Data
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
    ]

def run():
    # Crear las listas allPythonDevs y allPlatziWorkers usando una combinacion de filter y map
    print("Python devs")
    allPythonDevs = list(filter(lambda worker: worker['language'] == 'python', DATA))
    allPythonDevs = list(map(lambda worker: worker['name'], allPythonDevs))
    for i in allPythonDevs:
        print(i)

    print("\nPlatzi Workers")
    allPlatziWorkers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    allPlatziWorkers = list(map(lambda worker: worker['name'], allPlatziWorkers))
    for i in allPlatziWorkers:
        print(i)


    # Crear la lista oldPeople y adults con list comprehensions
    print("\nAdults")
    adults = [worker['name'] for worker in DATA if worker['age'] >= 18]
    print(adults)

    print("\nOld people")
    oldPeople = [worker | {"old": worker["age"] > 70} for worker in DATA]
    for i in oldPeople:
        print(i)

if __name__ == '__main__':
    run()