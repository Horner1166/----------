import random
from operator import index


#1. В одномерном массиве, заполненном случайными числами,
# найти сумму элементов, стоящих на четных позициях (индексах).
def sum_even_positions(arr):
    sum=0
    for num in arr:
        if index(num) % 2 == 0:
            sum+=num
    return sum

#2. В одномерном массиве найти все элементы,
#значение которых больше среднего арифметического всего массива. Вывести их значения и индексы.
def elements_above_average(arr):
    if not arr:
        return []
    avg = sum(arr) / len(arr)
    result = []
    for idx, val in enumerate(arr):
        if val > avg:
            result.append((idx, val))
    return result

#3. Дан массив целых чисел. Создать новый массив,
# который содержит только уникальные (неповторяющиеся) элементы исходного массива.
def unique_elements(arr):
    unique = []
    for num in arr:
        count = arr.count(num)
        if count < 2:
            unique.append(num)
    return unique

#4. Для матрицы (двумерного массива) найти сумму всех элементов.
def matrix_sum(matrix):
    return sum(sum(row) for row in matrix)

#5. Для квадратной матрицы найти сумму элементов на главной диагонали.
def main_diagonal_sum(matrix):
    n = len(matrix)
    return sum(matrix[i][i] for i in range(n))

#6. Реализовать алгоритм "Сдвиг массива".
# Для одномерного массива выполнить циклический сдвиг вправо на `k` элементов.
def cyclic_shift_right(arr, k):
    if not arr:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k]


if __name__ == "__main__":

    arr1 = [random.randint(1, 100) for _ in range(10)]
    print("1. Исходный массив:", arr1)
    print("Сумма на четных позициях:", sum_even_positions(arr1))
    print()

    print("2. Исходный массив:", arr1)
    avg = sum(arr1) / len(arr1)
    print(f"Среднее арифметическое: {avg:.2f}")
    above_avg = elements_above_average(arr1)
    print("Элементы больше среднего (индекс, значение):")
    for idx, val in above_avg:
        print(f"[{idx}] = {val}")
    print()


    arr3 = [random.randint(1, 10) for _ in range(15)]
    print("3. Исходный массив:", arr3)
    print("Уникальные элементы:", unique_elements(arr3))
    print()


    matrix = [[random.randint(1, 20) for _ in range(4)] for _ in range(3)]
    print("4. Матрица 3x4:")
    for row in matrix:
        print(row)
    print("Сумма всех элементов матрицы:", matrix_sum(matrix))
    print()


    square_matrix = [[random.randint(1, 20) for _ in range(4)] for _ in range(4)]
    print("5. Квадратная матрица 4x4:")
    for row in square_matrix:
        print(row)
    print("Сумма главной диагонали:", main_diagonal_sum(square_matrix))
    print()


    arr6 = list(range(1, 9))
    k = 3
    print(f"6. Исходный массив: {arr6}")
    print(f"Циклический сдвиг вправо на {k}: {cyclic_shift_right(arr6, k)}")