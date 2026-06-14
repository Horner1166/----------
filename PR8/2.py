import struct
import random
from typing import Tuple

class SortedChainedHashTable:
    """Хеш-таблица, где цепочки поддерживаются сортированными (вставкой)."""

    def __init__(self, size: int = 101):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.total_comparisons = 0
        self.search_count = 0

    @staticmethod
    def _float_to_int(f: float) -> int:
        return struct.unpack('Q', struct.pack('d', f))[0]

    def _hash(self, key: float) -> int:
        return self._float_to_int(key) % self.size

    def insert(self, key: float) -> None:
        idx = self._hash(key)
        chain = self.table[idx]
        i = 0
        while i < len(chain) and chain[i] < key:
            i += 1
        if i < len(chain) and chain[i] == key:
            return          # дубликат пропускаем
        chain.insert(i, key)

    def search(self, key: float) -> Tuple[bool, int]:
        """Возвращает (найден_ли, количество_сравнений)."""
        idx = self._hash(key)
        chain = self.table[idx]
        comparisons = 0
        for k in chain:
            comparisons += 1
            if k == key:
                return True, comparisons
            if k > key:    # дальше ключи только больше
                break
        return False, comparisons

    def search_and_record(self, key: float) -> bool:
        found, comps = self.search(key)
        self.total_comparisons += comps
        self.search_count += 1
        return found

    def average_search_length(self) -> float:
        if self.search_count == 0:
            return 0.0
        return self.total_comparisons / self.search_count


def measure_average(n: int = 2000, table_size: int = 251) -> float:
    table = SortedChainedHashTable(table_size)
    keys = [random.uniform(-1000, 1000) for _ in range(n)]
    for k in keys:
        table.insert(k)
    for k in keys:
        table.search_and_record(k)
    return table.average_search_length()


if __name__ == "__main__":
    avg = measure_average()
    print(f"Средняя длина поиска (число сравнений): {avg:.4f}")