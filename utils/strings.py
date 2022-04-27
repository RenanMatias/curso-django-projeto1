def is_positive_number(string):
    """
    Check if the string is a positive number.
    """
    try:
        if float(string) > 0:
            return True
        else:
            return False
    except (ValueError, TypeError):
        return False
