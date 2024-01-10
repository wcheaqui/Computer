

def copy_file(command, old_file_path):
    from Comms import speak, listen
    from fileutils import search_files
    import os
    import shutil

    if old_file_path == '':
        speak("which file would you like me to move")
        old_file_path = listen()
        search_files(old_file_path)

        speak(f'where would you like me to put {old_file_path}')
        command = listen()

    directory = ''
    while directory == '':
        if 'utility' in command:
            shutil.copy(old_file_path, os.getcwd() + '/fileutils/')
        elif 'download' in command:
            shutil.copy(old_file_path, '/Users/WCheaq/Downloads/')
        elif 'desktop' in command:
            shutil.copy(old_file_path, '/Users/WCheaq/Desktop/')
        elif 'work' in command:
            shutil.copy(old_file_path, os.getcwd() + '/Work/')
        elif 'current directory' in command or 'here' in command:
            shutil.copy(old_file_path, os.getcwd() + '/')
        else:
            speak("I did not find that directory. What was it again?")
            command = listen()