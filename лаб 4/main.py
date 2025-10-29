
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def to_lst(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    def from_lst(self, lst):
        self.head = None
        for x in lst:
            self.append(x)

    def print_lst(self):
        cur = self.head
        while cur:
            print(cur.data, end=", ")
            cur = cur.next
        print("0")

def create_link_lst():
    lst = LinkedList()
    print("Введите элементы списка, 0 - конец списка")
    while True:
        try:
            num = int(input())
        except ValueError:
            print("Целое число")
            continue
        if num == 0:
            break
        lst.append(num)
    return lst

def find_aver(linked_list):
    values = linked_list.to_lst()
    if not values:
        return 0
    return sum(values) / len(values)

def remove_greater_than_average(linked_list, avg):
    dummy = Node(0)
    dummy.next = linked_list.head
    prev, cur = dummy, linked_list.head

    while cur:
        if cur.data > avg:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    linked_list.head = dummy.next

def insrt_aft_even(linked_list):
    cur = linked_list.head
    while cur:
        if cur.data % 2 ==0:
            new_node = Node(100)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        else:
            cur = cur.next

def sort_desc(linked_list):
    values = linked_list.to_lst()
    values.sort(reverse=True)
    linked_list.from_lst(values)

if __name__ == "__main__":
    lst = create_link_lst()

    print("\nИсходный список:")
    lst.print_lst()

    avg = find_aver(lst)
    print(f"Среднее Арифметическое: {avg:.2f}")

    remove_greater_than_average(lst, avg)
    print("\nУдаляются элементы, которые больше среднего арифметического:")
    lst.print_lst()

    insrt_aft_even(lst)
    print("\nВставляется число 100 после каждого четного числа:")
    lst.print_lst()

    sort_desc(lst)
    print("\nСортировки по убыванию:")
    lst.print_lst()