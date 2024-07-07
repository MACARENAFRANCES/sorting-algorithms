"""
Created on Sat March 16
Data structures and algorithms Project 2

Sort methods
@author: macarenafrances
"""
'''Insertion Sort'''
def insertion_sort_with_counter(arr):
    count = 0  # Initialize the operation counter
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            count += 1  # Count the swap operation
        count += 1  # Count the comparison operation
        arr[j + 1] = key
    return arr, count

# For list 1
L_1 = [34, 32, 3, 16, 12, 11, 97, 59, 63, 4] 
sorted_L1, count_L1 = insertion_sort_with_counter(L_1)
print("List sorted by insertion sort:", sorted_L1)
print("Number of operations performed:", count_L1)
#Operations: 31

# For list 2
L_2 = [55, 47, 27, 96, 14, 28, 62, 75, 99, 44, 59, 100, 29, 52, 63, 85, 84, 54, 46, 49, 3, 18, 9, 77, 51, 4, 94, 86, 73, 66, 24, 67, 25, 95, 78, 21, 12, 37, 60, 31, 6, 32, 90, 81, 5, 87, 64, 19, 1, 57]
sorted_L2, count_L2 = insertion_sort_with_counter(L_2)
print("List sorted by insertion sort:", sorted_L2)
print("Number of operations performed:", count_L2)
#Operations: 717

# For list 3
L_3 = [52, 26, 51, 68, 47, 39, 19, 3, 40, 73, 87, 9, 36, 57, 77, 6, 32, 71, 91, 10, 55, 65, 22, 56, 81, 90, 82, 25, 37, 48, 66, 67, 79, 83, 62, 31, 45, 33, 89, 80, 69, 76, 29, 15, 11, 28, 44, 17, 16, 12, 23, 75, 95, 41, 96, 24, 99, 50, 98, 46, 72, 78, 54, 13, 35, 14, 63, 86, 8, 59, 38, 61, 92, 18, 27, 64, 88, 42, 4, 34, 74, 97, 30, 7, 70, 58, 94, 2, 21, 5, 85, 100, 20, 93, 53, 84, 60, 49, 1, 43]
sorted_L3, count_L3 = insertion_sort_with_counter(L_3)
print("List sorted by insertion sort:", sorted_L3)
print("Number of operations performed:", count_L3)
#Operations: 2540



'''Quicksort'''
def quicksort_with_counter(arr): 
    count = 0  # Initialize the operation counter

    def partition(l, r): 
        nonlocal count  
        pivot = arr[r] 
        pointer = l 
        for i in range(l, r): 
            if arr[i] <= pivot: 
                arr[i], arr[pointer] = arr[pointer], arr[i] 
                pointer += 1 
                count += 1  
            count += 1  
        arr[pointer], arr[r] = arr[r], arr[pointer]
        count += 1  
        return pointer

    def quicksort(l, r): 
        if l < r:
            pi = partition(l, r)
            quicksort(l, pi - 1) 
            quicksort(pi + 1, r)

    quicksort(0, len(arr) - 1)
    return arr, count

# For list 1
L_1 = [34, 32, 3, 16, 12, 11, 97, 59, 63, 4]
sorted_L1, count_L1 = quicksort_with_counter(L_1)
print("List 1 sorted by Quicksort:", sorted_L1)
print("Number of operations performed:", count_L1)
#Operations: 40

# For list 2
L_2 = [55, 47, 27, 96, 14, 28, 62, 75, 99, 44, 59, 100, 29, 52, 63, 85, 84, 54, 46, 49, 3, 18, 9, 77, 51, 4, 94, 86, 73, 66, 24, 67, 25, 95, 78, 21, 12, 37, 60, 31, 6, 32, 90, 81, 5, 87, 64, 19, 1, 57]
sorted_L2, count_L2 = quicksort_with_counter(L_2)
print("List 2 sorted by Quicksort:", sorted_L2)
print("Number of operations performed:", count_L2)
#Operations: 456

# For list 3
L_3 = [52, 26, 51, 68, 47, 39, 19, 3, 40, 73, 87, 9, 36, 57, 77, 6, 32, 71, 91, 10, 55, 65, 22, 56, 81, 90, 82, 25, 37, 48, 66, 67, 79, 83, 62, 31, 45, 33, 89, 80, 69, 76, 29, 15, 11, 28, 44, 17, 16, 12, 23, 75, 95, 41, 96, 24, 99, 50, 98, 46, 72, 78, 54, 13, 35, 14, 63, 86, 8, 59, 38, 61, 92, 18, 27, 64, 88, 42, 4, 34, 74, 97, 30, 7, 70, 58, 94, 2, 21, 5, 85, 100, 20, 93, 53, 84, 60, 49, 1, 43]
sorted_L3, count_L3 = quicksort_with_counter(L_3)
print("List 3 sorted by Quicksort:", sorted_L3)
print("Number of operations performed:", count_L3)
#Operations: 921
