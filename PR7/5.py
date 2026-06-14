def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)

    count = [0] * (max_val - min_val + 1)

    for num in arr:
        count[num - min_val] += 1

    sorted_arr = []
    for i, c in enumerate(count):
        sorted_arr.extend([i + min_val] * c)

    return sorted_arr

arr = [1, 3, 1, 2, 1, 4, 1, 1]  # 1 встречается >50%
print(counting_sort(arr))