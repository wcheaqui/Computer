def update_python_files(file, path, new_lines):
    """This function takes a file, path, and new lines and updates the python file with the new lines at the end of the file. 
    
    Args: 
        file (str): Name of the file to update
        path (str): Path to the file
        new_lines (str): The new lines to add to the file
    
    Returns: 
        None
    """
    with open(path + file, 'a') as f:
        f.write(new_lines)
    f.close()