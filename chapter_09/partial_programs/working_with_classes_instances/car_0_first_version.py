class TranslationProject:
    """Represent a general translation project."""

    def __init__(self, client, language_pair):
        self.client = client
        self.language_pair = language_pair
        self.status = 'preparation'

project = TranslationProject('GlobalTech', 'EN->ZH')
print(project.client)
print(project.language_pair)
