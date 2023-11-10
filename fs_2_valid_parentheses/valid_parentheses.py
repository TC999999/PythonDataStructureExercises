def valid_parentheses(parens):
    """Are the parentheses validly balanced?

    >>> valid_parentheses("()")
    True

    >>> valid_parentheses("()()")
    True

    >>> valid_parentheses("(()())")
    True

    >>> valid_parentheses(")()")
    False

    >>> valid_parentheses("())")
    False

    >>> valid_parentheses("((())")
    False

    >>> valid_parentheses(")()(")
    False
    """
    if parens.startswith(")"):
        return False
    elif parens.endswith("("):
        return False
    else:
        paren_list = list(parens)
        if paren_list.count("(") != paren_list.count(")"):
            return False
        else:
            return True
