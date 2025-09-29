def build_translator_name(first_name, last_name, middle_name=''):
    """Return a neatly formatted translator name."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

translator = build_translator_name('li', 'wen')
print(translator)
translator = build_translator_name('anna', 'garcia', 'maria')
print(translator)
