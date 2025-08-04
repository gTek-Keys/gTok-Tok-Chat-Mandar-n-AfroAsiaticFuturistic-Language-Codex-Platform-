import streamlit as st
import json
import os
from flow_manager import FlowManager
from export_utils import generate_pdf, generate_deck_markdown
from manifest_utils import generate_manifest

# Optional: safely import local-only speak module
try:
    from tts_module import speak
    tts_available = True
except:
    tts_available = False

# --- Layout and Styling ---
st.set_page_config(page_title="gTok Tok Chat Mandar:)n", layout="wide")

st.markdown("""
<style>
body {
    background: #0e0e1f;
    color: #e0e6f8;
    font-family: 'Orbitron', sans-serif;
}
h1, h2, h3 {
    color: #ff6de3;
    text-transform: uppercase;
}
.stButton>button {
    background-color: #421e58;
    border: 1px solid #bb66ff;
    color: white;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# --- Initialize State ---
if "flow" not in st.session_state:
    st.session_state.flow = FlowManager()

# --- Sidebar: Load Archetype Presets ---
st.sidebar.header("🧬 Load Archetype Template")
if st.sidebar.button("Load Template Options"):
    with open("archetypes.json") as f:
        options = json.load(f)
    selected = st.sidebar.selectbox("Choose Archetype", list(options.keys()))
    if st.sidebar.button("Apply Preset"):
        preset = options[selected]
        st.session_state.flow.blueprint = st.session_state.flow.blueprint.copy(update=preset)
        st.rerun()

# --- Header + Welcome ---
st.title("🧠 gTok Tok Codex Builder")
st.markdown("""
<div style='padding: 1em; background: rgba(255,255,255,0.05); border-radius: 12px;'>
    <h2 style='color:#ff6de3;'>✨ Welcome to the Codex Builder Ritual ✨</h2>
    <p>Invoke archetypes. Encode intention. Generate wisdom from form and frequency.</p>
</div>
""", unsafe_allow_html=True)

# --- Ritual Phases ---
phase = st.session_state.flow.state
phases = {
    "awakening": "🔮 Awakening",
    "embodiment": "🧿 Embodiment",
    "instruction": "📜 Instruction",
    "voice": "🎤 Voice",
    "understanding": "🧠 Understanding",
    "powers": "✨ Powers",
    "essence": "🌟 Essence",
    "complete": "✅ Complete"
}
st.subheader(f"🌀 Current Phase: {phases.get(phase, 'Unknown')}")
st.progress(list(phases.keys()).index(phase) / (len(phases) - 1))

# --- Input Field for Ritual Dialogue ---
user_input = st.text_input("💬 Speak to the ritual...", key="user_input")
if user_input:
    response = st.session_state.flow.process(user_input)
    st.chat_message("assistant").write(response)
    # Only run TTS locally
    if tts_available and os.getenv("STREAMLIT_ENV") != "cloud":
        try:
            speak(response)
        except Exception:
            st.warning("TTS failed or unavailable in cloud environment.")

# --- Blueprint Data Export ---
blueprint = st.session_state.flow.get_blueprint()

st.markdown("---")
st.subheader("📦 Export Persona")

# JSON Export
st.download_button(
    label="📄 Download Persona JSON",
    data=json.dumps(blueprint.model_dump(), indent=2),
    file_name="persona_blueprint.json",
    mime="application/json"
)

# HTML Export
if st.button("🧾 Generate Persona Sheet (HTML)"):
    html_path = generate_pdf(blueprint)
    with open(html_path, "rb") as f:
        st.download_button("Download Sheet", f, file_name="persona_guide.html")

# Markdown Deck Export
if st.button("📊 Export Slide Deck"):
    markdown_text = generate_deck_markdown(blueprint)
    st.download_button("Download Deck", markdown_text, file_name="persona_deck.md")

# Manifest Export
if st.button("📜 Generate Codex Manifest"):
    manifest_text = generate_manifest(blueprint)
    st.download_button("Download Manifest", manifest_text, file_name="persona_manifest.txt")

# --- Footer ---
st.markdown("""<hr><div style='text-align:center; opacity: 0.6'>
Crafted by <a href='https://github.com/gTek-Keys' target='_blank'>gTek-Keys</a> • 🛠️ Ritualizing AI Sovereignty
</div>""", unsafe_allow_html=True)
