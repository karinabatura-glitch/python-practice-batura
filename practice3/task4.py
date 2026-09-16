print("Karina Batura, IT-31")
score = int(input("Enter your expected score (0-100) "))
missed = int(input("Enter number of missed classes: "))
if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100.")
else:
    if score >= 90:
        ects = "A"
    elif score >= 82:
        ects = "B"
    elif score >= 74:
        ects = "C"
    elif score >= 64:
        ects = "D"
    elif score >= 60:
        ects = "E"
    else:
        ects = "F"

    if score >= 60:
        status = "passed"
    else:
        status = "failed"

    if missed / 16 > 0.30:
        print("not included")
    print(f"Score: {score}, ECTS: {ects}, Status: {status}")