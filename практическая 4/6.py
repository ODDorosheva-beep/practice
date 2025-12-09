print("Тригонометрические выражения")
import math

num = float(input("Введите значение 'X' (градусы):"))
degrees = math.radians(num)
sin = math.sin(degrees)
cos = math.cos(degrees)
tg = math.tan(degrees)

result = sin + cos + (tg**2)
print(result)
