# Удалите из кортежа первый и последний элемент (создав новый кортеж).
base_tuple = (10, -3, 7, 0, 15, -8, 22, 4, -1, 11)
lst = list(base_tuple)
new_tuple = tuple(lst[1:-1])
print(new_tuple)