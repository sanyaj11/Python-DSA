#%% Task 3 - Selection sort
def selection_sort(values):
    n = len(values)
    for i in range(n - 1):
        min = i
        for j in range(i+1, n):
            if values[j] < values[min]:
                min = j
        if min != i:
            values[i], values[min] = values[min], values[i]
    return values

values = [10, 2, 4, 5, 6, 7, 8, 9, 1]

#%%
def count_selection(values):
    n = len(values)
    count = 0
    swap = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            count = count + 1
            if values[j] < values[min_index]:
                min_index = j
        if i != j:
            values[i], values[min_index] = values[min_index], values[i]
            swap = swap + 1
    return values, swap, count
values = [10, 2, 4, 5, 6, 7, 8, 9, 1]
print(count_selection(values))

# %% Task 6: Sort Descending
def count_selection_desc(values):
    n = len(values)
    count = 0
    swap = 0
    for i in range(n - 1):
        max_idx = i                         #max find big value
        for j in range(i + 1, n):
            count = count + 1
            if values[j] > values[max_idx]:  #greater
                max_idx = j
        if i != max_idx:
            values[i], values[max_idx] = values[max_idx], values[i]
            swap = swap + 1
    return values

values = [10, 2, 4, 5, 6, 7, 8, 9, 1]
print(count_selection_desc(values))

# %% #%% Task 7 with insertion sort
def selection_student(students_list):
      n = len(students_list)
      for i in range(n - 1):
            max_var = i
            for j in range(i+1, n):
                  if students_list[max_var][2] < students_list[j][2]:
                        max_var = j
            if max_var != i:
                  students_list[i], students_list[max_var] = students_list[max_var], students_list[i]
      return(students_list) 

students_list = [
     ("ST101", "asha", 98),
     ("ST102", "Riya", 91),
     ("ST103", "Neha", 91),
     ("ST104", "Pinky", 95),
     ("ST105", "Sara", 73),
]
print(selection_student(students_list))

# %% Exercise E - Leaderboard (done): sort by score descending, move whole tuple
def leaderboard(students_list):
      n = len(students_list)
      for i in range(n):
          max_index = i
          for j in range(i + 1, n):
               if students_list[j][2] > students_list[max_index][2]:
                  max_index = j
          if max_index != i:
               key = students_list.pop(max_index)
               students_list.insert(i, key)
      return students_list

students_list = [
     ("ST101", "asha", 98),
     ("ST102", "Riya", 91),
     ("ST103", "Neha", 91),
     ("ST104", "Pinky", 95),
     ("ST105", "Sara", 73),
]
print(leaderboard(students_list))

# %% Exercise E - Leaderboard (done): built-in sorted() equivalent
students_list = [
     ("ST101", "asha", 98),
     ("ST102", "Riya", 91),
     ("ST103", "Neha", 91),
     ("ST104", "Pinky", 95),
     ("ST105", "Sara", 73),
]
leaderboard_builtin = sorted(students_list, key=lambda s: s[2], reverse=True)
print(leaderboard_builtin)
