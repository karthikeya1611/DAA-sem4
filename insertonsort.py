import time
import random

def insertion_sort(arr):
    n = len(arr)
    # Traverse from 1 to n-1
    for i in range(1, n):
        key = arr[i]     # Element to insert
        j = i - 1

        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key at correct position
        arr[j + 1] = key

    return arr


# Generate 50 random numbers (0–999)
nums = [random.randint(0, 9999) for _ in range(5000)]
print("Random 50 Numbers:")
print(nums)

# Measure time
start_time = time.time()

sorted_nums = insertion_sort(nums)

end_time = time.time()
execution_time = end_time - start_time

# Output
print("\nSorted List:")
print(sorted_nums)

print("\nExecution Time:", execution_time, "seconds")
print("Space Complexity: O(1)")   # Insertion sort uses constant extra space
