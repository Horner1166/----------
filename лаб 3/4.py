# Ротация ключей и значений.
# Напишите функцию, которая "циклически" сдвигает ключи словаря.
# Значение каждого ключа присваивается следующему ключу, а значение последнего ключа - первому.
def sdvig(diction):
    keys = list(diction.keys())
    values = list(diction.values())
    sdvig_v = [values[-1]] + values[:-1]
    return dict(zip(keys, sdvig_v))

diction = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
sdv = sdvig(diction)
print(sdv)