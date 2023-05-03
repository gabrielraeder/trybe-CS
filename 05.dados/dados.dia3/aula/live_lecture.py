def duplicate(nums):
    return len(set(nums)) < len(nums)


def duplicate2(nums):
    for i in nums:
        if nums.count(i) > 1:
            return True
    return False


# print(duplicate([0, 1, 2, 3]))
# print(duplicate([0, 2, 2, 3]))

# print(duplicate2([0, 1, 2, 3]))
# print(duplicate2([0, 2, 2, 3]))


def kids_candies(candies, extra):
    return [candy + extra >= max(candies) for candy in candies]


candies = [2, 3, 5, 1, 3]
print(kids_candies(candies, 3))
