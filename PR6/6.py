class BrowserHistory:
    def __init__(self, homepage: str):
        self.back_stack = []
        self.forward_stack = []
        self.current = homepage

    def visit(self, url) -> None:
        self.back_stack.append(self.current)
        self.forward_stack.clear()
        self.current = url

    def back(self) -> str:
        if not self.back_stack:
            return self.current
        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        return self.current

    def forward(self) -> str:
        if not self.forward_stack:
            return self.current
        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        return self.current

    def __repr__(self):
        """Для наглядного вывода состояния истории."""
        return (f"Текущая: {self.current}\n"
                f"Стек 'назад': {self.back_stack}\n"
                f"Стек 'вперёд': {self.forward_stack}\n")

if __name__ == "__main__":
    history = BrowserHistory("google.com")
    print("Гугл")
    print(history)

    print("переход на Ютуб")
    history.visit("youtube.com")
    print(history)

    print("Вернуться к гугл")
    history.back()
    print(history)

    print("Перейти на ютуб")
    history.forward()
    print(history)