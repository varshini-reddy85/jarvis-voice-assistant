import streamlit as st
from datetime import datetime, timedelta

# 🔁 Convert UTC to IST
utc_now = datetime.utcnow()
ist_now = utc_now + timedelta(hours=5, minutes=30)
hour = ist_now.hour

# 👋 Greet based on IST time
if 0 <= hour < 12:
    greet = "Good morning"
elif 12 <= hour < 18:
    greet = "Good afternoon"
else:
    greet = "Good evening"

# 🧠 Default Name
user_name = "Varshini"

# 🎨 Streamlit UI setup
st.set_page_config(page_title="JARVIS - Assistant", page_icon="🧠")
st.title("🧠 JARVIS - Your Python Assistant")
st.markdown(f"👋 {greet}, **{user_name}**! Type your command below:")

# 🔑 Input box
command = st.text_input("💬 Enter your command:")

# 🟩 Command handler
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

    elif 'chrome' in command:
        st.success("🌐 Opening Chrome homepage...")
        st.markdown("[Click here to open Chrome](https://www.google.com/chrome/)", unsafe_allow_html=True)

    elif 'time' in command:
        current_time = ist_now.strftime("%I:%M %p")
        st.info(f"🕒 The time in IST is: **{current_time}**")

    else:
        st.warning("🤖 Sorry, I didn't understand that command.")
