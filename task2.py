print("Karina Batura, IT-31")

num = int(input("Enter number: "))

n = num

if n < 0:
    n = -n

count = 0
total = 0
rev = 0

if n == 0:
    count = 1
    total = 0
    mx = 0
    mn = 0
    rev = 0
else:
    mx = 0
    mn = 9
    
    while n > 0:
        digit = n % 10
        
        count += 1
        total += digit
        rev = rev * 10 + digit
        
        if digit > mx:
            mx = digit
        if digit < mn:
            mn = digit
            
        n //= 10

print(f"Digits: {count}")
print(f"Sum: {total}")
print(f"Max: {mx}, min: {mn}")
print(f"Reversed: {rev}")