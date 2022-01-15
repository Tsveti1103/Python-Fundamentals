data = input()
courses = {}
while data != "end":
    course_name, student_name = data.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    data = input()

sorted_courses = sorted(courses.items(), key=lambda kvpt: -len(kvpt[1]))
for course_name, students in sorted_courses:
    print(f"{course_name}: {len(students)}")
    for name in sorted(students):
        print(f"-- {name}")
