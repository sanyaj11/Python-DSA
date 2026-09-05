from data import students

# find by id 
def find_by_id(student_id):
    return students.get(student_id, None)

# Search by name - Copied from exercises/linear_search_practice.py
def find_by_name(name):                     #best case O(1) -- first person
    for k, v in students.items():           #worst case O(n) -- Last person or doesnt exist
        if v["name"] == name:
            return k, v
    return "Doesnt exist"
# print(find_by_name("Sanya"))

# Copied from exercises/linear_search_practice.py (renamed find_students_by_course -> find_all_by_course)
def find_all_by_course(course):            #O(n)
    result =[]
    for k, v in students.items():
        if v["course"] == course:
            result.append(v["name"])
        # return result                 ## finds only first student because within loop
    return result                       ##finds all students

# find students above score 
def find_students_above_score(score):
    result = []
    for k, v in students.items():
        if v["score"] > score:
                result.append(v["name"])
    return result

# build score index
def build_score_index():
    new_list = []
    for k,v in students.items():
        new_list.append((v["score"], k))
    return sorted(new_list)

# Copied from exercises/binary_search_practice.py (renamed find_score -> find_exact_score)
def find_exact_score(score_index,target_score):               #Best: O(1) if the first mid is the score.
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

# Copied from exercises/binary_search_practice.py (renamed first_occurrence -> first_score_occurrence)
def first_score_occurrence(scores, target):               #Best: O(1) if the first mid is the score.
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

#%%comparison demo
def comparison_demo(target):
    sorted_score = []
    for v in students.values():
        sorted_score.append(v["score"])
    sorted_score = sorted(sorted_score)

    linear_count = 0
    for i in range(len(sorted_score)):
        linear_count = linear_count + 1
        if sorted_score[i] == target:
            break

    binary_count = 0
    left = 0
    right = len(sorted_score) - 1
    while left <= right:
        mid = (left + right) // 2
        binary_count = binary_count + 1
        if sorted_score[mid] == target:
            break
        elif sorted_score[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"Linear Search checks: {linear_count}")
    print(f"Binary Search checks: {binary_count}")
    return linear_count, binary_count