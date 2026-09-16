#Батури Каріни ІТ - 31
y = 2009

def print_age(year, current_year=2026):
    print(f"Age: {current_year - year}")

def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1
    return current_year - year
    print("after return")


print_age(y)
print(f"print_age returned: {print_age(y)}")

age = get_age(y)
print(f"Age from get_age: {age}")
print(f"Age in months: {age * 12}")
print(f"Age in weeks: {age * 52}")

print(f"Age in 2030: {get_age(y, 2030)}")

print(f"Invalid year 3000 gives: {get_age(3000)}")
