def student_analysis(marks):
    total = sum(marks)
    average = total / len(marks)

    print("Student Marks Analysis")
    print(f"Marks: {marks}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    print(f"Grade: {grade}")

if __name__ == "__main__":
    marks = []
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        m = int(input(f"Enter mark for subject {i+1}: "))
        marks.append(m)
    student_analysis(marks)
