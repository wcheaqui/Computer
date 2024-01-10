

import asyncio
import time
import simpleaudio as sa


async def set_timer(time_amount, type_sound='sound1.wav', reminder_text='Reminder1'):
    """
    This function sets a timer with a specified amount of time and sound, and
    displays a reminder text when the timer goes off.

    Args:
        time_amount (int): the amount of time (in seconds) for the timer
        type_sound (str): the file path of the sound to be played when the timer goes off
        reminder_text (str): the reminder text to be displayed when the timer goes off
    """
    # Convert time_amount to seconds
    time_amount = int(time_amount)

    # Display the reminder text
    print(reminder_text)

    # Wait for the specified amount of time
    await asyncio.sleep(time_amount)

    # Load the sound file
    wave_obj = sa.WaveObject.from_wave_file(type_sound)

    # Play the sound
    play_obj = wave_obj.play()
    play_obj.wait_done()


def set_timer_go(command):

    from Comms import speak, listen

    # Extract the time amount and reminder text from the command
    time_amount = 0
    if 'for' in command and 'minute' in command:
        time_amount = int(command[command.index("for") + 3:].split()[0])

    while time_amount == 0:
        speak("how long would you like the timer for")
        time_amount = int(listen())

    # extract reminder text from command
    if 'reminder text' in command.lower():
        reminder_text = command[command.lower().index("reminder text"):]
    else:
        reminder_text = 'Reminder1'

    # Set the timer using the extracted values
    asyncio.create_task(set_timer(time_amount, reminder_text))


