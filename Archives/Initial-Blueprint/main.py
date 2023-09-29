"""
Developer: @skywalkerSam
Purpose: Basic commands for Cortana AI
Date: 12022.06.16.20:57:00

"""

from intro import introduction, greeting
from stt import speechto_text
from tts import textto_speech
import datetime as dt
import os
import webbrowser as wb


if __name__ == '__main__':
    try:
        introduction()
        greeting('Starboy')  # Change the name of the user here
        textto_speech("I'm here...")
        text = speechto_text().lower()

        while True:
            if 'exit' in text:
                print("Exiting Interface...")
                textto_speech('Alright')
                break

            elif 'the time' in text:
                time = dt.datetime.now().strftime("%H:%M:%S")
                print(f"Current Time: {time}")
                textto_speech(f"The time is {time}")
                break

            elif 'open explorer' in text:
                os.system("explorer")
                print("Opening Explorer...")
                textto_speech("Opening Explorer...")
                break

            elif 'open youtube' in text:
                wb.open('https://www.youtube.com/')
                print("Opening Youtube...")
                textto_speech("Opening Youtube...")
                break

            else:
                print("Sorry, please say that again...")
                textto_speech("Sorry, please say that again...")
                break

    except KeyboardInterrupt:
        print("\n\nCancelling Tasks...\n")

    except UnboundLocalError:
        print('\n Done! \n')
