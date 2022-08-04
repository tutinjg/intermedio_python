import numbers


def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('Ingresa un número: '))
        if num < 0:
            raise TypeError('Solo se puede ingresar números positivos')
        print(divisors(num))
        print('Terminó el programa')
    except TypeError as te:
        print(te)
    # except ValueError:
    #     print('Solo se puede ingresar un número')


if __name__ == '__main__':
    run()
