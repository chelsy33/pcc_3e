class TranslationProject:
    """Represent a general translation project."""

    def __init__(self, client, language_pair):
        self.client = client
        self.language_pair = language_pair
        self.status = 'preparation'
        self.word_count = 0

    def update_word_count(self, words):
        self.word_count += words

project = TranslationProject('GlobalTech', 'EN->ZH')
project.update_word_count(3200)
print(project.word_count)
