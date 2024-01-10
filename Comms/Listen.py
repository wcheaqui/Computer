

# Define a function to recognize speech
def listen():
    import speech_recognition as sr
    import beepy

    # Initialize the speech recognizer and engine
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source)
        beepy.beep(sound=1)
        while True:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print(f'heard: {text}')
                return text
            except Exception as e:
                print(e)
                continue
