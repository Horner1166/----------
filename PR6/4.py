from collections import deque

string = "Используя очередь, реализуйте алгоритм циклического сдвига строки на N символов вправо"
    
def cyclic_shift_right(s, n):
    if not s:
        return s
    q = deque(s)
    for _ in range(n):
        q.appendleft(q.pop())
    return ''.join(q)

print(cyclic_shift_right(string, 5))