cat_glossaries = ['legal terms', 'medical terminology', 'software UI strings', 'marketing slogans']
print("My favorite reference materials:")
for resource in cat_glossaries:
    print(f"- {resource.title()}")

print("\nTeam member's reference materials:")
for resource in cat_glossaries[:2]:
    print(f"- {resource.title()}")
