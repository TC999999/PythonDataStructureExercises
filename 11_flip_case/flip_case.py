def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

    >>> flip_case('Aaaahhh', 'a')
    'aAAAhhh'

    >>> flip_case('Aaaahhh', 'A')
    'aAAAhhh'

    >>> flip_case('Aaaahhh', 'h')
    'AaaaHHH'

    """
    new_phrase = []
    for letter in phrase:
        if letter == to_swap or letter == to_swap.swapcase():
            letter = letter.swapcase()
            new_phrase.append(letter)
        else:
            new_phrase.append(letter)

    return "".join(new_phrase)
