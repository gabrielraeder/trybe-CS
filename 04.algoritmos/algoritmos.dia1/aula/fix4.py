def fix4(arr1, arr2):
    index_list = []
    for item in arr1:
        start = 0
        end = len(arr2) - 1
        while start <= end:
            print(start)
            mid = (start + end) // 2
            if item == arr2[mid]:
                index_list.append({"item": item, "posição": mid})
                break
            elif item == arr2[start]:
                index_list.append({"item": item, "posição": start})
                break
            elif item == arr2[end]:
                index_list.append({"item": item, "posição": end})
                break
            start += 1
            end -= 1
    return index_list


numbers1 = [2, 3, 4, 10, 40]
numbers2 = [3, 1, 4, 2, 10, 40]

print(fix4(numbers1, numbers2))
