print("Karina Batura, IT-31")

name = "Karina"
surname = "Batura"

f_name = name + surname

vowels = 0
consonants = 0

for char in f_name:
    c = char.lower()
    
    if c in "aeiouy":
        vowels += 1
    elif c.isalpha():
        consonants += 1

total = vowels + consonants

print(f"{name} {surname}")
print(f"Vowels: {vowels}, consonants: {consonants}")
print(f"Total letters: {total}")