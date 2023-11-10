def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

    >>> multiple_letter_count('yay')
    {'y': 2, 'a': 1}

    >>> multiple_letter_count('Yay')
    {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_dict = {}
    for letter in phrase:
        if list(letter_dict.keys()).count(letter) != 0:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict
