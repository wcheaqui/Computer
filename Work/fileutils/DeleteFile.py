
def delete_file(file_name):
    import os

    from Comms import speak, listen

    speak(f"Are you sure you would like to delete {file_name}")
    if listen() == 'yes':
        try:
            os.remove(file_name)
            speak(f"{file_name} deleted successfully.")
        except:
            speak(f"Error deleting {file_name}.")
    else:
        speak(f"I will not delete {file_name}")
