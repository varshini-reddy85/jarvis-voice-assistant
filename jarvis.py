import streamlit as st
import datetime

# Default Name
user_name = "Varshini"

# Greet based on time
hour = datetime.datetime.now().hour
if 0 <= hour < 12:
    greet = "Good morning"
elif 12 <= hour < 15:
    greet = "Good afternoon"
else:
    greet = "Good evening"

# UI
st.set_page_config(page_title="JARVIS - Assistant", page_icon="🧠")
st.title("🧠 JARVIS - Your Python Assistant")
st.markdown(f"👋 {greet}, **{user_name}**! Type your command below:")

# Input box
command = st.text_input("🔑 Enter your command:")

if st.button("Run") and command:
    command = command.lower()

    if 'youtube' in command:
        st.success("✅ Opening YouTube...")
        st.markdown("[Click here to open YouTube](https://www.youtube.com)", unsafe_allow_html=True)

    elif 'google' in command:
        st.success("✅ Opening Google...")
        st.markdown("[Click here to open Google](https://www.google.com)", unsafe_allow_html=True)

    elif 'whatsapp' in command:
        st.success("✅ Opening WhatsApp Web...")
        st.markdown("[Click here to open WhatsApp](https://web.whatsapp.com)", unsafe_allow_html=True)

    elif 'github' in command:
        st.success("✅ Opening GitHub...")
        st.markdown("[Click here to open GitHub](https://github.com)", unsafe_allow_html=True)

    elif 'spotify' in command or 'music' in command:
        st.success("🎵 Opening Spotify Web Player...")
        st.markdown("[Click here to open Spotify](https://open.spotify.com)", unsafe_allow_html=True)

    elif 'time' in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        st.info(f"🕒 The time is: **{time_now}**")

    else:
        st.warning("🤖 Sorry, I didn't understand that command.")
