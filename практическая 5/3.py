print ("Конверт валют")

USD_TO_RUB = 80.72
usd_to_rub = float(input("введите вашу сумму в долларах:"))
def convert_usd_to_rus(USD_TO_RUS): #вводим новую функцию, раситывающую сумму из долларов в рубли
    return usd_to_rub * USD_TO_RUS #обозначаем, что возвращет нам эта функция
print("Ваша сумма в рублях =", convert_usd_to_rus(USD_TO_RUB))