class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority  # Lower priority number means higher priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        # Comparison based on priority for min-heap (task with lower priority value comes first)
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(id={self.task_id}, priority={self.priority}, arrival={self.arrival_time}, deadline={self.deadline})"

class MinHeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_task = self.heap[0]  # The task with the smallest priority (earliest deadline)
        self.heap[0] = self.heap.pop()  # Replace root with the last task in the heap
        self._heapify_down(0)  # Restore the heap property by bubbling down
        return min_task

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1  # Left child index
        right = 2 * index + 2  # Right child index

        # Compare with left child
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        # Compare with right child
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current node, swap and continue heapifying
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def update_priority(self, task_id, new_priority):
        index = next((i for i, task in enumerate(self.heap) if task.task_id == task_id), None)
        if index is None:
            return  # Task not found

        old_priority = self.heap[index].priority
        self.heap[index].priority = new_priority  # Update the priority

        # If the new priority is lower (more urgent), bubble up
        if new_priority < old_priority:
            self._heapify_up(index)
        # If the new priority is higher (less urgent), bubble down
        else:
            self._heapify_down(index)

    def is_empty(self):
        return len(self.heap) == 0

# Test function to validate insert and extract_min operations
def test_insert_and_extract_min():
    # Create the priority queue
    pq = MinHeapPriorityQueue()

    # Create a single task
    task1 = Task(1, 3, "2024-11-06 09:00", "2024-11-06 12:00")

    # Insert the task into the heap
    pq.insert(task1)

    # Extract the task with the minimum priority (earliest deadline)
    extracted_task = pq.extract_min()

    # Check if the extracted task is the same as the one inserted
    print("Test - Insert and Extract Min:")
    print(f"Inserted task: {task1}")
    print(f"Extracted task: {extracted_task}")
    
    # Ensure that the extracted task is the same as the inserted one
    assert extracted_task == task1, "Test failed: The extracted task is not the same as the inserted one"
    print("Test passed!")

# Run the test
test_insert_and_extract_min()
