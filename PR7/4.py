def quick_sort_verbose(arr, low, high):
    if low < high:
        pivot_index = partition_verbose(arr, low, high)
        print(f"Pivot на позиции {pivot_index}: {arr}")
        quick_sort_verbose(arr, low, pivot_index - 1)
        quick_sort_verbose(arr, pivot_index + 1, high)

def partition_verbose(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [10, 7, 8, 9, 1, 5]
quick_sort_verbose(arr, 0, len(arr) - 1)