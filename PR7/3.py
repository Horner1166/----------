from collections import deque

class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __repr__(self):
        return f"{self.title} ({self.year})"

def quick_sort_queue(arr):
    queue = deque()
    queue.append((0, len(arr) - 1))

    while queue:
        low, high = queue.popleft()
        if low < high:
            pivot_index = partition(arr, low, high)
            queue.append((low, pivot_index - 1))
            queue.append((pivot_index + 1, high))

def partition(arr, low, high):
    pivot = arr[high].year
    i = low - 1

    for j in range(low, high):
        if arr[j].year <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

books = [
    Book("A", 2001),
    Book("B", 1999),
    Book("C", 2010),
    Book("D", 2005)
]

quick_sort_queue(books)
print(books)