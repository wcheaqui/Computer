

def camel_case(string):
    """
    This function takes a string as an argument and converts it to camelCase
    """
    # split the string into an array of words
    words = string.split()

    # capitalize the first letter of each word
    capitalizedWords = [word.capitalize() for word in words]

    # join the words together, removing the spaces
    return ''.join(capitalizedWords)
