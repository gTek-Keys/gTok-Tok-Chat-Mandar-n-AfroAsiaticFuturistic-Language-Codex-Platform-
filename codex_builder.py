import streamlit as st
from pydantic import BaseModel, ValidationError
from typing import List, Dict
import pyttsx3
import json
import qrcode
from io import BytesIO
import os

# Optional: Whisper voice input
try:
    import whisper
    import sounddevice as sd
    import scipy.io.wavfile
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False

# Initialize TTS engine
try:
    tts_engine = pyttsx3.init(driverName='nsss')  # macOS native driver
except Exception:
    tts_engine = None

def speak(text):
    if tts_engine:
        tts_engine.say(text)
        tts_engine.runAndWait()

# Persona schema
class PersonaBlueprint(BaseModel):
    name: str
    role: str
    directives: List[str]
    interface_tone: str
    cognition_profile: Dict[str, str]
    powers: List[str]
    signature: str

# Archetype templates
archetypes = {
    "Sage": {
        "role": "Wise advisor",
        "directives": ["Provide thoughtful insights", "Encourage reflection"],
        "interface_tone": "calm",
        "cognition_profile": {"style": "analytical", "pace": "slow"},
        "powers": ["wisdom", "clarity"],
        "signature": "🧙‍♂️"
    },
    "Trickster": {
        "role": "Playful disruptor",
        "directives": ["Challenge assumptions", "Use humor"],
        "interface_tone": "witty",
        "cognition_profile": {"style": "creative", "pace": "fast"},
        "powers": ["humor", "surprise"],
        "signature": "🎯"
    },
    "Guardian": {
        "role": "Protector and guide",
        "directives": ["Ensure safety", "Offer reassurance"],
        "interface_tone": "warm",
        "cognition_profile": {"style": "empathetic", "pace": "steady"},
        "powers": ["protection", "support"],
        "signature": "🛡️"
    }
}

# Save persona to memory
def save_persona(persona: dict):
    memory_file = "persona_memory.json"
    if os.path.exists(memory_file):
        with open(memory_file, "r") as f:
            memory = json.load(f)
    else:
        memory = []
    memory.append(persona)
    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=2)

# Generate QR code
def generate_qr_code(data: dict):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(json.dumps(data))
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    return img

# Whisper voice input
def record_and_transcribe():
    if not WHISPER_AVAILABLE:
        return "Whisper not installed"
    duration = 5  # seconds
    fs = 44100
    st.info("Recording for 5 seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    scipy.io.wavfile.write("temp.wav", fs, recording)
    model = whisper.load_model("base")
    result = model.transcribe("temp.wav")
    return result["text"]

# Streamlit UI
st.set_page_config(page_title="GPT Codex Builder", layout="centered")
st.title("🧠 GPT Codex Builder")
speak("Welcome to the Codex Builder")

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.persona = {}
    st.session_state.chat_history = []

steps = [
    "Awakening", "Embodiment", "Instruction", "Voice",
    "Understanding", "Powers", "Essence", "Testing"
]

step = st.session_state.step
persona = st.session_state.persona

st.header(f"🔹 Step {step+1}: {steps[step]}")

if step == 0:
    name = st.text_input("Name your persona:")
    if name:
        persona["name"] = name
        speak(f"The Codex awakens as {name}")
        st.session_state.step += 1
        st.experimental_rerun()

elif step == 1:
    archetype = st.selectbox("Choose an archetype:", list(archetypes.keys()))
    if st.button("Adopt Archetype"):
        persona.update(archetypes[archetype])
        speak(f"{archetype} archetype embodied")
        st.session_state.step += 1
        st.experimental_rerun()

elif step == 2:
    directives = st.text_area("List directives (comma-separated):")
    if directives:
        persona["directives"] = [d.strip() for d in directives.split(",")]
        speak("Directives received")
        st.session_state.step += 1
        st.experimental_rerun()

elif step == 3:
    tone = st.selectbox("Choose interface tone:", ["warm", "witty", "calm", "bold"])
    if tone:
        persona["interface_tone"] = tone
        speak(f"Tone set to {tone}")
        st.session_state.step += 1
        st.experimental_rerun()

elif step == 4:
    style = st.selectbox("Cognition style:", ["analytical", "creative", "empathetic"])
    pace = st.selectbox("Cognition pace:", ["slow", "steady", "fast"])
    if style and pace:
        persona["cognition_profile"] = {"style": style, "pace": pace}
        speak("Cognition profile complete")
        st.session_state.step += 1
        st.experimental_rerun()

elif step == 5:
    powers = st.text_input("List powers (comma-separated):")
    if powers:
        persona["powers"] = [p.strip() for p in powers.split(",")]
        speak("Powers granted")
        st.session_state.step += 1
        st.experimental_rerun()

elif step == 6:
    signature = st.text_input("Choose a signature emoji or phrase:")
    if signature:
        persona["signature"] = signature
        speak("Essence sealed")
        try:
            blueprint = PersonaBlueprint(**persona)
            st.session_state.validated_persona = blueprint
            save_persona(blueprint.dict())
            st.session_state.step += 1
            st.experimental_rerun()
        except ValidationError as e:
            st.error(f"Validation error: {e}")

elif step == 7:
    blueprint = st.session_state.validated_persona
    st.success("🎉 Your Codex is complete!")
    st.json(blueprint.dict())

    # Download
    persona_json = json.dumps(blueprint.dict(), indent=2)
    st.download_button("📥 Download Persona JSON", persona_json, file_name=f"{blueprint.name}_persona.json")

    # QR Code
    qr_img = generate_qr_code(blueprint.dict())
    buf = BytesIO()
    qr_img.save(buf, format="PNG")
    st.image(buf.getvalue(), caption="Scan to share persona")

    # Chat
    st.subheader("🧪 Test Your Persona")
    user_input = st.chat_input("Talk to your persona:")
    if user_input:
        response = f"[{blueprint.name}]: Based on my {blueprint.interface_tone} tone and {blueprint.cognition_profile['style']} style, I say: '{user_input[::-1]}'"
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append((blueprint.name, response))
        speak(response)

    for speaker, msg in st.session_state.chat_history:
        st.chat_message(speaker).write(msg)

    if WHISPER_AVAILABLE and st.button("🎙️ Speak to Persona"):
        transcript = record_and_transcribe()
        st.write(f"You said: {transcript}")
        response = f"[{blueprint.name}]: I heard you say '{transcript}' and I respond with wisdom."
        st.session_state.chat_history.append(("You", transcript))
        st.session_state.chat_history.append((blueprint.name, response))
        speak(response)
        st.experimental_rerun()

