#%% Task 5 - Insertion Sorting
def insertion_sort(values):
    n = len(values)
    for i in range(1, n):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j = j -1
        values[j+1] = key
    return values

#%% Task 6: Sort Descending
def insertion_sort_desc(values):
    n = len(values)
    for i in range(1, n):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] < key:     #j < key -- move smaller elements right
            values[j + 1] = values[j]
            j = j - 1
        values[j + 1] = key
    return values

values = [10, 2, 4, 5, 6, 7, 8, 9, 1]
print(insertion_sort_desc(values))

#%% Task 7 with insertion sort
def insertion_student(students_list):
      n = len(students_list)
      for i in range(1, n):
            keys = students_list[i]
            j = i - 1
            while j >=0 and keys[2] > students_list[j][2]:
                 students_list[j+1] = students_list[j]
                 j = j - 1
            students_list[j+1] = keys            
      return(students_list) 

students_list = [
     ("ST101", "asha", 98),
     ("ST102", "Riya", 91),
     ("ST103", "Neha", 91),
     ("ST104", "Pinky", 95),
     ("ST105", "Sara", 73),
]
print(insertion_student(students_list))

# %% Exercise F - Tie Break (done): built-in sorted(), score desc then name asc
students_list = [
     ("ST101", "asha", 98),
     ("ST102", "Riya", 91),
     ("ST103", "Neha", 91),
     ("ST104", "Pinky", 95),
     ("ST105", "Sara", 73),
]
leaderboard_tiebreak = sorted(students_list, key=lambda s: (-s[2], s[1]))
print(leaderboard_tiebreak)

# %% Exercise F - Tie Break (done): manual insertion sort, score desc then name asc

students_list = [
     ("ST101", "asha", 98),
     ("ST102", "Riya", 91),
     ("ST103", "Ariya", 91),
     ("ST104", "Pinky", 95),
     ("ST105", "Sara", 73),
]
def insertion_sorting_tie(students_list):
      n = len(students_list)
      for i in range(1, n):
           keys = students_list[i]
           j = i - 1
           while j >= 0 and (keys[2] > students_list[j][2] or (students_list[j][2] == keys[2] and students_list[j][1] > keys[1])):
                students_list[j+1] = students_list[j]
                j = j - 1
           students_list[j+1] = keys
      return students_list
print(insertion_sorting_tie(students_list))

# %% Exercise H - Sort Then Search (done): insertion sort scores + binary search
students_list = [
     ("ST101", "asha", 98),
     ("ST102", "Riya", 91),
     ("ST103", "Ariya", 91),
     ("ST104", "Pinky", 95),
     ("ST105", "Sara", 73),
     ("ST106", "Vishal", 39),
]
def get_pairs(students_list):
     list1 = []
     for student_id, name, score in students_list:
          list1.append((score, student_id))
     return list1

def insertion_sort_pairs(list1):
     n = len(list1)
     for i in range(1, n):
          keys = list1[i]
          j = i - 1
          while j >= 0 and keys[0] < list1[j][0]:
               list1[j+1] = list1[j]
               j = j - 1
          list1[j+1] = keys
     return list1

def binary_search(list1, target_score):
     left = 0
     right = len(list1) - 1
     while left <= right:
          mid = (left + right) // 2
          if list1[mid][0] == target_score:
               return list1[mid][1]
          elif list1[mid][0] > target_score:
               right = mid - 1
          else:
               left = mid + 1
     return None

score_index = insertion_sort_pairs(get_pairs(students_list))
print(binary_search(score_index, 73))
print(binary_search(score_index, 91))