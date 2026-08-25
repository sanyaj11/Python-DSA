from student_manager import add_student, find_student, update_name, update_course, remove_student, display_all_students, add_marks, course_freq, best_course, average_mark, add_skill

def print_menu():
    print("""
    CODECLASS STUDENT REGISTRY
    1. Add student
    2. Find student
    3. Update student name
    4. Update student course
    5. Delete student
    6. Display all students
    7. Add mark
    8. Add skill
    9. Show course frequencies
    10. Show most popular course
    11. Show student average mark
    12. Exit
""")

user_input = input("Select an Option: ")
if user_input == "1":
    student_id = input("Enter student id: ")
    name = input("Enter student name: ")
    course = input("Enter course: ")
    age = int(input("Enter age: "))
    call_function = add_student(student_id, name, course, age)
    print(call_function)

elif user_input == "2":
    student_id = input("Enter student id: ")
    call_function = find_student(student_id)
    print(call_function)

elif user_input == "3":
    student_id = input("Enter student id: ")
    new_name = input("Enter student new name: ")
    call_function = update_name(student_id, new_name)
    print(call_function)

elif user_input == "4":
    student_id = input("Enter student id: ")
    new_course = input("Enter the new course: ")
    call_function = update_course(student_id, new_course)
    print(call_function)

elif user_input == "5":
    student_id = input("Enter student id: ")
    call_function = remove_student(student_id)
    print(call_function)

elif user_input == "6":
    call_function = display_all_students()
    print(call_function)

elif user_input == "7":
    student_id = input("Enter student id: ")
    new_mark = int(input("Enter the new mark: "))
    call_function = add_marks(student_id, new_mark)
    print(call_function)

elif user_input == "8":
    student_id = input("Enter student id: ")
    new_skill = input("Enter the new skill: ")
    call_function = add_skill(student_id, new_skill)
    print(call_function)

elif user_input == "9":
    call_function = course_freq()
    print(call_function)

elif user_input == "10":
    call_function = best_course()
    print(call_function)

elif user_input == "11":
    student_id = input("Enter student id: ")
    call_function = average_mark(student_id)
    print(call_function)

elif user_input == "12":
    print("Exiting.")

else:
    print("Invalid option, try again.")











