

def string_list(input):
    '''
    Function to add a comma at the beginning of each space in a string
    
    Parameters:
    input (str): The input string with spaces
    
    Returns:
    str: The new string with the commas
    '''
    output = ""
    
    # Iterate through the characters in the input string
    for char in input:
        # If the character is a space, add a comma to the output string
        if char == " ":
            output += ", "
        # Otherwise, just add the character to the output string
        else:
            output += char
            
    return output