print("Перевод минуты в часы")

minutes = int(input("Введите минуты:"))
hour = minutes // 60
minutes_remains = minutes % 60
print(minutes, "мин - это", hour, "час", minutes_remains, "минут")