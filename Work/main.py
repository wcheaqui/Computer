
from Action import perform_action
from Comms.Speak import speak
from Comms.Listen import listen


# Define the main function
def main():

    bot_name = 'Jarvis'

    from fileutils.Greeting import greeting

    greeting()

    while True:
        command = listen()
        if command is None:
            continue
        # Check if the trigger word is present in the user's input
        while bot_name.lower() == command.lower():
            # Prompt the user for the next phrase
            speak("Yes sir, how can I assist you?")
            command = listen()
        if bot_name.lower() in command.lower():
            response = perform_action(command)
        if 'end' in command and 'session' in command:
            return None


if __name__ == "__main__":
    main()

