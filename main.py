

# %%
from data import students
# print(data.students["ST101"]["name"])
# print(data.students["ST101"]["marks"][2])
# print("python" in data.students["ST101"]["skills"])
# %%
from student_manager import add_student
print(add_student("ST102", "Riya", "Math", 27))
print(add_student("ST103", "Neha", "English", 20))
# %%
import student_manager 
# print(student_manager.find_student("ST102"))
# print(student_manager.update_course("ST101", "HTML"))
# print(student_manager.remove_student("ST102"))
# print(student_manager.remove_student("ST101"))

# for key in students.keys():
#     print(students[key])
print(students.keys())
print(students.values())
print(students.items())

for key, value in students.items():
    print(key + " | " + value['name'] + " | " + value['course'])
# %%
