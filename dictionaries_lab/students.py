searched_course = None
courses = {}
while True:
    command_input = input()

    if ":" not in command_input:
        searched_course = command_input
        break
    command_args = command_input.split(":")
    name = command_args[0]
    id = command_args[1]
    course = command_args[2]
    if course not in courses:
        courses[course] = {}

    courses[course][id] = name

searched_course = searched_course.replace("_", " ")
current_course = courses[searched_course]
for k, v in current_course.items():
    print(f"{v} - {k}")
