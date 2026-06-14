import struct
from typing import List, Tuple, Optional

class DoubleHashTable:
    """Двойное хеширование: h(k,i) = (h1 + i*h2) mod size."""

    def __init__(self, size: int = 101):
        self.size = size
        self.table: list[Optional[float]] = [None] * size

    @staticmethod
    def _float_to_int(f: float) -> int:
        return struct.unpack('Q', struct.pack('d', f))[0]

    def _h1(self, key: float) -> int:
        return self._float_to_int(key) % self.size

    def _h2(self, key: float) -> int:
        # h2 ∈ [1, size-2], взаимно простое с size (size простое)
        raw = self._float_to_int(key)
        return 1 + (raw % (self.size - 2))

    def insert(self, key: float) -> List[int]:
        """Вставка, возвращает последовательность индексов проб."""
        h1 = self._h1(key)
        h2 = self._h2(key)
        probes = []
        for i in range(self.size):
            idx = (h1 + i * h2) % self.size
            probes.append(idx)
            if self.table[idx] is None:
                self.table[idx] = key
                return probes
            if self.table[idx] == key:
                return probes
        raise RuntimeError("Таблица переполнена")

    def search(self, key: float) -> Tuple[bool, List[int]]:
        h1 = self._h1(key)
        h2 = self._h2(key)
        probes = []
        for i in range(self.size):
            idx = (h1 + i * h2) % self.size
            probes.append(idx)
            if self.table[idx] is None:
                return False, probes
            if self.table[idx] == key:
                return True, probes
        return False, probes


if __name__ == "__main__":
    dh = DoubleHashTable(11)
    for k in [3.0, 14.0, 25.0, 36.0]:
        probes = dh.insert(k)
        print(f"Вставка {k}: пробы -> {probes}")
    print("Содержимое таблицы:", [v for v in dh.table])