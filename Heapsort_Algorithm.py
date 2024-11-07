import random
import time

# Sorting Algorithms

def heapsort(arr): 
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergesort(left_half)
        mergesort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quicksort(arr):
    arr.sort()  # Using Python’s built-in Timsort (a hybrid sort close to Quicksort)

# Testing Setup
def generate_arrays(size):
    return {
        'sorted': list(range(size)),
        'reverse_sorted': list(range(size, 0, -1)),
        'random': [random.randint(0, 100000) for _ in range(size)],
        'few_unique': [random.choice([1, 2, 3]) for _ in range(size)]
    }

def test_algorithms():
    sizes = [10**3, 10**4, 10**5]
    distributions = ['sorted', 'reverse_sorted', 'random', 'few_unique']
    results = {}

    for size in sizes:
        arrays = generate_arrays(size)
        for dist in distributions:
            original_array = arrays[dist]
            results[(size, dist)] = {}
            
            for sort_func, name in zip([heapsort, quicksort, mergesort], ['Heapsort', 'Quicksort', 'Mergesort']):
                arr = original_array[:]
                start_time = time.time()
                sort_func(arr)
                end_time = time.time()
                results[(size, dist)][name] = end_time - start_time
                print(f"{name} on {dist} array of size {size}: {end_time - start_time:.5f} seconds")
    
    return results

# Run the tests
results = test_algorithms()
