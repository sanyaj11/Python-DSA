from data import students

# Search by name
def find_by_name(name):                     #best case O(1) -- first person
    for k, v in students.items():           #worst case O(n) -- Last person or doesnt exist
        if v["name"] == name:
            return k, v
    return "Doesnt exist"
print(find_by_name("Sanya"))

#%%Linear Search - Task 1
nums = [12, 25, 31, 44, 57]
target = 31
def linear_search(nums, target):           #best case O(1) -- first index
    for i in range(len(nums)):             #worst case O(n) -- Last index or doesnt exist
        if nums[i] == target:              #extra space O?? -- O(1) since we only created i
            return(i)
    return -1
print(linear_search(nums, target))

# %% Linear Search - Task 2  Return All Students in a Course
def find_students_by_course(course):            #O(n)
    result =[]
    for k, v in students.items():
        if v["course"] == course:
            result.append(v["name"])
        # return result                 ## finds only first student because within loop
    return result                       ##finds all students
print(find_students_by_course("Python"))

# %% Linear Search - Task 3 Case-Insensitive Name Search
def find_by_name_case_insensitive(name):
    name = name.lower()
    for v in students.values():
        if name == v["name"].lower():
            return v
    return False
print(find_by_name_case_insensitive("ASHA"))

# %% Chapter - 6 (Page 14)

#%% Exercise A - Find first Falling Score
def failing_score(scores, fail_score):
    for i in range(len(scores)):
        if scores[i] < fail_score:
            return scores[i]
    return -1
print(failing_score([23, 34, 55, 58, 65], 40))

# %% Exercise B - Find all Python students
def find_students_by_course(course):            #O(n)
    result =[]
    for k, v in students.items():
        if v["course"] == course:
            result.append(v["name"])
        # return result                 ## finds only first student because within loop
    return result                       ##finds all students
print(find_students_by_course("Python"))

# %% Excercise F - Count comparisons (linear side)
#  Modify linear and binary search to return both result and comparison count. Compare on large sorted lists

values = [3,7,11,18,24,31,42,56,70]
target = 42

def linear_search(values, target):
    count = 0
    for i in range(len(values)):
        count = count + 1
        if values[i] == target:
            return(i), count
    return -1, count
print(linear_search(values, target))

# %%
