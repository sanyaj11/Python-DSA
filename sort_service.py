from data import students

#%% Excercise A - One bubble Pass
list1 = [5, 1, 4, 2, 8]
n = len(list1)
swap = 0
count = 0
for i in range(0, 1):
    swapped = False
    count = count + 1
    for j in range(0, n - i - 1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
            swapped = True
            swap = swap + 1
    if swapped == False:
        break
print(list1, swap, count)      

# %% Excercise B - Selection Dry Run
list1 = [29, 10, 14, 37, 13]
n = len(list1)
for i in range(n - 1):
    min_index = i
    for j in range(i+1, n):
        if list1[min_index] > list1[j]:
            min_index = j
    print(min_index)
    if min_index != i:
        list1[i], list1[min_index] = list1[min_index], list1[i]
print(list1)

# %% Exercise C - Insertion Dry Run
list1 = [5, 2, 4, 6, 1, 3]
n = len(list1)
for i in range(1, n):
    keys = list1[i]
    j = i - 1
    while j >= 0 and keys < list1[j]:
        list1[j+1] = list1[j]
        j = j - 1
    list1[j + 1] = keys
    print(list1)
# print(list1)

# %% Exercise D - Sort marks - bubble
list1 = [72, 55, 91, 63, 88, 55]
n = len(list1)
for i in range(n - 1):
    swapped = False
    for j in range(0, n -i - 1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
            swapped = True
    if swapped == False:
        break
print(list1)

#%%  8 Final Assignment  - generate_leaderboard(): all students ordered by score descending.
from data import students
def generate_leaderboard():
    # records = [(k, v["name"], v["score"]) for k, v in students.items()]
    records = []
    for k, v in students.items():
        records.append((k, v["name"], v["score"]))
    n = len(records)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if records[j][2] < records[j+1][2]:
                records[j], records[j+1] = records[j+1], records[j]
                swapped = True
        if swapped == False:
            break
    return records
# print(generate_leaderboard())

#%% leaderboard_by_name(): all students alphabetically by name
from data import students
def leaderboard_by_name(): 
    records = []
    for v in students.values():
        records.append((v["name"], v["score"]))
    n = len(students)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if records[j][0] < records[min_index][0]:
                min_index = j
        if min_index != i:
            records[i], records[min_index] = records[min_index], records[i]
    return records
print(leaderboard_by_name())

# %%top k students
from data import students
def top_k(k):
    records = []
    for key, v in students.items():
        records.append((key, v["score"]))
    n = len(records) #4
    if k > n:
        k = n
        print("K is too high for data")
    for i in range(k):
        max_ind = i
        for j in range(i+1, n):
            if records[max_ind][1] < records[j][1]:
                max_ind = j
        if max_ind != i:
            records[i], records[max_ind] = records[max_ind], records[i]
    return records[:k]  ##slicing[start:stop:step]
k = 1
print(top_k(k))

# %% course_leaderboard(course) - filter by course and score descending
from data import students
def course_leaderboard(course):
    records = []
    for key, v in students.items():
        if v["course"].lower() == course.lower(): 
            records.append((key, v["course"], v["score"]))
    n = len(records)
    for i in range(1, n):
        keys = records[i]
        j = i - 1
        while j >= 0 and keys[2] > records[j][2]:
            records[j+1] = records[j]
            j = j - 1
        records[j+1] = keys    
    return records
print(course_leaderboard(course="python"))

# %% tie breaking(): equal scores ordered by name
from data import students
def tie_breaking():
    records = []
    for key, v in students.items():
        records.append((key, v["score"], v["name"]))
    n = len(records)
    for i in range(n-1):
        swapped = False
        for j in range(0, n - i - 1):
            if records[j][1] < records[j+1][1] or (records[j][1] == records[j+1][1] and records[j][2] > records[j+1][2]) :
                records[j], records[j+1] = records[j+1], records[j]
                swapped = True
        if swapped == False:
            break
    return records
print(tie_breaking())

#%% tie breaking
from data import students
def tie_breaking():
    records = []
    for key, v in students.items():
        records.append((key, v["score"], v["name"]))
    return sorted(records, key=lambda potato:(-potato[1], potato[2]) )
print(tie_breaking())


# %% build score index(): ascending (score, student_id) records
from data import students
def build_score_index():
    records = []
    for key, v in students.items():
        records.append((v["score"], key))
    n = len(records)
    for i in range(n-1):
        min_ind = i
        for j in range(i+1, n):
            if records[min_ind] > records[j]:
                min_ind = j
        if min_ind != i:
            records[i], records[min_ind] = records[min_ind], records[i]
    return records
print(build_score_index())

# %%find score(score): binary search the score index #does handle duplicates
from data import students

def binary_search(records, score):
    left = 0
    right = len(records) - 1
    while left <= right:
        mid = (left+right)//2
        if records[mid][1] == score:
            return records[mid][0], mid
        elif records[mid][1] < score:
            left = mid + 1
        else:
            right = mid - 1
    return None

def find_score(score):
    records = []
    for key, v in students.items():
        records.append((key, v["score"]))
    n = len(records)
    for i in range(1, n):
        keys = records[i]
        j = i - 1
        while j >= 0 and keys < records[j]:
            records[j+1] = records[j]
            j = j - 1
        records[j+1] = keys
    return binary_search(records, score)
score = 91
print(find_score(score))

# %% 9 - Challenge Tasks
#Challenge 1 - Top K
def top_k_challenge(k):
    records = []
    for key, v in students.items():
        records.append((key, v["score"]))
    n = len(records)
    if k > n:
        k = n
    for i in range(k):
        max_ind = i
        for j in range(i + 1, n):
            if records[max_ind][1] < records[j][1]:
                max_ind = j
        if max_ind != i:
            records[i], records[max_ind] = records[max_ind], records[i]
    return records[:k]
print(top_k_challenge(3))


#%% Challenge 2 - Stable leaderboard using bubble sort since its preseves the order
from data import students

def stable_leaderboard():
    records = []
    for key, v in students.items():
        records.append((key, v["name"], v["score"]))
    n = len(records)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if records[j][2] < records[j+1][2]:         #decreasing order
                records[j], records[j+1] = records[j+1], records[j]
                swapped = True
        if swapped == False:
            break
    return records
print(stable_leaderboard())

#%% Challenge 3 - multi level ordering
from data import students
def function_multi_level():
    records = []
    for k, v in students.items():
        records.append((k, v["course"], v["score"]))
    records = sorted(records, key=lambda potato:(potato[1], -potato[2]))
    return records
print(function_multi_level())

#%% Challenge 4 - Performance Experiment
def bubble_count(values):
    values = values.copy()
    n = len(values)
    count = 0
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            count = count + 1
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
                swapped = True
        if swapped == False:
            break
    return count

def selection_count(values):
    values = values.copy()
    n = len(values)
    count = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            count = count + 1
            if values[j] < values[min_index]:
                min_index = j
        if min_index != i:
            values[i], values[min_index] = values[min_index], values[i]
    return count

def insertion_count(values):
    values = values.copy()
    n = len(values)
    count = 0
    for i in range(1, n):
        key = values[i]
        j = i - 1
        while j >= 0:
            count = count + 1
            if values[j] > key:
                values[j+1] = values[j]
                j = j - 1
            else:
                break
        values[j+1] = key
    return count

base_values = [10, 2, 4, 5, 6, 7, 8, 9, 1]
sorted_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_values = [9, 8, 7, 6, 5, 4, 3, 2, 1]
random_values = [6, 1, 9, 4, 10, 2, 7, 5, 8] 

print("Sorted input:", sorted_values)
print("bubble comparisons:", bubble_count(sorted_values))
print("selection comparisons:", selection_count(sorted_values))
print("insertion comparisons:", insertion_count(sorted_values))

print("Reverse input:", reverse_values)
print("bubble comparisons:", bubble_count(reverse_values))
print("selection comparisons:", selection_count(reverse_values))
print("insertion comparisons:", insertion_count(reverse_values))

print("Random input:", random_values)
print("bubble comparisons:", bubble_count(random_values))
print("selection comparisons:", selection_count(random_values))
print("insertion comparisons:", insertion_count(random_values))

#%% Challenge 5 - System Design
#index once and reusing it is better than sorting before every search.
#Sorting is expensive O(n) at best, if we sort before every search for large data then its waste of work
#sorting once and reusing the search is better due to cost and time+space complexity.
