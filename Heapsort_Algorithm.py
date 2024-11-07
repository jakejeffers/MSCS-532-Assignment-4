def heapify(arr, n, i):
    # i is the index of the element we need to heapify
    # n is the size of the heap
    largest = i
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If the left child is larger than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If the right child is larger than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest isn't the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Step 1: Build a max-heap from the array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (largest) to the end
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify the reduced heap
        heapify(arr, i, 0)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
print("Sorted array is:", arr)
