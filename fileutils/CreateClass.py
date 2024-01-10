

def create_class(command):
    speak("what are you creating a class for?")
    class_create = listen()
    speak("what class will it have any inheritance?")
    inheritance = listen()

    if 'no ' not in inheritance and 'none' not in inheritance:
        inheritance = f' and the class should inherit the following classes ' + string_list(inheritance)

    speak("Would you like to name the class?")
    class_name_question = listen()