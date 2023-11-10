def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

    >>> vowel_count('rithm school')
    {'i': 1, 'o': 2}

    >>> vowel_count('HOW ARE YOU? i am great!')
    {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowel_dict = {}
    for letter in phrase.lower():
        if "aeiou".find(letter) != -1:
            if list(vowel_dict.keys()).count(letter) != 0:
                vowel_dict[letter] += 1
            else:
                vowel_dict[letter] = 1
    return vowel_dict
