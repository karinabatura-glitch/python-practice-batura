# Завдання 6, Батура ІТ - 31
name = input("Введіть ваше ім'я: ")
age = int(input("Введіть ваш вік: "))

vertification = 18 <= age <= 60
par = age % 2 == 0
b1 = vertification and par 
b2 = vertification or par  

if age <= 60:
    years_left = 60 - age
else:
    years_left = 0

print(f"Користувач: {name}, Вік: {age}")
print(f"Чи потрапляє вік у діапазон від 18 до 60: {vertification}")
print(f"Чи є вік парним числом: {par}")
print(f"Чи виконуються обидві умови одночасно: {b1}")
print(f"Чи виконується хоча б одна умова: {b2}")
print(f"Років залишилося до 60: {years_left}")