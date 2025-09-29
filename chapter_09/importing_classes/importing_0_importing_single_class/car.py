class TranslationProject:
    """A simple model of a translation project."""

    def __init__(self, client, language_pair):
        self.client = client
        self.language_pair = language_pair
        self.status = 'preparation'

    def describe_project(self):
        description = f"{self.client} project ({self.language_pair})"
        return description

    def advance_status(self, new_status):
        self.status = new_status
