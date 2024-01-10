

# Define a function to speak the response
def speak(text):
    import pyttsx3

    engine = pyttsx3.init()

    engine.setProperty('rate', 175)
    engine.setProperty('age', 75)

    engine.say(text)
    print(text)
    engine.runAndWait()

