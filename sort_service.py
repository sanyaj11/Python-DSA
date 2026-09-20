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


