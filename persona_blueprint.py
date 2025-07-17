from pydantic import BaseModel, Field
from typing import List, Dict

class PersonaBlueprint(BaseModel):
    name: str = Field(..., description="Persona name")
    role: str = Field(..., description="Primary archetype")
    directives: List[str]
    interface_tone: str
    cognition_profile: Dict[str, str]
    powers: List[str]
    signature: str

