import streamlit as st
import json
from flow_manager import FlowManager
from tts_module import speak
from export_utils import generate_pdf, generate_deck_markdown
from manifest_utils import generate_manifest

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

# --- Initialize Ritual Engine ---
if "flow" not in st.session_state:
    st.session_state.flow = FlowManager()

# --- Load Archetype Templates ---
st.sidebar.markdown("### 🧬 Load Archetype Template")
if st.sidebar.button("Load Template Options"):
    with open("archetypes.json") as f:
        options = json.load(f)
    selected = st.sidebar.selectbox("Choose Archetype", list(options.keys()))
    if st.sidebar.button("Apply Preset"):
        preset = options[selected]
        st.session_state.flow.blueprint = st.session_state.flow.blueprint.copy(update=preset)
        st.rerun()

# --- Header + Intro ---
st.title("🧠 gTok Tok Codex Builder")
st.markdown("""
<div style='padding: 1em; background: rgba(255,255,255,0.05); border-radius: 12px;'>
    <h2 style='color:#ff6de3;'>✨ Welcome to the Codex Builder Ritual ✨</h2>
    <p>Invoke archetypes. Encode intention. Generate wisdom from form and frequency.</p>
</div>
""", unsafe_allow_html=True)

# --- Ritual Phase Tracker ---
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

# --- Ritual Dialogue Input ---
user_input = st.text_input("💬 Speak to the ritual...", key="user_input")
if user_input:
    response = st.session_state.flow.process(user_input)
    st.chat_message("assistant").write(response)
    try:
        speak(response)
    except Exception:
        pass

# --- Persona Blueprint Access ---
blueprint = st.session_state.flow.get_blueprint()

# --- Export Section ---
st.markdown("---")
st.subheader("📦 Export Persona")

st.download_button(
    "📄 Download Persona JSON",
    json.dumps(blueprint.model_dump(), indent=2),
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

# --- Footer ---
st.markdown("""<hr><div style='text-align:center; opacity: 0.6'>
Crafted by <a href='https://github.com/gTek-Keys' target='_blank'>gTek-Keys</a> • 🛠️ Ritualizing AI Creation
</div>""", unsafe_allow_html=True)
