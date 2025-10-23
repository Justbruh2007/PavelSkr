import math

a = int(input(print("Введите число а:")))
if a**2 + 1 > -1:
    x = (a**2 + 10) / math.sqrt(a**2 + 1)
    print(x)
else:
    print('Не решаемо')