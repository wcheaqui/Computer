def search_files(command, name='', directory='', directory_only=False):
    """
    This function looks for files in a directory that match a given speech pattern.
    
    Parameters
    ----------
    file_name : str
        The speech pattern to search for.
    directory: str
        the directory in which to search

    Returns
    -------
    list
        A list of file names that match the given speech pattern.
        :param name:
        :param directory_only:
        :param command:
        :param file_name:
        :param directory:
    """

    import os
    from Comms import speak, listen

    from fileutils.DeleteFile import delete_file
    from Action import perform_action

    # Iterate through the directory and look for files that match the given speech pattern
    while directory == '':
        directory = ''
        if 'utility' in command:
            directory = '/Users/WCheaq/PycharmProjects/chatbot/make_jarvis/fileutils/'
        elif 'personal project' in command:
            print('test')
            directory = '/Users/WCheaq/PycharmProjects/chatbot/make_jarvis/PersonalProject/'
        elif 'download' in command:
            directory = '/Users/WCheaq/Downloads/'
        elif 'desktop' in command:
            directory = '/Users/WCheaq/Desktop/'
        elif 'work' in command:
            directory = '/Users/WCheaq/PycharmProjects/chatbot/make_jarvis/Work/'
        elif 'current directory' in command:
            directory = '/Users/WCheaq/PycharmProjects/chatbot/make_jarvis/'
        elif 'recipes' in command:
            directory = '/Users/WCheaq/PycharmProjects/chatbot/make_jarvis/PersonalProject/Recipes/'
        if 'named' in command:
            name = command[command.index("named") + 5:].split()[0]
        elif ' name' in command:
            name = command[command.index("name") + 4:].split()[0]
        if directory == '':
            speak("what directory should I look for?")
            command = listen()
    if directory_only:
        if name == '':
            speak("what is the new directory name?")
            name = listen()
        print(command, directory, name)
        perform_action(command, directory=directory, new_name=name)
        return

    file_name = name

    if file_name == '':
        speak("What file would you like me to look for?")
        file_name = listen()

    files = []
    for file in os.listdir(directory):
        if file_name in file.lower():
            files.append(file)

    if len(files) == 0:
        search_files(command='')

    for i in files:
        speak(f"found {i}. What would you like me to do with it?")
        command = listen()
        if 'delete' not in command:
            with open(i, 'r') as f:
                perform_action(command, file=f.read(), old_file_path=i)
        elif 'delete' in command and 'file' in command:
            delete_file(directory + i)
    return files


