"""
Developer: @skywalkerSam
Purpose: To create a intro for Cortana AI
Date: 12022.06.15.16:26:00

"""

from pyfiglet import figlet_format
import datetime as dt


def introduction():
    text = figlet_format("Cortana  AI", "doom")
    print(text)
    return text


def greeting(user="User"):
    dt.datetime.now()
    timein_hour = int(dt.datetime.now().hour)

    if 0 < timein_hour < 12:
        print(f"Hello {user}, Good Morning :)\n")
    elif 12 < timein_hour < 16:
        print(f"Hello {user}, Good Afternoon :)\n")
    else:
        print(f"Hello {user}, Good Evening :)\n")


if __name__ == '__main__':
    introduction()
    greeting("Sam")
