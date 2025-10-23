import math
# a)
a = 17
b = -6
c = 13
d = b**2 - 4 * c * a

if d > -1:
    d = math.sqrt(d)

    x1 = (-b - d)/2*a ; print(x1)

    x2 = (-b + d)/2*a ; print(x2)

else:
    print('Не решаемо')



# b)
a = 3
b = 5
c = -21
d = b**2 - 4 * c * a
if d > -1:
    d = math.sqrt(d)

    x1 = (-b - d)/2*a ; print(x1)

    x2 = (-b + d)/2*a ; print(x2)

else:
    print('Не решаемо')
