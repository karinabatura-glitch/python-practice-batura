# Завдання 5, Батура ІТ - 31
hb = 23
positive = hb > 0
evnum = hb % 2 == 0
condition = positive and evnum

print(f"День народження ({hb}):")
print(f"Чи додатне: {positive}")
print(f"Чи парне: {evnum}")
print(f"Обидві умови: {condition}")

month = 3
product = hb * month
positive_prod = product > 0
evnum_prod = product % 2 == 0
condition_prod = positive_prod and evnum_prod

print(f"Добуток дня і місяця ({hb} * {month} = {product}):")
print(f"Чи додатне: {positive_prod}")
print(f"Чи парне: {evnum_prod}")
print(f"Обидві умови (and): {condition_prod}")