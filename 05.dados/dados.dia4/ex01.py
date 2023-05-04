from linked_list_content import LinkedList


def remove_duplicates(linked: LinkedList):
    nums = set()
    for i in range(linked.__len__()):
        nums.add(linked.get_element_at(i).value)
    newLinked = LinkedList()
    for num in nums:
        newLinked.insert_last(num)
    return newLinked


def delete_duplicates(linked_list):
    list_with_unique_elements = LinkedList()

    while linked_list:
        current_node = linked_list.remove_first()
        if list_with_unique_elements.index_of(current_node.value) == -1:
            list_with_unique_elements.insert_last(current_node.value)

    return list_with_unique_elements


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at(1, 1)
    linked_list.insert_at(1, 2)
    linked_list.insert_at(2, 3)
    linked_list.insert_at(3, 4)
    print(linked_list)
    result = delete_duplicates(linked_list)

    print(result)
