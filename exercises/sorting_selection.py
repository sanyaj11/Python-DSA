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
