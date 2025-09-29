responses = {}

polling_active = True

while polling_active:
    name = input("Translator name: ")
    preference = input("Which CAT tool do you prefer? ")

    responses[name] = preference

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, preference in responses.items():
    print(f"{name.title()} prefers {preference.title()}.")
