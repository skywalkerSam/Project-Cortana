# Project-CortanaAI, Level 0, Step - 6 (main program for CortanaAI_v0)


"""
Developer: Sam Skywalker
Purpose: Initial Blueprint for Project-CortanaAI 
Date: 12022.04.25.16:53
"""

import pyttsx3
import speech_recognition as source1
import datetime
import os
import webbrowser
from pyfiglet import figlet_format

# User Definition
formal_name = "Sam Skywalker"  # What you'd like to be called?
username = "Starboy"  # Username of yours in system.
ai_name = "Cortana"  # What you'd like to call your AI assistant?


def introduction():
    """
    Introduction of the Base AI system...
    """
    out = figlet_format("Cortana  AI", "doom")
    print(out)
    return out


# voice_engine
voice_engine = pyttsx3.init("sapi5")
voice_engine_voice = voice_engine.getProperty("voices")
# Choose between voices: print(voice_engine_voice[2].id)
voice_engine.setProperty("voice", voice_engine_voice[0].id)
voice_engine_rate = voice_engine.getProperty("rate")
voice_engine.setProperty("rate", 200)


def speak(audio):
    """
    It's a speak function() that, takes audio as its parameter...
    """
    voice_engine.say(audio)
    voice_engine.runAndWait()


def greeting():
    """
    It's about how the AI will approach you initially...
    """
    datetime.datetime.now()
    time_in_hour = int(datetime.datetime.now().hour)

    if 0 < time_in_hour < 12:
        print(f"Hello {formal_name}, Good Morning :)\n")
    elif 12 < time_in_hour < 16:
        print(f"Hello {formal_name}, Good Afternoon :)\n")
    else:
        print(f"Hello {formal_name}, Good Evening :)\n")

    print("I'm here... \n")
    speak("I am here...")


def process_command():
    """
    It processes the voice data from microphone & converts into strings...

    """
    command = source1.Recognizer()
    with source1.Microphone() as source:
        print("\n Listening...")
        command.pause_threshold = 1.5
        audio = command.listen(source)
    try:
        print("Recognizing...\n")
        request = command.recognize_google(audio, language="en-us")
        # print(f"You said; {request}\n")
    except Exception:
        return "Something's not right, Please try again! \n"
    return request


attempt = 0
if __name__ == "__main__":
    introduction()
    greeting()
    try:
        while attempt <= 10:
            user_request = process_command().lower()
            attempt = attempt + 1

            # Personal AI Introduction
            if "who are you" in user_request:
                print(
                    f"Hello, I'm {ai_name} & I'm here to help you... \n")
                speak(f"Hello, I am {ai_name}, and I am here to help you")
                continue

            elif "tell me about yourself" in user_request:
                print(
                    f"Hey, I'm {ai_name} & I'm here to help you... \n")
                speak(f"Hey, I am {ai_name}, and I am here to help you")
                continue

            elif "hello cortana" in user_request:
                print(
                    f"Hello {formal_name}. How may I help you? \n")
                speak(f"Hello {formal_name}. How may I help you?")
                continue

            # User Feedback
            elif "you need to improve" in user_request:
                print("Sorry for the inconvenience :( \n")
                speak("Sure")
                break

            # date
            elif "the date" in user_request:
                current_date = str(datetime.date.today())
                print(f"Today is; {current_date} \n")
                speak(f"Today is, {current_date}")
                continue

            # time
            elif "the time" in user_request:
                current_time = datetime.datetime.now().strftime(" %H:%M:%S ")
                print(f"The time is; {current_time} \n")
                speak(f"The time is; {current_time}")
                continue

            # wishing
            elif "good morning" in user_request:
                print(f"Good morning {formal_name}, have a nice day :) \n")
                speak(f"Good morning {formal_name}, have a nice day")
                continue

            elif "good afternoon" in user_request:
                print(
                    f"Good afternoon {formal_name}, hope you doing good :) \n")
                speak(f"Good afternoon {formal_name}, hope you doing good")
                continue

            elif "good evening" in user_request:
                print(
                    f"Good evening {formal_name}, It's time to get refreshed :) \n")
                speak(
                    f"Good evening {formal_name}, It's time to get refreshed")
                continue

            elif "good night" in user_request:
                print(f"Good Night {formal_name}, Have a nice dream :) \n")
                speak(f"Good Night {formal_name}, Have a nice dream")
                continue

            # Web Commands

            # google.com
            elif 'open google.com' in user_request:
                webbrowser.open('https://www.google.com/')
                print('Opening Google.com...')
                speak('Opening Google.com...')
                exit()

            # duckduckgo.com
            elif "open duckduckgo" in user_request:
                webbrowser.open("https://duckduckgo.com/")
                print("Opening DuckDuckGo.com...")
                speak("Opening DuckDuckGo.com...")
                exit()

            # wikipedia.org
            elif "open wikipedia" in user_request:
                webbrowser.open("https://www.wikipedia.org/")
                print("Opening Wikipedia.org...")
                speak("Opening Wikipedia...")
                exit()

            # gmail.com
            elif "open gmail" in user_request:
                webbrowser.open("https://www.gmail.com/")
                print("Opening Google Mail...")
                speak("Opening Google Mail...")
                exit()

                # gmail.com
            elif "open google mail" in user_request:
                webbrowser.open("https://www.gmail.com/")
                print("Opening Google Mail...")
                speak("Opening Google Mail...")
                exit()

            # protonmail.com
            elif "open protonmail" in user_request:
                webbrowser.open("https://protonmail.com/")
                print("Opening ProtonMail.com...")
                speak("Opening ProtonMail.com...")
                exit()

            # blogger.com
            elif "open blogger.com" in user_request:
                webbrowser.open("https://www.blogger.com/")
                print("Opening Blogger.com...")
                speak("Opening Blogger.com...")
                exit()

            # youtube.com
            elif 'open youtube' in user_request:
                webbrowser.open('https://www.youtube.com/')
                print('Opening Youtube...')
                speak('Opening Youtube...')
                exit()

            # google drive
            elif "open google drive" in user_request:
                webbrowser.open("https://drive.google.com/")
                print("Opening Google Drive...")
                speak("Opening Google Drive...")
                exit()

            # google cloud shell
            elif "open cloud terminal" in user_request:
                webbrowser.open("https://cloud.google.com/shell/")
                print("Opening Google Cloud Shell...")
                speak("Opening Google Cloud Shell...")
                exit()

            # khanacademy.org
            elif "open khan academy" in user_request:
                webbrowser.open("https://www.khanacademy.org/")
                print("Opening KhanAcademy.org...")
                speak("Opening KhanAcademy.org...")
                exit()

            # udemy.com
            elif 'open udemy' in user_request:
                webbrowser.open('https://www.udemy.com/')
                print('Opening Udemy.com...')
                speak('Opening Udemy...')
                exit()

            # replit.com
            elif "open code browser" in user_request:
                webbrowser.open("https://replit.com/")
                print("Opening Replit.com...")
                speak("Opening Replit.com...")
                exit()

            # stackoverflow
            elif "open stack overflow" in user_request:
                webbrowser.open("https://stackoverflow.com/")
                print("Opening StackOverFlow.com...")
                speak("Opening StackOverFlow...")
                exit()

            # stackoverflow.com
            elif "open stackoverflow" in user_request:
                webbrowser.open("https://stackoverflow.com/")
                print("Opening StackOverFlow.com...")
                speak("Opening StackOverFlow.com...")
                exit()

            # github.com
            elif 'open github' in user_request:
                webbrowser.open('https://github.com/')
                print('Opening Github.com...')
                speak('Opening Github...')
                exit()

            # gitlab.com
            elif "open git lab" in user_request:
                webbrowser.open("https://gitlab.com/")
                print("Opening GitLab.com...")
                speak("Opening GitLab...")
                exit()

            # hackthebox.eu
            elif "open hack the box" in user_request:
                webbrowser.open("https://www.hackthebox.eu/")
                print("Opening HackTheBox.eu...")
                speak("Opening HackTheBox...")
                exit()

            # hackerone.com
            elif "open hacker 1" in user_request:
                webbrowser.open("https://www.hackerone.com/")
                print("Opening HackerOne.com...")
                speak("Opening HackerOne.com...")
                exit()

            # docker hub
            elif "open docker hub" in user_request:
                webbrowser.open("https://hub.docker.com/")
                print("Opening Docker Hub...")
                speak("Opening Docker Hub...")
                exit()

            # apple.com
            elif "open apple.com" in user_request:
                webbrowser.open("https://www.apple.com/")
                print("Opening Apple.com...")
                speak("Opening Apple.com...")
                exit()

            # amazon.in
            elif 'open amazon.in' in user_request:
                webbrowser.open('https://www.amazon.in/')
                print('Opening Amazon.in...')
                speak('Opening Amazon.in...')
                exit()

            # amazon.com
            elif 'open amazon.com' in user_request:
                webbrowser.open('https://www.amazon.com/')
                print('Opening Amazon.com...')
                speak('Opening Amazon.com...')
                exit()

            # flipkart.com
            elif "open flipkart" in user_request:
                webbrowser.open("https://www.flipkart.com/")
                print("Opening Flipkart.com...")
                speak("Opening Flipkart.com...")
                exit()

            # twitter.com
            elif "open twitter" in user_request:
                webbrowser.open("https://twitter.com/")
                print("Opening Twitter.com...")
                speak("Opening Twitter.com...")
                exit()

            # discord.com
            elif "open discord" in user_request:
                webbrowser.open("https://discord.com/")
                print("Opening Discord.com...")
                speak("Opening Discord.com...")
                exit()

            # reddit.com
            elif "open reddit" in user_request:
                webbrowser.open("https://www.reddit.com/")
                print("Opening Reddit.com")
                speak("Opening Reddit.com")
                exit()

            # spacex.com
            elif "open space x.com" in user_request:
                webbrowser.open("https://www.spacex.com/")
                print("Opening SpaceX.com...")
                speak("Opening SpaceX.com...")
                exit()

            # unrealengine.com
            elif "open unreal engine dotkom" in user_request:
                webbrowser.open("https://www.unrealengine.com/")
                print("Opening Unreal Engine.com...")
                speak("Opening Unreal Engine.com...")
                exit()

            elif "open unreal engine dotcom" in user_request:
                webbrowser.open("https://www.unrealengine.com/")
                print("Opening Unreal Engine.com...")
                speak("Opening Unreal Engine.com...")
                exit()

            # learn.unrealengine.com
            elif "open unreal engine learning" in user_request:
                webbrowser.open("https://learn.unrealengine.com/")
                print("Opening Learn.UnrealEngine.com...")
                speak("Opening Learn.UnrealEngine.com...")
                exit()

            # dev.epicgames.com
            elif "open epic developer community" in user_request:
                webbrowser.open("https://dev.epicgames.com/community/")
                print("Opening Dev.EpicGames.com/community...")
                speak("Opening Dev.EpicGames.com/community...")
                exit()

            # metahuman.unrealengine.com
            elif "open metahuman creator" in user_request:
                webbrowser.open("https://metahuman.unrealengine.com/")
                print("Opening Metahuman Creator...")
                speak("Opening Metahuman Creator...")
                exit()

            elif "open m h c" in user_request:
                webbrowser.open("https://metahuman.unrealengine.com/")
                print("Opening Metahuman Creator...")
                speak("Opening Metahuman Creator...")
                exit()

            # open.spotify.com
            elif "open spotify on web" in user_request:
                webbrowser.open("https://open.spotify.com/")
                print("Opening Spotify on Web, Enjoy listening...")
                speak("Opening Spotify on Web, Enjoy listening...")
                exit()

            # open.spotify.com
            elif "open spotify on the web" in user_request:
                webbrowser.open("https://open.spotify.com/")
                print("Opening Spotify on Web, Enjoy listening...")
                speak("Opening Spotify on Web, Enjoy listening...")
                exit()

            # Operating System Commands

            # file explorer
            elif "open explorer" in user_request:
                os.system("explorer")
                print("Opening Explorer...")
                speak("Opening File Explorer...")
                exit()

            elif "open file explorer" in user_request:
                os.system("explorer")
                print("Opening File Explorer...")
                speak("Opening File Explorer...")
                exit()

            elif "open files" in user_request:
                os.system("explorer")
                print("Opening Files...")
                speak("Opening File Explorer...")
                exit()

            # bash shell
            elif "open bash shell" in user_request:
                print("Opening Bash Shell (Linux Terminal, WSL)...")
                speak("Opening Bash Shell...")
                os.system("bash")
                exit()

            # bash terminal
            elif "open bash terminal" in user_request:
                print("Opening Bash Shell (Linux Terminal, WSL)...")
                speak("Opening Bash Shell...")
                os.system("bash")
                exit()

            # ubuntu
            elif "open ubuntu" in user_request:
                print("Opening Ubuntu (Linux Terminal, WSL/WSL2)...")
                speak("Opening Ubuntu...")
                os.system("ubuntu")
                exit()

            # python
            elif "open python" in user_request:
                print("Opening Python Shell...")
                speak("Opening Python Shell...")
                os.system("python")
                exit()

            # vscode
            elif 'open code' in user_request:
                os.system("code")
                print('Opening Visual Studio Code...')
                speak('Opening Visual Studio Code...')
                exit()

            elif 'open code editor' in user_request:
                os.system("code")
                print('Opening Visual Studio Code...')
                speak('Opening Visual Studio Code...')
                exit()

            elif 'open vs code' in user_request:
                vscodePath = f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(vscodePath)
                print('Opening Visual Studio Code...')
                speak('Opening Visual Studio Code...')
                exit()

            # atom
            elif 'open atom code editor' in user_request:
                os.system("atom")
                print('Opening Atom Code Editor...')
                speak('Opening Atom Code Editor...')
                exit()

            elif 'open atom' in user_request:
                os.system("atom")
                print('Opening Atom Code Editor...')
                speak('Opening Atom Code Editor...')
                exit()

            # pycharm
            elif "open pycharm" in user_request:
                print('Opening Pycharm IDE...')
                speak('Opening Pycharm IDE...')
                os.system("pycharm")
                speak("Welcome Back, I am here...")

            # pycharm
            elif "open pycharm ide" in user_request:
                print('Opening Pycharm IDE...')
                speak('Opening Pycharm IDE...')
                os.system("pycharm")
                speak("Welcome Back, I am here...")

            # # Anaconda Navigator
            # elif 'open anaconda navigator' in user_request:
            #     anaconda_navigator = "C:\\ProgramData\\Anaconda3\\pythonw.exe C:\\ProgramData\\Anaconda3\\cwp.py C:\\ProgramData\\Anaconda3 C:\\ProgramData\\Anaconda3\\pythonw.exe C:\\ProgramData\\Anaconda3\\Scripts\\anaconda-navigator-script.py"
            #     os.startfile(anaconda_navigator)
            #     print('Opening Anaconda Navigator...')
            #     speak('Opening Anaconda Navigator...')
            #     exit()

            # docker desktop
            elif "open docker desktop" in user_request:
                docker_desktop_path = "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"
                os.startfile(docker_desktop_path)
                print("Opening Docker Desktop...")
                speak("Opening Docker Desktop...")
                exit()

            # virtualbox
            elif "open virtualbox" in user_request:
                virtualbox_path = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
                os.startfile(virtualbox_path)
                print("Opening Virtualbox...")
                speak("Opening Virtualbox...")
                exit()

            # firefox
            elif 'open firefox' in user_request:
                firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                os.startfile(firefox_path)
                print('Opening Firefox Browser...')
                speak('Opening Firefox...')
                exit()

            # chrome
            elif "open chrome" in user_request:
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chrome_path)
                print("Opening Chrome Browser...")
                speak("Opening Chrome...")
                exit()

            # Microsoft Edge Browser
            elif "open microsoft browser" in user_request:
                microsoft_browser_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(microsoft_browser_path)
                print('Opening Microsoft Edge Browser...')
                speak("Opening Microsoft Edge...")
                exit()

            elif "open microsoft edge browser" in user_request:
                microsoft_browser_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(microsoft_browser_path)
                print('Opening Microsoft Edge Browser...')
                speak("Opening Microsoft Edge...")
                exit()

            elif "open microsoft edge" in user_request:
                microsoft_browser_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(microsoft_browser_path)
                print('Opening Microsoft Edge Browser...')
                speak("Opening Microsoft Edge...")
                exit()

            elif "open windows browser" in user_request:
                microsoft_browser_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(microsoft_browser_path)
                print('Opening Microsoft Edge Browser...')
                speak("Opening Microsoft Edge...")
                exit()

            # Epic Games Launcher
            elif "open epic games launcher" in user_request:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                exit()

            elif "open fortnite" in user_request:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                exit()

            elif "open fortnite game" in user_request:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                exit()

            elif "i wanna play fortnite" in user_request:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                exit()

            elif "i want to play fortnite" in user_request:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                exit()

            elif "i want to play fortnite game" in user_request:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                exit()

            elif "open unreal engine" in user_request:
                epic_games_launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
                os.startfile(epic_games_launcher)
                print("Opening Epic Games Launcher...")
                speak("Opening Epic Games Launcher...")
                exit()

            # Steam Play
            elif "open steam play" in user_request:
                steam_play = "C:\\Program Files (x86)\\Steam\\steam.exe"
                os.startfile(steam_play)
                print("Opening Steam Play...")
                speak("Opening Steam Play...")
                exit()

            elif "open steam" in user_request:
                steam_play = "C:\\Program Files (x86)\\Steam\\steam.exe"
                os.startfile(steam_play)
                print("Opening Steam Play...")
                speak("Opening Steam Play...")
                exit()

            elif "i wanna play halo infinite" in user_request:
                steam_play = "C:\\Program Files (x86)\\Steam\\steam.exe"
                os.startfile(steam_play)
                print("Opening Steam Play...")
                speak("Opening Steam Play...")
                exit()

            elif "i want to play halo infinite" in user_request:
                steam_play = "C:\\Program Files (x86)\\Steam\\steam.exe"
                os.startfile(steam_play)
                print("Opening Steam Play...")
                speak("Opening Steam Play...")
                exit()

            # control panel
            elif "open control panel" in user_request:
                os.system("%windir%\\System32\\Control.exe")
                print("Opening Control Panel...")
                speak("Opening Control Panel...")
                exit()

            # poweroff
            elif 'poweroff the system' in user_request:
                print('Shutting Down The System In Less Than A Minute...')
                speak('Shutting Down The System In Less Than A Minute...')
                os.system('shutdown -s')
                speak('Looking forward to help you!')
                exit()

            elif 'power of the system' in user_request:
                print('Shutting Down The System In Less Than A Minute...')
                speak('Shutting Down The System In Less Than A Minute...')
                os.system('shutdown -s')
                speak('Looking forward to help you...')
                exit()

            elif "stop poweroff" in user_request:
                print('Stopping System From Shutdown...')
                speak('Stopping System From Shutdown...')
                os.system('shutdown -a')
                speak("Welcome Back, I am here to help you... ")

            elif "stop power of" in user_request:
                print('Stopping System From Shutdown...')
                speak('Stopping System From Shutdown...')
                os.system('shutdown -a')
                speak("Welcome Back, I am here to help you... ")

            # shutdown
            elif 'shutdown the system' in user_request:
                print('Shutting Down The System In Less Than A Minute...')
                speak('Shutting Down The System In Less Than A Minute...')
                os.system('shutdown -s')
                speak('Looking forward to help you!')
                exit()

            elif 'shut down the system' in user_request:
                print('Shutting Down The System In Less Than A Minute...')
                speak('Shutting Down The System In Less Than A Minute...')
                os.system('shutdown -s')
                speak('Looking forward to help you...')
                exit()

            elif "stop shutdown" in user_request:
                print('Stopping System From Shutdown...')
                speak('Stopping System From Shutdown...')
                os.system('shutdown -a')
                speak("Welcome Back, I am here to help you... ")

            elif "stop shut down" in user_request:
                print('Stopping System From Shutdown...')
                speak('Stopping System From Shutdown...')
                os.system('shutdown -a')
                speak("Welcome Back, I am here to help you... ")

            # reboot
            elif 'reboot the system' in user_request:
                print('Rebooting The System In Less Than A Minute...')
                speak('Rebooting The System In Less Than A Minute...')
                os.system('shutdown /r')
                speak('Looking forward to help you...')
                exit()

            elif "stop reboot" in user_request:
                print('Stopping System From Reboot...')
                speak('Stopping System From Reboot...')
                os.system('shutdown -a')
                speak("Welcome Back, I am here to help you... ")

            # restart
            elif 'restart the system' in user_request:
                print('Restarting The System In Less Than A Minute...')
                speak('Restarting The System In Less Than A Minute...')
                os.system('shutdown /r')
                speak('Looking forward to help you...')
                exit()

            elif "stop restart" in user_request:
                print('Stopping System From Restart...')
                speak('Stopping System From Restart...')
                os.system('shutdown -a')
                speak("Welcome Back, I am here to help you... ")

            # PowerShell Terminal
            elif "open terminal" in user_request:
                print("Opening PowerShell Terminal...")
                speak("Opening PowerShell Terminal...")
                os.system("powershell")
                speak("Welcome Back, I am here...")

            elif "open windows terminal" in user_request:
                print("Opening PowerShell In Windows Terminal...")
                speak("Opening PowerShell In Windows Terminal...")
                os.system("powershell")
                speak("Welcome Back, I am here...")

            elif "open powershell" in user_request:
                print("Opening PowerShell Terminal...")
                speak("Opening PowerShell Terminal...")
                os.system("powershell")
                speak("Welcome Back, I am here...")

            # exit
            elif "quit" in user_request:
                print("Okay :) \n")
                speak("Okay")
                break

            elif "exit" in user_request:
                print("Okay :) \n")
                speak("Okay")
                break

            # ok
            elif "ok" in user_request:
                print("Alright ;) \n")
                speak("Alright")
                break

            # error-message
            else:
                print("Please Try Again! \n")
                speak("Say again")
                continue

    except KeyboardInterrupt:
        print("\n Operation cancelled by the user :( \n")
