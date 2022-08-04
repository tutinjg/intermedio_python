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
        'language': 'go',
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
        'name': 'Natalia',
        'age': 22,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # RETO - High order functions
    all_python_devs = list(filter(lambda worker:worker['language']=='python', DATA))
    all_python_devs = list(map(lambda worker:worker['name'], all_python_devs))

    # RETO - High order functions
    all_platzi_workers = list(filter(lambda worker:worker['organization']=='Platzi', DATA))
    all_platzi_workers = list(map(lambda worker:worker['name'], all_platzi_workers))

    # clase - List comprehensions
    # all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    # all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']

    # clase High order functions
    # adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    # adults = list(map(lambda worker: worker['name'], adults))
    # old_people = list(map(lambda worker: worker | {'old':worker['age'] > 70}))

    # RETO - List comprehensions
    adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    old_people = [worker['name'] for worker in DATA if worker['age'] > 70]


    for worker in all_python_devs:
        print(worker)
    print('''
        ''')
    for worker in all_platzi_workers:
        print(worker)
    print('''
        ''')
    for worker in adults:
        print(worker)
    print('''
        ''')
    for worker in old_people:
        print(worker)
    print('''
        ''')    


if __name__ == '__main__':
    run()