#Батури Каріни, ІТ - 31
def read_grade(prompt: str) -> int:
    """Запитує в користувача оцінку, доки не буде введено ціле число від 0 до 100."""
    while True:
        value = input(prompt)
        if not value.isdigit():
            print("Помилка: вводити можна лише цифри")
            continue
        grade = int(value)
        if 0 <= grade <= 100:
            return grade
        print("Помилка: значення має бути від 0 до 100")


def to_letter(grade: float) -> str:
    """Перетворює числову оцінку у буквену (A–F), використовуючи декілька return."""
    if grade >= 90:
        return "A"
    if grade >= 82:
        return "B"
    if grade >= 75:
        return "C"
    if grade >= 64:
        return "D"
    if grade >= 60:
        return "E"
    return "F"


def average(grades: list[int]) -> float:
    """Повертає середнє арифметичне для списку оцінок."""
    return sum(grades) / len(grades)


def count_above(grades: list[int], limit: float) -> int:
    """Повертає кількість оцінок, які чітко більші за вказаний ліміт."""
    count = 0
    for g in grades:
        if g > limit:
            count += 1
    return count


def print_report(name: str, group: str, grades: list[int]) -> None:
    """Виводить відформатований звіт для студента за допомогою допоміжних функцій."""
    avg_grade = average(grades)
    letter_grade = to_letter(avg_grade)
    above_avg_count = count_above(grades, avg_grade)
    grades_str = " ".join(str(g) for g in grades)

    print("--- Звіт ---")
    print(f"Студент: {name}, група {group}")
    print(f"Оцінки: {grades_str}")
    print(f"Середній бал: {avg_grade:.2f} -> {letter_grade}")
    print(f"Найкращий: {max(grades)}, найгірший: {min(grades)}")
    print(f"Вище середнього: {above_avg_count}")


def main() -> None:
    """Головна точка входу в програму."""
    name = "Каріна Батура"
    group = "ІТ-31"

    first_name = "Каріна"
    n = max(len(first_name), 3)

    print(f"{name}, {group}")

    grades = []
    for i in range(1, n + 1):
        grade = read_grade(f"Оцінка {i} (0-100): ")
        grades.append(grade)

    print_report(name, group, grades)


main()