from collections import deque

class StackWithQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        # Кладем x в пустую очередь
        self.q1.append(x)
        # Перемещаем все из q1 в q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Меняем местами q1 и q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            raise IndexError("нет элементов для удаления")
        return self.q1.popleft()

    def is_empty(self):
        return not self.q1

stack = StackWithQueues()

stack.push(1)
stack.push(2)

print(stack.q1)
print(stack.q2)