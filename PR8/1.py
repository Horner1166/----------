import struct

class ChainedHashTable:
    """Хеш-таблица с раздельными цепочками. Ключ — float, хеш — по битовому представлению."""

    def __init__(self, size: int = 101):
        self.size = size
        self.table = [[] for _ in range(size)]

    @staticmethod
    def _float_to_int(f: float) -> int:
        # Преобразуем float в беззнаковое 64-битное целое (IEEE 754)
        return struct.unpack('Q', struct.pack('d', f))[0]

    def _hash(self, key: float) -> int:
        return self._float_to_int(key) % self.size

    def insert(self, key: float) -> None:
        idx = self._hash(key)
        self.table[idx].append(key)

    def search(self, key: float) -> bool:
        idx = self._hash(key)
        return key in self.table[idx]

    def display(self):
        for i, chain in enumerate(self.table):
            if chain:
                print(f"{i}: {chain}")

# ---- демонстрация ----
if __name__ == "__main__":
    ht = ChainedHashTable(7)
    for val in [1.1, 2.2, 3.3, 10.1, 17.1]:
        ht.insert(val)
    ht.display()
    print("Поиск 3.3:", ht.search(3.3))
    print("Поиск 99.9:", ht.search(99.9))