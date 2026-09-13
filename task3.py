#Батури Каріни ІТ - 31
def get_initials(name: str, surname: str) -> str:
    return f"{name[0].upper()}.{surname[0].upper()}."


def count_letters(text: str, letter: str = "a") -> int:
    """Return how many times letter occurs in text."""
    count = 0
    for char in text.lower():
        if char == letter.lower():
            count += 1
    return count


def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


def reverse_text(text: str) -> str:
    reversed_str = ""
    for char in text:
        reversed_str = char + reversed_str
    return reversed_str


name = "Karina"
surname = "Batura"

print(f"{name} {surname}, IT-31")
print(f"Initials: {get_initials(name, surname)}")

c = len(surname)
vowels = count_vowels(surname)
consonants = c - vowels

print(f"Letters in surname: {c}")
print(f"Vowels: {vowels}, consonants: {consonants}")

for v in "aeiou":
    print(f"{v}: {count_letters(surname, letter=v)}")

print(f"Default letter 'a': {count_letters(surname)}")
print(f"Reversed surname: {reverse_text(surname)}")
print(f"Docstring: {count_letters.__doc__}")
print(f"Annotations: {count_letters.__annotations__}")