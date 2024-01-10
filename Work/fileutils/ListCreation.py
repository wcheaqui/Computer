

def listCreation(drink: str):
    #Create an empty list
    drink_list = []
    
    #Split the string by spaces and add each word to the list
    for word in drink.split():
        drink_list.append(word)
    
    #return the new list
    return drink_list

