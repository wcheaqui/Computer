def greeting():
    import datetime
    from Comms import speak, get_weather

    # Get the current time
    current_time = datetime.datetime.now()

    # Format the time as HH:MM:SS
    hour = int(current_time.strftime('%H'))
    minute = current_time.strftime('%-M')
    hour_12 = current_time.strftime('%-I')
    am_pm = current_time.strftime('%p')

    weekday = current_time.strftime('%A')
    month = current_time.strftime('%B')
    day = current_time.strftime('%-d')

    if hour < 5:
        speak("Wow it is late. Go to bed.")
    elif hour < 12:
        speak(f"Good morning it is {weekday},{month} {day}. The time is {hour_12}:{minute} {am_pm}")
        if hour < 8:
            get_weather()
    elif hour < 17:
        speak(f"Good afternoon. It is {weekday}, {month} {day}. The time is {hour_12}:{minute} {am_pm}")
    else:
        speak(f"Good evening")


