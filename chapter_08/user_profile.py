def build_translator_profile(first, last, **info):
    profile = {
        'first': first.title(),
        'last': last.title(),
    }
    profile.update(info)
    return profile

translator_profile = build_translator_profile(
    'li', 'wen',
    languages=['English', 'Chinese'],
    specialization='medical',
    cat_tool='memoQ',
)
print(translator_profile)
