number_os_students = int(input())
number_of_lectures = int(input())
bonus = int(input())
students_attendances = []
for i in range(number_os_students):
    student_attendances = int(input())
    students_attendances.append(student_attendances)
if students_attendances:
    max_student_attendances = max(students_attendances)
    max_bonus_points = max_student_attendances / number_of_lectures * (5 + bonus)
    print(f"Max Bonus: {round(max_bonus_points)}.")
    print(f"The student has attended {max_student_attendances} lectures.")
else:
    print("Max Bonus: 0.")
    print("The student has attended 0 lectures.")