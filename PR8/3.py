import struct
from typing import Tuple, Optional

class LinearProbingHashTable:
    """Линейное пробирование: поиск возвращает (найден, шаги)."""

    DELETED = object()

    def __init__(self, size: int = 101):
        self.size = size
        self.table: list[Optional[float]] = [None] * size

    @staticmethod
    def _float_to_int(f: float) -> int:
        return struct.unpack('Q', struct.pack('d', f))[0]

    def _hash(self, key: float) -> int:
        return self._float_to_int(key) % self.size

    def insert(self, key: float) -> bool:
        idx = self._hash(key)
        for i in range(self.size):
            probe = (idx + i) % self.size
            if self.table[probe] is None or self.table[probe] is self.DELETED:
                self.table[probe] = key
                return True
            if self.table[probe] == key:
                return False
        raise RuntimeError("Таблица переполнена")

    def search(self, key: float) -> Tuple[bool, int]:
        idx = self._hash(key)
        steps = 0
        for i in range(self.size):
            probe = (idx + i) % self.size
            steps += 1
            if self.table[probe] is None:
                return False, steps
            if self.table[probe] != self.DELETED and self.table[probe] == key:
                return True, steps
        return False, steps


if __name__ == "__main__":
    ht = LinearProbingHashTable(11)
    for k in [0.5, 11.5, 22.5, 33.5, 44.5]:
        ht.insert(k)

    found, steps = ht.search(22.5)
    print(f"Поиск 22.5: найден={found}, шагов={steps}")
    found, steps = ht.search(99.9)
    print(f"Поиск 99.9: найден={found}, шагов={steps}")