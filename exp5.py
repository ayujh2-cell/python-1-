num_students = int(input("Enter the number of students: "))

class_total = 0

for student in range(1, num_students + 1):
    student_total = 0

    print(f"\nStudent {student}")

    for test in range(1, 6):
        score = float(input(f"Enter score for Test {test}: "))
        student_total += score

    student_average = student_total / 5
    print(f"Average score for Student {student}: {student_average:.2f}")

    class_total += student_average

class_average = class_total / num_students

print(f"\nOverall class average: {class_average:.2f}"
