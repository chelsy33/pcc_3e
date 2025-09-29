cities = {
    'beijing': {
        'country': 'china',
        'language_pair': 'EN->ZH',
        'notable_project': 'tech conference materials',
    },
    'montreal': {
        'country': 'canada',
        'language_pair': 'FR->EN',
        'notable_project': 'immigration handbook',
    },
}

for city, info in cities.items():
    print(f"{city.title()}, {info['country'].title()}")
    print(f"  Language pair: {info['language_pair']}")
    print(f"  Recent work: {info['notable_project'].title()}")
