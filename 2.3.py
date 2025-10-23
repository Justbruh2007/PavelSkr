import math

# a)
a = float(input("Введите a: "))
num_a = 2 * a + math.sin(abs(3 * a))
if num_a < 0:
    print("Ошибка: подкоренное выражение отрицательное в (a)")
else:
    value_a = math.sqrt(num_a / 3.56)
    print(f"Результат (a): {value_a:.4f}")

# б)
x = float(input("Введите x: "))
if x == 0:
    print("Ошибка: деление на ноль в (б)")
else:
    num_b = 3.2 + math.sqrt(1 + x)
    c = abs(5 * x)
    value_b = num_b / c
    print(f"Результат (б): {value_b:.4f}")