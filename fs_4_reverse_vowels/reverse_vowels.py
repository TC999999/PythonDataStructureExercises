def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    s_list = list(s)
    con_list = [l if "aeiou".count(l.lower()) == 0 else None for l in s_list]

    vowel_list = [l for l in s_list if "aeiou".count(l.lower()) != 0]
    vowel_list.reverse()

    for vowel in vowel_list:
        i = con_list.index(None)
        con_list.insert(i, vowel)
        con_list.pop(i + 1)
    return "".join(con_list)
