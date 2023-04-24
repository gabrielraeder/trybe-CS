from cronometro import Cronometro

test1 = [True, True, True, True, False, False, False]  # saída: 4


test2 = [True, True, False, False, False, False, False]  # saída: 2


def search_fail_test(bool_list: list):
    start = 0
    end = len(bool_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if bool_list[mid] is False:
            end = mid - 1
        if bool_list[mid] is True:
            start = mid + 1
    return mid


def search_recursive(bool_list: list, start, end):
    mid = (start + end) // 2
    if start == end:
        return mid
    if start <= end:
        if bool_list[mid] is False:
            return search_recursive(bool_list, start, mid - 1)
        if bool_list[mid] is True:
            return search_recursive(bool_list, mid + 1, end)


with Cronometro("search_fail_test1"):
    print(search_fail_test(test1))
with Cronometro("search_fail_test2"):
    print(search_fail_test(test2))

with Cronometro("search_recursive1"):
    print(search_recursive(test1, 0, len(test1)))

with Cronometro("search_recursive2"):
    print(search_recursive(test2, 0, len(test2)))
