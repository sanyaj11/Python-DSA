from data import students

# Copied from exercises/linear_search_practice.py (renamed find_students_by_course -> find_all_by_course)
def find_all_by_course(course):            #O(n)
    result =[]
    for k, v in students.items():
        if v["course"] == course:
            result.append(v["name"])
        # return result                 ## finds only first student because within loop
    return result                       ##finds all students

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
