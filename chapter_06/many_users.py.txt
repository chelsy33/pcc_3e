translator_profiles = {
    'lwen': {
        'first': 'li',
        'last': 'wen',
        'languages': ['English', 'Chinese'],
    },
    'cchen': {
        'first': 'chen',
        'last': 'yu',
        'languages': ['English', 'Japanese'],
    },
}

for username, profile in translator_profiles.items():
    full_name = f"{profile['first']} {profile['last']}"
    languages = ', '.join(profile['languages'])
    print(f"User: {username}")
    print(f"  Name: {full_name.title()}")
    print(f"  Working languages: {languages}")
