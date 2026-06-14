import tracemalloc


def bubble_sort_strings(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def sort_with_memory_measure(data):
    #Сортирует список строк
    arr = data.copy()  # создаём копию
    tracemalloc.start()
    bubble_sort_strings(arr)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return arr, current


# Пример использования
if __name__ == "__main__":
    test_strings = ["banana", "apple", "grape", "cherry", "date"]
    sorted_list, mem_kb = sort_with_memory_measure(test_strings)

    print(sorted_list)  # только отсортированный список
    print(f"{mem_kb:.2f} Bytes")