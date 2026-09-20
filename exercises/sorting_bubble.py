#%% Task 1: Bubble Sort - optimized
def bubble_sort(values):
    n = len(values)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j+1] = values[j+1], values[j]
                swapped = True
        if swapped == False:
            break
    return values
values = [10, 2, 4, 5, 6, 7, 8, 9, 1]
print(bubble_sort(values))

# %% 
def bubble_count(values):
    n = len(values)
    count = 0
    swap = 0
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i -1):
            count = count + 1
            if values[j] > values [j+1]:
                values[j], values[j+1] = values[j+1], values[j]
                swapped = True
                swap = swap + 1
        if swapped == False:
            break
    return values, swap, count
values = [10, 2, 4, 5, 6, 7, 8, 9, 1]
print(bubble_count(values))


#%% Task 6: Sort Descending

def bubble_count(values):
    n = len(values)
    count = 0
    swap = 0
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            count = count + 1
            if values[j] < values[j + 1]:               ## big value move to left
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
                swap = swap + 1
        if swapped == False:
            break
    return values, count, swap

values = [10, 2, 4, 5, 6, 7, 8, 9, 1]
print(bubble_count(values))

#%% Task 7 with bubble sort
def bubble_student(students_list):
      n = len(students_list)
      for i in range(n - 1):
            for j in range(0, n - i - 1):
                 if students_list[j][2] < students_list[j+1][2]:
                      students_list[j], students_list[j+1] = students_list[j+1], students_list[j]
      return(students_list) 

students_list = [
     ("ST101", "asha", 98),
     ("ST102", "Riya", 91),
     ("ST103", "Neha", 91),
     ("ST104", "Pinky", 95),
     ("ST105", "Sara", 73),
]
print(bubble_student(students_list))

# %% Bubble sort dry-run practice (manual trace, not Exercise A's list)
# list = [7, 3, 9, 2, 5]
#         3 , 7, 9, 2 ,5   -- compared 3 and 7 -- swap 1
#         3, 7, 9, 2, 5       -- compared 7 and 9 -- NO SWAP
#         3, 7, 2, 9, 5       -- compared 9 and 2 -- swap 2
#         3, 7, 2, 5, 9       -- compared 9 and 5 -- swap 3
#         3, 2, 7, 5, 9       -- compared 2 and 7 -- swap 4
#         3, 2, 5, 7, 9       -- compared 5 and 7 -- swap 5
#         2, 3, 5, 7, 9       -- compared 2 and 3 -- swap 6

# comparison count = 7
# swap = 6

# [7, 6, 5, 4, 2] -
# 6, 7, 5, 4, 2   - compared 6 and 7 -- swap 1
# 6, 5, 7, 4, 2   - compared 5 and 7 -- swap 2
# 6, 5, 4, 7, 2   - compared 4 and 7 -- swap 3
# 6, 5, 4, 2, 7   - compared 2 and 7 -- swap 4
# 5, 6, 4, 2, 7   - compared 4 and 5 -- swap 5
# 5, 4, 6, 2, 7   - compared 4 and 2  -- swap 6
# 5, 4, 2, 6, 7   - compared 2 and 6 -- swap 7
# worst case - O(n^2)

# NOTE: Exercise A asks for [5,1,4,2,8] after ONE pass specifically - still todo.