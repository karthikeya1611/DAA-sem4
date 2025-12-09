import time
import random

# ------------------ Insertion Sort ------------------
def insertion_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ------------------ Bubble Sort ------------------
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# ------------------ Selection Sort ------------------
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# ------------------ Heap Sort ------------------
def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    arr = arr.copy()
    n = len(arr)

    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


# ------------------ Bucket Sort ------------------
def bucket_sort(arr):
    arr = arr.copy()
    if len(arr) == 0:
        return arr

    num_buckets = 10
    max_value = max(arr)
    buckets = [[] for _ in range(num_buckets)]

    for value in arr:
        index = int((value / max_value) * (num_buckets - 1))
        buckets[index].append(value)

    for i in range(num_buckets):
        buckets[i].sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr



# ------------------ Generate random numbers ------------------

original_list = [random.randint(0, 9999) for _ in range(500)]

# Make separate copies for each sorting algorithm
list_insertion  = original_list.copy()
list_bubble     = original_list.copy()
list_selection  = original_list.copy()
list_heap       = original_list.copy()
list_bucket     = original_list.copy()

print("Random 500 Numbers Generated!\n")



# ------------------ Sort and store results ------------------

results = {}

# Insertion Sort
start = time.time()
sorted_insertion = insertion_sort(list_insertion)
results["Insertion Sort"] = time.time() - start

# Bubble Sort
start = time.time()
sorted_bubble = bubble_sort(list_bubble)
results["Bubble Sort"] = time.time() - start

# Selection Sort
start = time.time()
sorted_selection = selection_sort(list_selection)
results["Selection Sort"] = time.time() - start

# Heap Sort
start = time.time()
sorted_heap = heap_sort(list_heap)
results["Heap Sort"] = time.time() - start

# Bucket Sort
start = time.time()
sorted_bucket = bucket_sort(list_bucket)
results["Bucket Sort"] = time.time() - start



# ------------------ Print sorted lists ------------------

print("--------------- SORTED LISTS FOR EACH ALGORITHM ---------------\n")

print("Insertion Sort Output:\n", sorted_insertion, "\n")
print("Bubble Sort Output:\n", sorted_bubble, "\n")
print("Selection Sort Output:\n", sorted_selection, "\n")
print("Heap Sort Output:\n", sorted_heap, "\n")
print("Bucket Sort Output:\n", sorted_bucket, "\n")



# ------------------ Print performance ------------------

print("------------------ PERFORMANCE COMPARISON ------------------")
for name, exec_time in results.items():
    print(f"{name}: {exec_time:.8f} seconds")

print("\n------------------ SPACE COMPLEXITIES ------------------")
print("Insertion Sort: O(1)")
print("Bubble Sort: O(1)")
print("Selection Sort: O(1)")
print("Heap Sort: O(1)")
print("Bucket Sort: O(n + k)")
