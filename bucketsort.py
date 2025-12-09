import time
import random

def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    # Step 1: Create empty buckets
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]

    # Step 2: Insert elements into buckets
    max_value = max(arr)
    for value in arr:
        index = int((value / max_value) * (num_buckets - 1))
        buckets[index].append(value)

    # Step 3: Sort each bucket
    for i in range(num_buckets):
        buckets[i].sort()

    # Step 4: Merge buckets into a single list
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


# Generate 50 random numbers (0–999)
nums = [random.randint(0, 9999) for _ in range(5000)]
print("Random 50 Numbers:")
print(nums)

# Measure time
start_time = time.time()

sorted_nums = bucket_sort(nums)

end_time = time.time()
execution_time = end_time - start_time

# Output
print("\nSorted List:")
print(sorted_nums)

print("\nExecution Time:", execution_time, "seconds")
print("Space Complexity: O(n + k)")  # n = number of elements, k = number of buckets
