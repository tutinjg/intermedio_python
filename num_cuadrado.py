def run():
    # list = []
    # for i in range(1, 101):
    #     # Expresión para obtener los NO DIVISIBLES ENTRE 3
    #     if i % 3 !=0:
    #         list.append(i**2)

    # print(list)
    # squares = [i**2 for i in range(1, 101) if i % 3 !=0]

    challenge = [i for i in range(1, 100000) if i % 4 ==0 and i % 6 ==0 and i % 9 ==0]
    print(challenge)


if __name__ == '__main__':
    run()