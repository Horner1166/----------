import struct
from typing import Optional

class QuadraticProbingHashTable:
    """Открытая адресация, смещение i^2. Без удаления."""

    def __init__(self, size: int = 101):
        self.size = size
        self.table: list[Optional[float]] = [None] * size

    @staticmethod
    def _float_to_int(f: float) -> int:
        return struct.unpack('Q', struct.pack('d', f))[0]

    def _hash(self, key: float) -> int:
        return self._float_to_int(key) % self.size

    def insert(self, key: float) -> bool:
        h = self._hash(key)
        for i in range(self.size):
            idx = (h + i * i) % self.size
            if self.table[idx] is None:
                self.table[idx] = key
                return True
            if self.table[idx] == key:
                return False
        raise RuntimeError("Таблица переполнена")

    def search(self, key: float) -> bool:
        h = self._hash(key)
        for i in range(self.size):
            idx = (h + i * i) % self.size
            if self.table[idx] is None:
                return False
            if self.table[idx] == key:
                return True
        return False


if __name__ == "__main__":
    ht = QuadraticProbingHashTable(11)
    for k in [1.0, 12.0, 23.0, 34.0, 45.0]:
        ht.insert(k)

    print("Поиск 23.0:", ht.search(23.0))
    print("Поиск 99.0:", ht.search(99.0))