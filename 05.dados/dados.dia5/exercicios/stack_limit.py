from stackLL import Stack


class LimitStack(Stack):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def push(self, value):
        if self.size() >= self.limit:
            raise OverflowError
        super().push(value)


if __name__ == "__main__":
    content_stack = LimitStack(2)
    content_stack.push(1)
    content_stack.push(-2)

    try:
        content_stack.push(3)
    except OverflowError:
        print("Não é possível adicionar outro item à pilha")
