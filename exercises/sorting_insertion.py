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