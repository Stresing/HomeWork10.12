from decimal import Decimal
import math
from random import randint


def Task1():
    d = str(input("Введите число точности : "))
    n = float(input('Ведите второе число: '))
    nope_int = Decimal(d) % 1
    some_list = list(str(nope_int))
    if nope_int != 0:
        some_list.remove("0")
        some_list.remove('.')
        print(format(n, f'10.{len(some_list)}f'))
    else:
        print(int(n))


def Task2():
    N = int(input("Введите простое число: "))
    some_list = []
    for i in range(2, int(math.sqrt(N)) + 1):
        while (N % i == 0):
            some_list.append(i)
            N //= i

    if (N != 1):
        some_list.append(N)
        print(some_list)


def Task3():
    some_list = list(map(int, input("Для заполнение списка, введите числа через пробел: ").split()))
    some_two_list = []
    print(some_list)
    for i in some_list:
        if i not in some_two_list:
            some_two_list.append(i)
    print(some_two_list)


def Task4():
    with open('file', 'w', encoding='utf-8') as g:
        max = 100
        k = int(input('Введите натуральную степень k: '))
        koff = [randint(0, max) for i in range(k)] + [randint(1, max)]
        n = '+'.join([f'{(j, "")[j == 1]}x^{i}' for i, j in enumerate(koff) if j][::-1])
        n = n.replace('x^1+', 'x+')
        n = n.replace('x^0', '')
        n += ('', '1')[n[-1] == '+']
        n = (n, n[:-2])[n[-2:] == '^1']
        g.write(n)


task = int(input('Введите номер(1-4) задания: '))
if task == 1:
    Task1()
elif task == 2:
    Task2()
elif task == 3:
    Task3()
elif task == 4:
    Task4()
# elif task == 5:
#     Task5()
