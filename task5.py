print("Karina Batura, IT-31")

d = 23
c = 6
n = d * c

print(f"n = {d} * {c} = {n}")

div_count = 0
div_sum = 0

print("Divisors:", end=" ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        div_count += 1
        div_sum += i
print()

print(f"count: {div_count}, sum: {div_sum}")

if n < 2:
    print(f"{n} is not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime")
            break
    else:
        print(f"{n} is prime")

primes_count = 0

print(f"Primes up to {n}:", end=" ")
for num in range(2, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        primes_count += 1
print()

print(f"Primes count: {primes_count}")