

def move_file(command, old_file_path, directory):
    from fileutils import search_files
    from Comms import speak, listen
    import shutil

    command_later = ''
    if old_file_path == '':
        if 'put' in command:
            command_later = command[command.index("put"):]
            command = command[:command.index("put")]
        search_files(command)
        if command_later != '':
            command = command_later

    else:
        speak(f'where would you like me to put {old_file_path}')
        command = listen()
    search_files(command=command, directory_only=True)
    shutil.move(old_file_path, directory)
