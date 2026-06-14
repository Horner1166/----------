# 1
# Enqueue(1) - [1]
# Enqueue(2) - [1,2]
# Dequeue() - [2]
# Enqueue(1) - [2,3]
# Dequeue() - [3]
# Dequeue() - []


class Stack:
    def __init__(self, items = None):
        if items is None:
            self.items = []
        else:
            self.items = list(items)

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Стэк пуст")

    def peek_stack(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Стэк пуст")

stack2 = Stack()
print(stack2.is_empty())

stack2.push(1)
stack2.push(2)
stack2.push(3)
stack2.push(4)
stack2.push(5)

print(stack2.items)
print(stack2.peek_stack())

stack3 = Stack(["x", "y"])

stack3.push("z")
stack3.pop()
stack3.push("w")
stack3.pop()

print(stack3.items)
