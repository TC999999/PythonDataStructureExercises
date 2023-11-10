def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    letters = list(phrase.upper())

    no_spaces = [letter for letter in letters if letter != " "]
    reverse = no_spaces.copy()
    reverse.reverse()
    if no_spaces == reverse:
        return True
    else:
        return False
