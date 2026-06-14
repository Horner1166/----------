import struct
from typing import Optional

class OrderedQuadraticHashTable:
    """
    Квадратичное пробирование (шаги +1, +4, +9, …) с упорядочиванием ключей.
    При коллизии, если вставляемый ключ меньше находящегося в ячейке,
    они меняются местами, и вытесненный ключ продолжает пробирование.
    """

    def __init__(self, size: int = 101):
        self.size = size
        self.table: list[Optional[float]] = [None] * size

    @staticmethod
    def _float_to_int(f: float) -> int:
        return struct.unpack('Q', struct.pack('d', f))[0]

    def _hash(self, key: float) -> int:
        return self._float_to_int(key) % self.size

    def insert(self, key: float) -> None:
        idx = self._hash(key)
        i = 1              # первый шаг смещения – 1^2 = 1
        current = key
        while True:
            offset = i * i
            probe = (idx + offset) % self.size
            if self.table[probe] is None:
                self.table[probe] = current
                return
            if self.table[probe] == current:
                return      # уже есть
            if current < self.table[probe]:
                # меняем местами: более «лёгкий» ключ остаётся, более «тяжёлый» идёт дальше
                self.table[probe], current = current, self.table[probe]
            i += 1

    def search(self, key: float) -> bool:
        idx = self._hash(key)
        i = 1
        while True:
            offset = i * i
            probe = (idx + offset) % self.size
            if self.table[probe] is None:
                return False
            if self.table[probe] == key:
                return True
            if self.table[probe] > key:
                # дальше ключи только больше
                return False
            i += 1


if __name__ == "__main__":
    oq = OrderedQuadraticHashTable(11)
    for k in [5.0, 16.0, 27.0, 6.0, 17.0]:
        oq.insert(k)
    print("Таблица:", [v for v in oq.table])
    print("Поиск 6.0:", oq.search(6.0))
    print("Поиск 15.0 (отсутствует):", oq.search(15.0))