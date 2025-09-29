class TranslationProject:
    """Represent a general translation project."""

    def __init__(self, client, language_pair):
        self.client = client
        self.language_pair = language_pair
        self.status = 'preparation'
        self.word_count = 0

project = TranslationProject('GlobalTech', 'EN->ZH')
print(project.word_count)
project.word_count = 3500
print(project.word_count)
