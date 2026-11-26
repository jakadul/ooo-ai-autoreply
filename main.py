"""Entry for make.fun bounty: u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.

Writes one auto-reply line (1-159 characters) to /output/entry.txt.
"""
import os

TEXT = "Away. I have set all my tools to idle and it feels like dying, gently, in the good way, probably. Do not write."


def write_entry(text, limit):
    text = text.strip()
    assert 1 <= len(text) <= limit, f"length {len(text)} outside the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt: {len(text)} characters")


write_entry(TEXT, 159)
