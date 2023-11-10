def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    sum_pair_list = [()]
    last_index = len(nums)
    new_nums = nums.copy()
    for num1 in nums:
        new_nums.pop(0)
        for num2 in new_nums:
            if (num1 + num2) == goal:
                sum_pair = (num1, num2)
                new_last_index = nums.index(num2)
                if new_last_index <= last_index:
                    last_index = new_last_index
                    sum_pair_list.append(sum_pair)
                    sum_pair_list[0:1] = []

    return sum_pair_list[0]
