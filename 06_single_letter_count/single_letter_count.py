def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

    >>> single_letter_count('Hello World', 'h')
    1

    >>> single_letter_count('Hello World', 'z')
    0

    >>> single_letter_count("Hello World", 'l')
    3
    """
    big_word = word.upper()
    big_letter = letter.upper()
    total = 0
    for letters in big_word:
        if big_letter == letters:
            total += 1

    return total
