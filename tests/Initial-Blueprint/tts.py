"""
Developer: @skywalkerSam
Purpose: Text To Speech generator for Cortana AI
Date: 12022.06.15.

"""

import pyttsx3 as pt


def textto_speech(text="Hello World"):
    engine = pt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.getProperty('rate')
    engine.setProperty('rate', 210)
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    textto_speech(
        "Hello I am Cortana, your personal assistant. What can i do for you?")
