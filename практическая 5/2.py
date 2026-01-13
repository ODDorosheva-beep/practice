print("Калькулятор ИМТ")

weight, height = input("Введите ваш вес (кг) и рост(м):").split()
weight = float(weight)
height = float(height)
imt = (weight/(height**2))
print(f"Ваш ИМТ равен {imt:,.1f}")


