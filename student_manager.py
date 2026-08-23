#write a functin add_student that takes student_id, name, course and age.
from data import students
def add_student(student_id, name, course, age):
    if student_id in students:
        return False
    students[student_id] = {"name": name,
                              "course": course,
                              "age": age,
                              "marks" : [],
                              "skills": set()
                              }
    return True

def find_student(student_id):
    return students.get(student_id)

#update_course -- take student_id and updates the course
def update_course(student_id, new_course):
    if student_id not in students:
        return False
    students[student_id]["course"] = new_course
    return True

## remove_student
def remove_student(student_id):
    if student_id not in students:
        return False
    del students[student_id]
    return True

##return student value by default, by default gives error if it doesnt exist
## adding none will return none 
def remove_student_pop(student_id):
    students.pop(student_id, None)

