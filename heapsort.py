import time
import random

# Function to heapify a subtree rooted at index i
def heapify(arr, n, i):
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root (max value) to the end
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify the reduced heap
        heapify(arr, i, 0)

    return arr


# Generate 50 random numbers (0–999)
nums = [random.randint(0, 9999) for _ in range(5000)]
print("Random 50 Numbers:")
print(nums)

# Measure execution time
start_time = time.time()

sorted_nums = heap_sort(nums)

end_time = time.time()
execution_time = end_time - start_time

# Output results
print("\nSorted List:")
print(sorted_nums)

print("\nExecution Time:", execution_time, "seconds")
print("Space Complexity: O(1)  # Heap sort is in-place")
