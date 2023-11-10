def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

    >>> same_frequency(551122, 221515)
    True

    >>> same_frequency(321142, 3212215)
    False

    >>> same_frequency(1212, 2211)
    True
    """
    num1_lst = list(str(num1))
    num2_lst = list(str(num2))

    num1_lst.sort()
    num2_lst.sort()

    return num1_lst == num2_lst
