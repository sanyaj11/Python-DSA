
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
# %% 
