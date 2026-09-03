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

# %% Binary Search - Task 4 + 5 Binary Search Dry run
values = [3,7,11,18,24,31,42,56,70]
target = 42

def binary_search(values, target):              #best case: mid == target O(1)
    left = 0                                   #worst case: divide, conquer O(log n)
    n = len(values)
    right = n-1
    while left <= right:
        mid = (left+right)//2
        if values[mid] == target:
            return mid          #index returned
        if values[mid] < target:
            left = mid + 1
        elif values[mid] > target:
            right = mid - 1
    return -1
print(binary_search(values, target))


# %% For values [2,5,8,12,16,23,38,56,72,91], search 23.
#               left    right   mid     values[mid]
#                0      9       4       16
#                5      9       7       56
#                5      6       5       23

#search 40
#               left    right   mid     values[mid]
#                0      9       4       16
#                5      9       7       56
#                5      6       5       23
#                6      6       6       38
#                7      6       -       STOP  

# %% Binary Search - Task 7 Search for an Exact Score
score_index = [
                (73, "ST104"),
                (78, "ST101"),
                (84, "ST103"),
                (91, "ST102")
            ]

def find_score(score_index,target_score):               #Best: O(1) if the first mid is the score.
    left = 0                                            #Worst: O(log n) if the score is at an end or missing.
    right = len(score_index) - 1                        #Extra space: O(1) - left, right, mid
    while left <= right:
        mid = (left + right)//2
        if score_index[mid][0] == target_score:
            return score_index[mid]
        elif score_index[mid][0] < target_score:
            left = mid + 1
        else:
            right = mid - 1
    return None
print(find_score(score_index,78))

#• What cost would be involved if you had to sort from scratch every single time? o(n log n)
sorting - n log n + binary search - o(log n)

# %% Binary Search - Task 8 First Occurrence with Duplicates
scores = [60, 70, 70, 70, 80, 90]
target = 70

def first_occurrence(scores, target):               #Best: O(1) if the first mid is the score.
    left = 0                                        #Worst: O(log n) if the score is at an end or missing.
    right = len(scores) - 1                         #Extra space: O(1) - left, right, mid
    w = -1
    while left <= right:
        mid = (left + right)//2
        if scores[mid] == target:
            w = mid
            right = mid - 1
        elif scores[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return w
print(first_occurrence(scores, target))

# %%  search 
values = [3,7,11,18,24,31,42,56,70]
target = 15

def binary_search(values, target):              #best case: mid == target O(1)
    left = 0                                   #worst case: divide, conquer O(log n)
    n = len(values)
    right = n-1
    while left <= right:
        mid = (left+right)//2
        if values[mid] == target:
            return mid          #index returned
        if values[mid] < target:
            left = mid + 1
        elif values[mid] > target:
            right = mid - 1
    return left
print(binary_search(values, target))


# recursive way
def binary_search(values, target):              #best case: mid == target O(1)
    left = 0                                   #worst case: divide, conquer O(log n)
    n = len(values)
    right = n-1
    return binary_recu(values, left, right, target)

def binary_recu(values, left, right, target):
    if left > right:
        return left
    mid = (left+right)//2
    if values[mid] == target:
        return mid          #index returned
    if values[mid] < target:
        return binary_recu(values,mid + 1, right, target)
    elif values[mid] > target: 
        return binary_recu(values,left, mid - 1, target)
print(binary_search(values, target))


# %% Chapter - 6 (Page 14)

#%% Exercise A - Find first Falling Score
def failing_score(scores, fail_score):
    for i in range(len(scores)):
        if scores[i] <= fail_score:
            return scores[i]
print(failing_score([23, 34, 55, 58, 65], 35))

# %% Exercise B - Find all Python students
def find_students_by_course(course):            #O(n)
    result =[]
    for k, v in students.items():
        if v["course"] == course:
            result.append(v["name"])
        # return result                 ## finds only first student because within loop         
    return result                       ##finds all students
print(find_students_by_course("Python"))

#%% Exercise C - Exact Sorted score
def binary_search(scores, target):
    left = 0
    right = len(scores) - 1
    while left <= right:
        mid = (left+right)//2
        if scores[mid] == target:
            return mid
        if scores[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(binary_search([34, 54, 56, 88, 90, 95], 90))

# %% Exercise D - Search Insert Position

