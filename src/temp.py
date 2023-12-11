import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Example usage:
text_to_speech("Hello, this is a test. I hope this works!")
