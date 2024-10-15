import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low <= high:
        
        pivot_index = partition(arr, low, high)

        
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return quickselect(arr, low, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, high, k)

def ith_order_statistic(arr, i):
    
    return quickselect(arr, 0, len(arr) - 1, i - 1)


arr = [12, 3, 5, 7, 19, 26, 1]
i = 4  
result = ith_order_statistic(arr, i)
print(f"The {i}th smallest element is {result}")
