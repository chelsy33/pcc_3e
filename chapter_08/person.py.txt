def build_translator(first_name, last_name, specialization='general'):
    translator = {
        'first': first_name.title(),
        'last': last_name.title(),
        'specialization': specialization,
    }
    return translator

translator = build_translator('li', 'wen', 'medical')
print(translator)
