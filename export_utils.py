def generate_pdf(blueprint):
    html_content = f"""
    <html>
    <body style='font-family: Palatino Linotype, serif; padding: 2em;'>
        <h1>{blueprint.name}</h1>
        <p><strong>Role:</strong> {blueprint.role}</p>
        <p><strong>Tone:</strong> {blueprint.interface_tone}</p>
        <p><strong>Directives:</strong><br>{'<br>'.join(blueprint.directives)}</p>
        <p><strong>Cognition:</strong> {blueprint.cognition_profile.get('style')}</p>
        <p><strong>Powers:</strong><br>{', '.join(blueprint.powers)}</p>
        <p><strong>Signature:</strong><br>{blueprint.signature}</p>
    </body>
    </html>
    """
    path = "/tmp/persona_guide.html"
    with open(path, "w") as f:
        f.write(html_content)
    return path

def generate_deck_markdown(blueprint):
    return f"""
# {blueprint.name}
**Role**: {blueprint.role}

---

## Tone
{blueprint.interface_tone}

---

## Directives
{chr(10).join(f'- {d}' for d in blueprint.directives)}

---

## Cognition Style
{blueprint.cognition_profile.get('style')}

---

## Powers
{chr(10).join(f'- {p}' for p in blueprint.powers)}

---

## Essence
{blueprint.signature}
"""

