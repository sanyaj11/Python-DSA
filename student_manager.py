from data import students

##add_student
def add_student(student_id, name, course, age):
    if student_id in students:
        return False
    students[student_id] = {"name": name,
                            "age" : age,
                            "course": course,
                            "marks": [],
                            "skills": set()}
    return True

##find student
def find_student(student_id):
    return students.get(student_id, False)

##update student name
def update_name(student_id, new_name):
    if student_id not in students:
        return False
    students[student_id]["name"] = new_name
    return True

##update_course -- take student_id and updates the course
def update_course(student_id, new_course):
    if student_id not in students:
        return False
    students[student_id]["course"] = new_course
    return True

## remove_student
def remove_student(student_id):
    return students.pop(student_id, None)

## display all students
def display_all_students():
    names=[]
    for v in students.values():
        names.append(v["name"])
        # print(v["name"])
    return names

## add marks
def add_marks(student_id, new_mark):
    if student_id not in students:
        return False
    students[student_id]["marks"].append(new_mark)
    return True

## add skill
def add_skill(student_id, new_skill):
    if student_id not in students:
        return False
    students[student_id]["skills"].add(new_skill)
    return True

##write a function that counts frequency of numbers from marks
def freq_marks():
    freq = {}
    for v in students.values():
        for mark in v["marks"]:
            freq[mark] = freq.get(mark, 0) + 1
    return freq

##find how many took courses 
def course_freq():
    freq = {}
    for v in students.values():
        course = v["course"]
        freq[course] = freq.get(course, 0) + 1
    return freq

## find the best course 
def best_course():
    freq = course_freq()          # reuse freq function
    best_count = 0
    best_course = None

    for k, v in freq.items():
        if v > best_count:
            best_count = v
            best_course = k
    return best_course

## character frequency
def char_freq():
    text = 'programming'
    freq = {}
    for char in text:
        freq[char]=freq.get(char, 0) + 1
    return freq

## Unique Marks, and return only one count elements
def unique_marks_list():
    text = [70,80,70,90,80,95,23]
    freq = {}
    for i in text:
        freq[i] = freq.get(i, 0) + 1

    unique_marks = []
    for k, v in freq.items():
        if v == 1:
            unique_marks.append(k)
    return unique_marks

#%% Highest Mark Student Given student_id -> mark, return the ID with highest mark without max(..., key=...).
def highest_mark(student_id):
    if student_id not in students:
        return False
    highest_marks = 0
    best_student = None
    for k, v in students.items():
        for mark in v["marks"]:
            if mark > highest_marks:
                highest_marks = mark
                best_student = k
    return best_student

##Average Marks - Given student_id -> list of marks, build student_id -> average.
def average_mark(student_id):
    if student_id not in students:
        return False
    w = 0
    marks = students[student_id]["marks"]
    if not marks:
        return False
    for i in marks: 
        w = w + i
    average = w/(len(students[student_id]["marks"]))
    return average

 ##Course to Student Names -Transform registry into course -> list of student names. Challenge 11-1
def get_student_from_course(course):
    student_names = []
    for k, v in students.items():
            if course == v["course"]:
                student_names.append(v["name"])
    return student_names

## Global Mark Frequency - Combine marks across all profiles into one mark -> count map. Challenge 11-2
def global_mark_freq():
    freq = {}
    for k, v in students.items():
        for mark in v["marks"]:
            freq[mark] = freq.get(mark, 0)+1
    return freq

## Most Common Mark. Find the most common mark manually using the global frequency map. Challenge 11-3
def common_mark():
    freq = {}
    for v in students.values():
        for mark in v["marks"]:
            freq[mark] = freq.get(mark, 0) + 1
    common = None
    count = 0
    for k, v in freq.items():
        if v > count:
            count = v
            common = k
    return common

##Challenge 4 - Design Question
##With 1,000,000 students and frequent ID lookup, explain why student_id -> profile is better than list-only storage.
#---> O(n) List is not a good choice here because it will iterate through all the items even for one lookup task. 
# O(1) Dict is the correct choice because it uses hash tables, and uses unique location for each lookup, making search quicker, and efficient.

##Challenge 5 - Think Ahead
##If name-based search becomes frequent, does the current ID-keyed dictionary automatically make it O(1)?
##Explain. Do not optimize yet.
#--> Dict gives o(1) only for key lookup not on values. Name based search will be O(n)
#any lookup where you supply the ID is O(1) no matter which field you're pulling out (name, age, course, skills). Any lookup where you're searching by name, age, course, or skill — instead of by ID — is O(n)


# %%
