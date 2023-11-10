def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

    >>> three_odd_numbers([1, 2, 3, 4, 5])
    True

    >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
    True

    >>> three_odd_numbers([5, 2, 1])
    False

    >>> three_odd_numbers([1, 2, 3, 3, 2])
    False
    """
    f_index = 0
    l_index = 3
    length = len(nums[1:-1])
    for n in range(length):
        total = 0
        for s in nums[f_index:l_index]:
            total += s
        if total % 2 != 0:
            return True
        f_index += 1
        l_index += 1
    return False
