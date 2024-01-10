
def responses_load(search_criteria, prompt, conversation='Responses.json'):
    import json
    """
    Loads a response file from disc, matches on keys and updates any additional
    dictionary items that do not match.
 
    Parameters
    ----------
    converstion : str
        The name of the json file to be loaded
    prompt : dict
        The dictionary containing the keys and values
 
    Returns
    -------
    dict
        The updated dictionary
    """
    # Read response file
    with open(conversation) as f:
        response_data = json.load(f)
    # Iterate over the response data and update the dictionary
    for k, v in response_data.items():
        if search_criteria in k or search_criteria in v:
            response_data[k] = v
        else:
            dictionary[name + '_' + key] = value
    return dictionary