def titleize(phrase):
    """Return phrase in title case (each word capitalized).

    >>> titleize('this is awesome')
    'This Is Awesome'

    >>> titleize('oNLy cAPITALIZe fIRSt')
    'Only Capitalize First'
    """
    words = phrase.split(" ")
    new_phrase = []
    for word in words:
        new_word = word.capitalize()
        new_phrase.append(new_word)
    return " ".join(new_phrase)
