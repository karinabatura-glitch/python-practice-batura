#Батури Каріни ІТ - 31
def print_card():
    print("Каріна Батура, ІТ-31, 2009")


print_card()
print_card()
print_card()


def print_card_args(name, surname, year, group="ІТ-31"):
    print(f"{name} {surname}, {group}, {year}")


print_card_args("Каріна", "Батура", 2009, "ІТ-31")
print_card_args(surname="Батура", year=2009, name="Каріна", group="ІТ-31")
print_card_args("Каріна", "Батура", group="ІТ-31", year=2009)
print_card_args("Каріна", "Батура", 2009)