import random
import time
import numpy as np
from scipy.stats import describe  # For statistical summaries of results

# Define sorting algorithms: Heapsort, Quicksort, Mergesort
def heapsort(arr): 
    # Heapsort implementation as defined earlier
    ...

def quicksort(arr):
    # Python’s built-in Timsort, close to Quicksort in behavior
    arr.sort()

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Testing function for various inputs
def test_sorting_algorithms():
    sizes = [10**3, 10**4, 10**5]
    distributions = {
        'sorted': lambda n: list(range(n)),
        'reverse_sorted': lambda n: list(range(n, 0, -1)),
        'random': lambda n: [random.randint(0, 100000) for _ in range(n)],
        'few_unique': lambda n: [random.choice([1, 2, 3]) for _ in range(n)]
    }

    for size in sizes:
        for dist_name, dist_func in distributions.items():
            arr = dist_func(size)
            for sort_func, name in zip([heapsort, quicksort, mergesort], ['Heapsort', 'Quicksort', 'Mergesort']):
                arr_copy = arr[:]
                start = time.time()
                sort_func(arr_copy)
                end = time.time()
                print(f"{name} on {dist_name} array of size {size}: {end - start:.5f} seconds")
