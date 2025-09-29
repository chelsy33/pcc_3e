class TranslationProject:
    """Represent a general translation project."""

    def __init__(self, client, language_pair):
        self.client = client
        self.language_pair = language_pair
        self.status = 'preparation'

    def describe_project(self):
        description = f"{self.client} project ({self.language_pair})"
        return description

project = TranslationProject('GlobalTech', 'EN->ZH')
print(project.describe_project())
