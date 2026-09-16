# Завдання 2, Батура ІТ - 31
print("Karina Batura, IT-31")
n = int(input("Enter an integer:"))
if not n:
    print("the number was not given")
else:
    number = int(n)

    if number > 0:
      print("number is positive")
    elif n < 0:
        print("number is negative")
    else:
        print("number is 0")

    if number != 0:
        if number % 2 == 0:
            print("number is even")
        else:
            print("numder is odd")
        if (10 <= number <= 99) or (-99 <= number <= -10):
            print("The number is two-digit")