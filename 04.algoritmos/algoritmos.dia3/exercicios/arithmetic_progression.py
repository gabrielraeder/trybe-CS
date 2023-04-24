def pa(nums: list):
    nums.sort()
    start = 0
    if len(nums) <= 2:
        return True
    razao = nums[start + 1] - nums[start]
    if nums[1] + razao == nums[2]:
        start += 1
        return pa(nums[start:])
    return False


lista = [9, 7, 1, 3, 5]
print(pa(lista))
