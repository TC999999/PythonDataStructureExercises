def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    total = 0
    new_nums = nums.copy()
    if start != 0 and end == None:
        new_nums[:start] = []
    elif start == 0 and end != None:
        new_nums[end + 1 :] = []
    elif start != 0 and end != None:
        new_nums = new_nums[start : end + 1]

    for num in new_nums:
        total += num
    return total
