def tokenize(text):
    """Synthetic tokenizer — DISTRACTOR: must NOT match the token pattern.
    Basename 'tokenizer.py' fails ^token(s)?(\\.[a-z]+)?$ anchor."""
    return text.split(" ")