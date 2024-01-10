

def rename_file(command, old_file_path):
    from fileutils import search_files, camel_case
    from Comms import speak, listen
    import shutil

    if old_file_path == '':
        search_files(command)
    new_file_name = ''
    agreeable_name = 'no'
    while 'yes' not in agreeable_name:
        speak("what would you like to name it?")
        new_file_name = camel_case(listen())
        speak(f"is the {new_file_name} name satisfactory to you?")
        agreeable_name = listen()
    shutil.move(old_file_path, new_file_name)