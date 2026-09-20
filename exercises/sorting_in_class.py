
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

#%%bubble sort 
def bubble_sort(list1):
    for i in range(len(list1) -1):         ## (0,4) --- i = 0, 1, 2, 3
          swap = False
          for j in range(0, len(list1) - i - 1): ## (0, 4 - i - 1)
                if list1[j] > list1[j+1]:
                      list1[j], list1[j+1] = list1[j+1], list1[j]
                      swap = True
          if swap == False:
            break
    return list1

list1 = [7, 6, 5, 5, 4, 2]
print(bubble_sort(list1))
          ## worst case - O(n^2)   
          # best case - o(1) -- already sorted 
          # 
                 
# %% Task 7 Move entire tuple but sort based on score selection #TODO
def leaderboard(student_list):
      n = len(students_list)
      for i in range(n): 
          max_index = i
          for j in range(i + 1, n):
               if students_list[j][2] > students_list[max_index][2]:
                  max_index = j
          if max_index != i:
               key = students_list.pop(max_index)
               student_list.insert(i, key)   
            #    students_list[i], students_list[max_index] = students_list[max_index], students_list[j]
      return students_list

students_list = [
     ("ST101", "asha", 98),
     ("ST102", "Riya", 91),
     ("ST103", "Neha", 91),
     ("ST104", "Pinky", 95),
#      ("ST105", "Sara", 73),
]
print(leaderboard(students_list))

#%% Task 8 - Production Sort
students_list = [
     ("ST101", "asha", 98),
     ("ST102", "Riya", 91),
     ("ST103", "Neha", 91),
     ("ST104", "Pinky", 95),
     ("ST105", "Sara", 73),
]
leaderboard = sorted(students_list, key = lambda potato:potato[2], reverse = True)
print(leaderboard)


# %% Task 9 Sorting with Production
students_list = [
     ("ST101", "asha", 98),
     ("ST102", "Riya", 91),
     ("ST103", "Neha", 91),
     ("ST104", "Pinky", 95),
     ("ST105", "Sara", 73),
]
leaderboard = sorted(students_list, key=lambda potato: (-potato[2], potato[1]))

print(leaderboard)

# %% Task 9 with insertion sorting
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
           while j >=0 and keys[2] > students_list[j][2] or (students_list[j][2] == keys[2] and students_list[j][1] > keys[1]) :
                students_list[j+1] = students_list[j]  
                j = j -1
           students_list[j+1] = keys
      return students_list
print(insertion_sorting_tie(students_list))

# %% Task 10 Sorting + Binary Search
students_list = [
     ("ST101", "asha", 98),
     ("ST102", "Riya", 91),
     ("ST103", "Ariya", 91),
     ("ST104", "Pinky", 95),
     ("ST105", "Sara", 73),
     ("ST106", "Vishal", 39)
]
def get_pairs(students_list):
     list1 = []
     for student_id, name, score in students_list:
          list1.append((score, student_id))
     return list1

def insertion_sort(list1):
     n = len(list1)
     for i in range(1, n):
          keys = list1[i]
          j = i - 1
          while j >= 0 and keys[0] < list1[j][0]:
               list1[j+1] = list1[j]
               j = j - 1
          list1[j+1] = keys
     return list1
print(insertion_sort(get_pairs(students_list)))

def binary_search(list1, target_score):
     left = 0
     right = len(list1) - 1
     while left <= right:
          mid = (left+right) // 2
          if list1[mid][0] == target_score:
               return list1[mid][1]
          elif list1[mid][0] > target_score:
               right = mid - 1
          else:
               left = mid + 1
     return None
score_index = insertion_sort(get_pairs(students_list))
print(binary_search(score_index,73)) #var to print
print(binary_search(insertion_sort(get_pairs(students_list)), 91)) #one liner print
# %%
