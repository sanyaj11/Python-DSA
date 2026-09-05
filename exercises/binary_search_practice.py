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
#sorting - n log n + binary search - o(log n)

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
values = [3,7,11,18,24,31,42,56,70]
target = 15

def insert_index(values, target):
    left = 0
    right = len(values) - 1
    while left < right:
        mid = (left+right)//2
        if values[mid] == target:
            return mid
        elif values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
print(insert_index(values, target))

# %% Exercise E - First and Last occurence
values = [10,20,20,20,30,40]
target = 20
def find_occurence(values, target, first):
    left = 0
    right = len(values) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if values[mid] == target:
            ans = mid
            if first:
                right = mid - 1
            else:
                left = mid + 1
        elif values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans
print(find_occurence(values, 20, first=True))
print(find_occurence(values, 20, first=False))

# %% Excercise F - Count comparisons (binary side)
#  Modify linear and binary search to return both result and comparison count. Compare on large sorted lists

values = [3,7,11,18,24,31,42,56,70]
target = 42

def binary_search(values, target):
    left = 0
    n = len(values)
    right = n-1
    count = 0
    while left <= right:
        mid = (left+right)//2
        count = count + 1
        if values[mid] == target:
            return mid, count
        if values[mid] < target:
            left = mid + 1
        elif values[mid] > target:
            right = mid - 1
    return -1, count
print(binary_search(values, target))

# %%
