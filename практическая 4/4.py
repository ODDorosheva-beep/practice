print("Мандарины для школьников")

students = int(input("Введите количество школьников:"))
oranges = int(input("Введите количество мандарин:"))

oranges_for_students = oranges // students
oranges_free = oranges % students

print("Каждома школьнику достанется", oranges_for_students, "мандаринов")
print("В корзине останется", oranges_free, "мандарин")