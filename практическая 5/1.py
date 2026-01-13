print("Калькулятор налогов")

TAX_RATE = 0.13
annual_income = float(input("Введите Ваш годовой доход:"))
tax = annual_income * TAX_RATE
income = annual_income - tax
print (f"Общая сумма дохода = {annual_income:,.2f}")
print(f"Сумма расчитанного налога = {tax:,.2f}")
print(f"Сумма 'на руки, после вычета налога = {income:,.2f}")