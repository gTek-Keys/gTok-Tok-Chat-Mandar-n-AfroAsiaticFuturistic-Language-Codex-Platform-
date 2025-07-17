import streamlit as st
from flow_manager import FlowManager
from tts_module import speak
from export_utils import generate_pdf, generate_deck_markdown
from manifest_utils import generate_manifest
import json

# Setup layout and theming
st.set_page_config(page_title="GPT Codex Builder", layout="wide")
st.markdown("""
<style>
body {
    background: radial-gradient(circle at center, #0d0d0d, #000000);
    font-family: 'Orbitron', sans-serif;
    color: #e0e6f8;
}
h1, h2, h3 {
    color: #d0afff;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.stButton>button {
    background-color: #2b133f;
    color: #f0eaff;
    border-radius: 12px;
    padding: 0.6em 1.2em;
    border: 1px solid #8830ff;
}
.stButton>button:hover {
    background-color: #49197c;
    border-color: #ff6de3;
}
.stTextInput>div>div>input {
    background-color: #1b1b1f;
    color: #ffffff;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 10px;
}
.stDownloadButton>button {
    border-radius: 8px;
    background-color: #102020;
    border: 1px solid #88ffff;
    color: #b4f0f4;
}
</style>
""", unsafe_allow_html=True)

# Initialize state
if "flow" not in st.session_state:
    st.session_state.flow = FlowManager()

# Archetype loader
st.sidebar.markdown("### 🧬 Load Archetype Template")
if st.sidebar.button("Load Template Options"):
    with open("archetypes.json") as f:
        options = json.load(f)
    selected = st.sidebar.selectbox("Choose Archetype", list(options.keys()))
    if st.sidebar.button("Apply Preset"):
        preset = options[selected]
        st.session_state.flow.blueprint = st.session_state.flow.blueprint.copy(update=preset)
        st.rerun()

# Title and intro
st.title("🧠 GPT Codex Builder")
st.markdown("""
<div style='padding: 1.5em; background: rgba(255, 255, 255, 0.05); border-radius: 12px;'>
    <h2 style='color:#ff6de3;'>✨ Welcome to the Codex Builder Ritual ✨</h2>
    <p style='font-size: 1.1em;'>Step through the ceremonial gates and give form to your AI guide.
    Invoke archetypes, encode intentions, and bestow your persona with essence and power.</p>
</div>
""", unsafe_allow_html=True)

# Ritual phase tracker
phase = st.session_state.flow.state
phase_icons = {
    "awakening": "🔮 Awakening",
    "embodiment": "🧿 Embodiment",
    "instruction": "📜 Instruction",
    "voice": "🎤 Voice",
    "understanding": "🧠 Understanding",
    "powers": "✨ Powers",
    "essence": "🌟 Essence",
    "complete": "✅ Complete"
}
st.subheader(f"🌀 Current Phase: {phase_icons.get(phase, 'Unknown')}")
st.progress(list(phase_icons.keys()).index(phase) / (len(phase_icons) - 1))

# Input field
user_input = st.text_input("💬 Speak to the ritual...", key="user_input")
if user_input:
    response = st.session_state.flow.process(user_input)
    st.chat_message("assistant").write(response)
    try:
        speak(response)
    except:
        pass

# Persona access
blueprint = st.session_state.flow.get_blueprint()

# Export tools
st.markdown("---")
st.subheader("📦 Export Persona")

st.download_button(
    "📄 Download Persona JSON",
    json.dumps(blueprint.dict(), indent=2),
    file_name="persona_blueprint.json"
)

if st.button("🧾 Generate Persona Sheet (HTML)"):
    html_path = generate_pdf(blueprint)
    with open(html_path, "rb") as f:
        st.download_button("Download Sheet", f, file_name="persona_guide.html")

if st.button("📊 Export Slide Deck"):
    markdown_text = generate_deck_markdown(blueprint)
    st.download_button("Download Deck", markdown_text, file_name="persona_deck.md")

if st.button("📜 Generate Codex Manifest"):
    manifest_text = generate_manifest(blueprint)
    st.download_button("Download Manifest", manifest_text, file_name="persona_manifest.txt")

# Footer + GitHub badge
st.markdown("""<hr><div style='text-align:center; opacity: 0.6'>
Crafted by <a href='https://github.com/gTek-Keys' target='_blank'>gTek-Keys</a> • 🛠️ Ritualizing AI Creation
</div>""", unsafe_allow_html=True)

st.sidebar.markdown(
    "[![GitHub Repo](https://img.shields.io/badge/View%20Code-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gTek-Keys/New_Chat_App)",
    unsafe_allow_html=True
)

