unconfirmed_translators = ['li wen', 'chen yu', 'maria gonzalez']
confirmed_translators = []

while unconfirmed_translators:
    translator = unconfirmed_translators.pop()
    print(f"Verifying CAT tool setup for {translator.title()}...")
    confirmed_translators.append(translator)

print("\nConfirmed translators:")
for translator in confirmed_translators:
    print(f"- {translator.title()}")
