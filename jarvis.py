import streamlit as st
import webbrowser
import datetime
import subprocess

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

st.set_page_config(page_title="JARVIS Assistant", page_icon="🤖")
st.title("🧠 JARVIS - Your Python Assistant")
st.markdown(f"👋 {greet}, **{user_name}**! Type your command below:")

# Text input from user
command = st.text_input("🎤 Enter your command:")

if st.button("Run") and command:
    response = ""

    if 'exit' in command:
        response = f"Goodbye {user_name}, see you soon! 👋"
    
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
        response = "📺 Opening YouTube"

    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        response = "🔍 Opening Google"

    elif 'open whatsapp' in command:
        webbrowser.open("https://web.whatsapp.com")
        response = "💬 Opening WhatsApp Web"

    elif 'open github' in command:
        webbrowser.open("https://github.com")
        response = "🐙 Opening GitHub"

    elif 'play music' in command or 'open spotify' in command:
        webbrowser.open("https://open.spotify.com/")
        response = "🎵 Opening Spotify Web Player"

    elif 'time' in command or 'what is the time' in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        response = f"⏰ The time is {time_now}"

    elif 'open notepad' in command:
        try:
            subprocess.Popen(["notepad.exe"])
            response = "📝 Opening Notepad"
        except:
            response = "⚠️ Notepad is not supported on this platform."

    else:
        response = "❓ Sorry, I didn't understand that command."

    st.success(response)
