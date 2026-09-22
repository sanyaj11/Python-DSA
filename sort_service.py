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


