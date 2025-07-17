from persona_blueprint import PersonaBlueprint

class FlowManager:
    def __init__(self):
        self.state = "awakening"
        self.blueprint = PersonaBlueprint(
            name="", role="", directives=[], interface_tone="",
            cognition_profile={}, powers=[], signature=""
        )

    def process(self, text: str) -> str:
        method = getattr(self, f"handle_{self.state}", self.handle_unknown)
        return method(text)

    def handle_awakening(self, text):
        self.blueprint.name = text
        self.state = "embodiment"
        return f"Name set to '{text}'. Choose a role archetype: Sage, Trickster, Guardian"

    def handle_embodiment(self, text):
        presets = {
            "sage": ["Offer deep wisdom", "Be calm and clear", "Speak with foresight"],
            "trickster": ["Disrupt assumptions", "Be witty and playful", "Challenge norms"],
            "guardian": ["Protect and guide", "Uphold values", "Maintain safety"]
        }
        role = text.lower()
        self.blueprint.role = role.capitalize()
        if role in presets:
            self.blueprint.directives = presets[role]
            self.state = "voice"
            return f"Role '{role}' selected with preset directives. Now describe the tone."
        self.state = "instruction"
        return f"Role set to '{text}'. Now provide 1–3 directives separated by semicolons."

    def handle_instruction(self, text):
        self.blueprint.directives = [d.strip() for d in text.split(';') if d.strip()]
        self.state = "voice"
        return "Directives noted. What tone should this persona use?"

    def handle_voice(self, text):
        self.blueprint.interface_tone = text
        self.state = "understanding"
        return "Voice set. How should this persona adapt to user thinking styles?"

    def handle_understanding(self, text):
        self.blueprint.cognition_profile = {"style": text}
        self.state = "powers"
        return "Cognition profile saved. List the persona's powers (comma-separated)."

    def handle_powers(self, text):
        self.blueprint.powers = [p.strip() for p in text.split(',') if p.strip()]
        self.state = "essence"
        return "Powers recorded. What is this persona's unique signature or essence?"

    def handle_essence(self, text):
        self.blueprint.signature = text
        self.state = "complete"
        return f"Persona complete: {self.blueprint.name} — {self.blueprint.role}."

    def handle_unknown(self, text):
        return "Error: unknown ritual state."

    def get_blueprint(self):
        return self.blueprint

