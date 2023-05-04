from double_linked_list import DoubleLinkedList


def remove_duplicates(linked: DoubleLinkedList):
    new_list = DoubleLinkedList()

    while linked:
        removed = linked.remove_first()
        if new_list.index_of(removed.value) == -1:
            new_list.insert_last(removed.value)

    return new_list


if __name__ == "__main__":
    print("=" * 40)
    double_linked = DoubleLinkedList()
    double_linked.insert_at(1, 1)
    double_linked.insert_at(1, 2)
    double_linked.insert_at(2, 3)
    double_linked.insert_at(3, 4)
    print(double_linked)
    result = remove_duplicates(double_linked)
    print("=" * 40)
    print(result)
