def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if type(collection) == set:
        set_lst = list(collection)
        if set_lst.count(sought) != 0:
            return True
        return False
    elif type(collection) == dict:
        val_lst = list(collection.values())
        if val_lst.count(sought) != 0:
            return True
        return False
    else:
        item_lst = list(collection)
        if start == None:
            if item_lst.count(sought) != 0:
                return True
        else:
            item_lst[0:start] = []
            if item_lst.count(sought) != 0:
                return True
        return False
