from decimal import Decimal

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
