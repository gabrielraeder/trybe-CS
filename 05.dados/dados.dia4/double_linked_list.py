from nodeDouble import DoubleNode


class DoubleLinkedList:
    def __init__(self):
        self.head_value = None
        self.tail_value = None
        self.__length = 0

    def __str__(self):
        return f"DoubleLinked(len={self.__length}, value={self.head_value})"

    def __len__(self):
        return self.__length

    def is_empty(self):
        return not self.__length

    def insert_first(self, value):
        first_value = DoubleNode(value)
        first_value.next = self.head_value
        if isinstance(self.head_value, DoubleNode):
            self.head_value.previous = first_value
        self.head_value = first_value
        self.__length += 1
        if self.__len__() == 1:
            self.tail_value = self.head_value

    def insert_last(self, value):
        last_value = DoubleNode(value)
        last_value.previous = self.tail_value
        if isinstance(self.tail_value, DoubleNode):
            self.tail_value.next = last_value
        self.tail_value = last_value
        self.__length += 1
        if self.__len__() == 1:
            self.head_value = self.tail_value

    def insert_at(self, value, position):
        if position < 1:
            return self.insert_first(value)
        if position >= len(self):
            return self.insert_last(value)
        current_value = self.head_value
        while position > 1:
            current_value = current_value.next
            position -= 1
        next_value = DoubleNode(value)
        current_value.next.previous = next_value
        next_value.next = current_value.next
        next_value.previous = current_value
        current_value.next = next_value
        self.__length += 1

    def remove_first(self):
        value_to_be_removed = self.head_value
        if value_to_be_removed:
            self.head_value = self.head_value.next
            if isinstance(self.head_value, DoubleNode):
                self.head_value.previous = None
            value_to_be_removed.next = None
            self.__length -= 1
        return value_to_be_removed

    def remove_last(self):
        value_to_be_removed = self.tail_value
        if value_to_be_removed:
            self.tail_value = self.tail_value.previous
            if isinstance(self.tail_value, DoubleNode):
                self.tail_value.next = None
            value_to_be_removed.previous = None
            self.__length -= 1
        return value_to_be_removed

    def remove_at(self, position):
        if position < 1:
            return self.remove_first()
        if position >= len(self):
            return self.remove_last()

        previous_to_be_removed = self.head_value

        while position > 1:
            previous_to_be_removed = previous_to_be_removed.next
            position -= 1

        value_to_be_removed = previous_to_be_removed.next
        previous_to_be_removed.next = value_to_be_removed.next
        value_to_be_removed.next.previous = previous_to_be_removed
        value_to_be_removed.next = None
        value_to_be_removed.previous = None
        self.__length -= 1

        return value_to_be_removed

    def get_element_at(self, position):
        value_returned = None
        value_to_be_returned = self.head_value
        if value_to_be_returned:
            while position > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                position -= 1
            if value_to_be_returned:
                value_returned = DoubleNode(value_to_be_returned.value)
                value_returned.next = value_to_be_returned.next
        return value_returned

    def index_of(self, value):
        position = 1
        start = self.head_value
        while position <= self.__len__():
            if start.value == value:
                return position
            start = start.next
            position += 1
        return -1


if __name__ == "__main__":
    lista = DoubleLinkedList()

    print("+" * 50)
    # # print(lista.is_empty())
    # lista.insert_first(1)
    # print(lista)
    # print("+" * 50)
    # lista.insert_last(2)
    # lista.insert_last(4)
    # print(lista)
    # print("+" * 50)
    # lista.insert_at(3, 2)
    # print(lista)
    # print("+" * 50)
    # lista.remove_at(2)
    # print(lista)
    # print("+" * 50)
    # print(lista)
    # print(lista.get_element_at(1))
    # lista.remove_first()
    # print(lista)
    # print("+" * 50)
    # lista.remove_last()
    # print(lista)
    # print("+" * 50)

    lista.insert_at(1, 1)
    lista.insert_at(1, 2)
    lista.insert_at(3, 3)
    lista.insert_at(1, 4)
    print(lista)
    print("+" * 50)
    print(lista.index_of(3))
