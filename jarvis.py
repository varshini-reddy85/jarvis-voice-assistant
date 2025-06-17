import asyncio
import edge_tts
import playsound
import os
import webbrowser
import datetime
import subprocess

# Speak function using edge-tts (male voice)
def speak(text):
    async def speak_async():
        communicate = edge_tts.Communicate(text=text, voice="en-GB-RyanNeural")
        await communicate.save("voice.mp3")
        playsound.playsound("voice.mp3")
        os.remove("voice.mp3")
    asyncio.run(speak_async())

# Default Name
user_name = "Varshini"

# Greet based on time
hour = datetime.datetime.now().hour
if 0 <= hour < 12:
    greet = "Good morning"
elif 12 <= hour < 18:
    greet = "Good afternoon"
else:
    greet = "Good evening"

# Speak welcome message
speak(f"{greet}, {user_name}! I am JARVIS, your assistant. How can I help you today?")
print(f"{greet}, {user_name}! I am JARVIS, your assistant.")

# Command loop
while True:
    command = input(f"\n🎤 {user_name}, enter your command (or type 'exit'): ").lower()

    if 'exit' in command:
        speak(f"Goodbye {user_name}, see you soon!")
        print("🔚 Exiting JARVIS.")
        break

    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'open whatsapp' in command:
        speak("Opening WhatsApp Web")
        webbrowser.open("https://web.whatsapp.com")

    elif 'open github' in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif 'play music' in command or 'open spotify' in command:
        speak("Opening Spotify Web Player")
        webbrowser.open("https://open.spotify.com/")

    elif 'time' in command or 'what is the time' in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time_now}")
        print(f"The time is {time_now}")

    elif 'open notepad' in command:
        speak("Opening Notepad")
        subprocess.Popen(["notepad.exe"])

    else:
        speak("Sorry, I didn't understand that command.")
