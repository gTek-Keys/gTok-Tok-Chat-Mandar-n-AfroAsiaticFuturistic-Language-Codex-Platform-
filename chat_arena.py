import streamlit as st
from flow_manager import FlowManager
import random

# Load persona
if "flow" not in st.session_state:
    st.error("Please create a persona in app.py first.")
    st.stop()

persona = st.session_state.flow.get_blueprint()

st.set_page_config(page_title="Codex Chat Arena", layout="wide")
st.title("🧪 Codex Chat Arena")
st.markdown(f"""
Welcome to the Arena of {persona.name}, your **{persona.role}**.

> *Tone*: {persona.interface_tone}  
> *Signature*: {persona.signature}
""")

# Simulated chat logic
user_message = st.text_input("💬 Speak to your Codex...", key="arena_input")

if "arena_log" not in st.session_state:
    st.session_state.arena_log = []

if user_message:
    tone = persona.interface_tone.lower()
    flavor = random.choice(["Certainly", "Of course", "As you wish", "Let me guide you", "Indeed"]) if tone == "formal" else random.choice(["Sure!", "Got it!", "Yep!", "Let’s go!", "Alright!"])
    reply = f"{flavor} {persona.signature} responds: 'I hear you say, \"{user_message}\" — what would you like to do next?'"
    st.session_state.arena_log.append(("user", user_message))
    st.session_state.arena_log.append(("codex", reply))

for role, msg in reversed(st.session_state.arena_log):
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

