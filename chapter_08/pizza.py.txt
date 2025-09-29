def build_keyword_list(base_language, target_language, *keywords):
    print(f"Keyword list for {base_language}->{target_language}:")
    for keyword in keywords:
        print(f"- {keyword}")

build_keyword_list('English', 'Spanish', 'stakeholder', 'compliance', 'sustainability')
