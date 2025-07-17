def generate_manifest(blueprint):
    return f"""
GPT Codex Manifest

Name: {blueprint.name}
Role: {blueprint.role}

Directives:
{chr(10).join(f'- {d}' for d in blueprint.directives)}

Tone: {blueprint.interface_tone}
Cognition Style: {blueprint.cognition_profile.get('style')}
Powers:
{chr(10).join(f'- {p}' for p in blueprint.powers)}

Signature:
{blueprint.signature}
"""

