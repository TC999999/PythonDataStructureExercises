def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

    >>> capitalize('python')
    'Python'

    >>> capitalize('only first word')
    'Only first word'
    """
    phr_list = list(phrase)
    phr_list[0] = phr_list[0].upper()
    return "".join(phr_list)
