

def play_youtube_video(command):

    from Comms import speak, listen
    import pywhatkit

    search = command[command.rindex('Tube') + 5:]

    speak(f"Do you want to play {search} on YouTube")

    confirm = listen()
    while 'yes' not in confirm:
        speak(f"My apologies. What do you want to search for?")
        search = listen()
        speak(f"Do you want to play {search} then?")
        confirm = listen()

    pywhatkit.playonyt(command)


