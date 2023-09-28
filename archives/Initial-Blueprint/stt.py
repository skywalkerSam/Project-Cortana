"""
Developer: @skywalkerSam 
Purpose: Speech To Text generator for Cortana AI    
Date: 12022.06.15.18:14:00

"""

import speech_recognition as sr


def speechto_text():
    while True:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say Something...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            print("Recognizing Now...\n")
            text = r.recognize_google(audio, language="en-US")
            print("You Said: " + text + "\n")
            break
        except KeyboardInterrupt:
            print("\n\nCancelling Tasks...\n")
            break
        except sr.UnknownValueError:
            print("Sorry, Please say that again...\n")
            continue
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {0}".format(e))
            break
    return text


if __name__ == '__main__':
    speechto_text()
