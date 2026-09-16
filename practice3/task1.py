print("Karina Batura, IT-31")

name = input("Enter your name: ")
age_i = input("Enter your age: ")

if not name:
    print("name not entered.")
    name = "Anonymous"

if not age_i:
    print("age not entered!")
else:
    age = int(age_i)

    if age < 0:
        category = "invalid age value"
    elif age <= 6:
        category = "child"
    elif age <= 17:
        category = "schoolchild"
    elif age <= 64:
        category = "adult"
    else:
        category = "senior"

    print(f"Hello, {name}! Your age category is: {category}.")