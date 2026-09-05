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

#challenge 2 - page 16 module 2
#Given sorted (score, student_id) pairs, return the first student whose score >= target.
#Binary Search: best O(1), worst O(log n), extra space O(1).
def first_at_or_above_score(target_score):
    score_index = build_score_index()
# score_index = [(42, 'ST101'), (59, 'ST103'), (79, 'ST102')]
    left = 0
    right = len(score_index) - 1
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        if score_index[mid][0] >= target_score:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    if answer == -1:
        return None
    return score_index[answer]

#challenge 3 - page 16 module 2
#Users type a prefix like 'Ash' and want every name starting with it.
#Linear Search best O(1), worst O(n), extra space O(n) for the result list.
def find_by_name_prefix(prefix):
    prefix = prefix.lower()
    result = []
    for v in students.values():
        if v["name"].lower().startswith(prefix) == True:
            result.append(v["name"])
    return result

#challenge 4 - page 16 module 2 - Design Decision
#Exact ID lookup            -> Dictionary lookup. Keys are the IDs, average O(1).
#Arbitrary unsorted name    -> Linear Search. Names aren't keys so scan everything O(n).
#Exact score in a maintained sorted score index -> Binary Search. Sorted data + only need one exact match, O(log n).
#All students in a course   -> Linear Search. Course isn't a key, and we need every match, so a full O(n) scan.
#Membership in a Set of skills -> Set membership. "in" on a Set is average O(1), no comparisons needed.

