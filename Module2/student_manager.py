from data import students

# Search by name
def find_by_name(name):                     #best case O(1) -- first person
    for k, v in students.items():           # worst case O(n) -- Last person or doesnt exist
        if v["name"] == name:
            return k, v
    return "Doesnt exist"
print(find_by_name("Sanya"))

#%%Linear Search - Task 1
nums = [12, 25, 31, 44, 57]
target = 31
def linear_search(nums, target):           #best case O(1) -- first index
    for i in range(len(nums)):             # worst case O(n) -- Last index or doesnt exist
        if nums[i] == target:              # extra space O??
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
    left = 0                                    #worst case: divide, conquer O(log n)
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

