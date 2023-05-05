from linked_list_content import LinkedList
from node import Node


class Stack:
    def __init__(self) -> None:
        self.data = LinkedList()

    def size(self):
        return len(self.data)

    def push(self, value):
        self.data.insert_last(value)

    def pop(self):
        return self.data.remove_last()

    def peek(self):
        return self.data.get_element_at(len(self.data) - 1)

    def is_empty(self):
        return self.data.is_empty()

    def __str__(self):
        str_items = ""
        for i in range(self.size()):
            value = self.data.get_element_at(i)
            str_items += str(value)
            if i + 1 < self.size():
                str_items += ", "
        return "Stack(" + str_items + ")"

    def min_value(self):
        values = []
        for i in range(self.size()):
            values.append(self.data.get_element_at(i).value)
        return Node(min(values))


if __name__ == "__main__":
    elements = [1, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    content_stack = Stack()

    for elem in elements:
        content_stack.push(elem)

    print(content_stack)

    print(content_stack.size())

    print("pop -->", content_stack.pop())
    print("pop -->", content_stack.pop())

    print("peek -->", content_stack.peek())

    print(content_stack)
    print("=" * 50)
    print(content_stack.min_value())
