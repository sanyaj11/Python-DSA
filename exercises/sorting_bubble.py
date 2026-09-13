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
    return values, count, swap
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
