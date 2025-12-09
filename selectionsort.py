import time
import random

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i  # Assume the current position has the smallest element

        # Find the index of the minimum element in the remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Generate 50 random numbers (0–999)
nums = [random.randint(0, 9999) for _ in range(5000)]
print("Random 50 Numbers:")
print(nums)

# Measure time
start_time = time.time()

sorted_nums = selection_sort(nums)

end_time = time.time()
execution_time = end_time - start_time

# Output
print("\nSorted List:")
print(sorted_nums)

print("\nExecution Time:", execution_time, "seconds")
print("Space Complexity: O(1)")   # Selection sort uses constant extra space
