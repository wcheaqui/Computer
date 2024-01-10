def snake_case(string):
    """
    This function takes a string and converts it to snake case
    """
    # replace any spaces with underscores
    string = string.replace(' ', '_')
    # lowercase the string
    string = string.lower()
    # return the new string
    return string
