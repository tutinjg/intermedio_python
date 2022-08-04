def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'Firstname': 'Natalia', 'Lastname': 'Jaramillo'}

    # Lista de Diccionarios
    super_list = [
        {'Firstname': 'Natalia', 'Lastname': 'Jaramillo'},
        {'Firstname': 'Olga', 'Lastname': 'Gonzalez'},
        {'Firstname': 'Luis', 'Lastname': 'Solarte'},
        {'Firstname': 'Esteban', 'Lastname': 'Rojas'}
    ]

    # Diccionario de Listas
    super_dict = {
        'info_natalia' : [1, 'Hello N', True, 22],
        'info_olga' : [2, 'Hello O', True, 49],
        'info_luis' : [3, 'Hello L', True, 47],
        'info_esteban' : [4, 'Hello E', True, 26]
    }


    for key, value in super_dict.items():
        print(key, ' - ', value)


if __name__ == '__main__':
    run()