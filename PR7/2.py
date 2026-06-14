import heapq
import time
import random

def test_heap_operations(data):
    heap = []

    # Insert
    start = time.time()
    for item in data:
        heapq.heappush(heap, item)
    insert_time = time.time() - start

    # DeleteMax
    max_heap = [-x for x in data]

    start = time.time()
    while max_heap:
        heapq.heappop(max_heap)
    delete_time = time.time() - start

    return insert_time, delete_time

sizes = [1000, 5000, 10000]

for size in sizes:
    data_int = [random.randint(0, 100000) for _ in range(size)]
    insert_t, delete_t = test_heap_operations(data_int)

    print(f"Размер: {size}")
    print(f"Insert: {insert_t:.6f} сек")
    print(f"DeleteMax: {delete_t:.6f} сек\n")