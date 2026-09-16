d = 23
c = 6

print(f"Numbers from {d} to 31:", end=" ")

count = 0
total_sum = 0
product = 1
even_count = 0
odd_count = 0

for num in range(d, 32):
    print(num, end=" ")
    count += 1
    total_sum += num
    product *= num
    
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print()
average = total_sum / count

print(f"Count: {count}")
print(f"Sum: {total_sum}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
print(f"Even: {even_count}, odd: {odd_count}")

print(f"Numbers from {d} to 31:", end=" ")
#while version
count_w = 0
total_sum_w = 0
product_w = 1
even_count_w = 0
odd_count_w = 0

current = d
while current <= 31:
    print(current, end=" ")
    count_w += 1
    total_sum_w += current
    product_w *= current
    
    if current % 2 == 0:
        even_count_w += 1
    else:
        odd_count_w += 1
        
    current += 1

print()
average_w = total_sum_w / count_w

print(f"Count: {count_w}")
print(f"Sum: {total_sum_w}")
print(f"Product: {product_w}")
print(f"Average: {average_w:.2f}")
print(f"Even: {even_count_w}, odd: {odd_count_w}")

print("Countdown:", end=" ")
for i in range(c, 0, -1):
    print(i, end=" ")
print()