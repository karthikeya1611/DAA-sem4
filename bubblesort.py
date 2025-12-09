#Bubble sort is a simple comparison-based sorting algorithm. It repeatedly steps through a list, compares adjacent items, and swaps them if they are in the wrong order. This process continues until no more swaps are needed, meaning the list is sorted.

#Bubble sort is a simple comparison-based sorting algorithm. It repeatedly steps through a list, compares adjacent items, and swaps them if they are in the wrong order. This process continues until no more swaps are needed, meaning the list is sorted.

#How it works (conceptually)

#Start at the beginning of the list.

#Compare the current element with the next one.

#If the current element is greater, swap them.

#Move to the next pair and repeat.

#After each full pass, the largest unsorted element “bubbles up” to its correct position at the end.

#Repeat passes until the list is sorted.

#Example

#Given the list: [5, 2, 4, 1]

#Pass 1: (5,2) → swap → (5,4) → swap → (5,1) → swap → [2, 4, 1, 5]

#Pass 2: (2,4) OK → (4,1) swap → [2, 1, 4, 5]

#Pass 3: (2,1) swap → [1, 2, 4, 5]

#Sorted!




import time
import random   # for random number generation

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Generate 50 random numbers
nums = [random.randint(0, 9999) for _ in range(5000)]
print("Random 50 numbers:")
print(nums)

# Measure time
start_time = time.time()

sorted_nums = bubble_sort(nums)

end_time = time.time()
execution_time = end_time - start_time

# Output
print("\nSorted list:")
print(sorted_nums)
print("\nExecution Time:", execution_time, "seconds")
print("Space Complexity: O(1)")
