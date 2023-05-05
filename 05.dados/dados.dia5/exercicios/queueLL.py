from linked_list_content import LinkedList

# from node import Node


class Queue:
    def __init__(self) -> None:
        self.queue = LinkedList()

    def enqueue(self, value):
        self.queue.insert_first(value)

    def dequeue(self):
        return self.queue.remove_first()

    def peek(self):
        return self.queue.get_element_at(0)

    def is_empty(self):
        return not len(self.queue)

    def __str__(self):
        str_items = ""
        for i in range(len(self.queue)):
            value = self.queue.get_element_at(i)
            str_items += str(value)
            if i + 1 < len(self.queue):
                str_items += ", "

        return "Queue(" + str_items + ")"


if __name__ == "__main__":
    elements = ["Milkshake", "Batata Frita", "Refrigerante"]
    queue = Queue()

    print(queue)

    for elem in elements:
        queue.enqueue(elem)

    print(queue)

    queue.dequeue()
    print(queue)

    print(queue.peek())
