class TranslationProject:
    """Represent a general translation project."""

    def __init__(self, client, language_pair):
        self.client = client
        self.language_pair = language_pair
        self.status = 'preparation'

class MultimediaProject(TranslationProject):
    """A translation project that includes multimedia elements."""

    def __init__(self, client, language_pair):
        super().__init__(client, language_pair)
        self.subtitle_tracks = 0

project = MultimediaProject('CreativeMedia', 'EN->ES')
print(project.client)
print(project.subtitle_tracks)
