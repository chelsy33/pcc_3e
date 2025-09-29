class TranslationProject:
    """Represent a general translation project."""

    def __init__(self, client, language_pair):
        self.client = client
        self.language_pair = language_pair
        self.status = 'preparation'

    def describe_project(self):
        description = f"{self.client} project ({self.language_pair})"
        return description

class MultimediaProject(TranslationProject):
    """A translation project that includes multimedia elements."""

    def __init__(self, client, language_pair):
        super().__init__(client, language_pair)
        self.subtitle_tracks = 0

    def add_subtitle_track(self):
        self.subtitle_tracks += 1

project = MultimediaProject('CreativeMedia', 'EN->ES')
project.add_subtitle_track()
print(project.describe_project())
print(f"Subtitle tracks: {project.subtitle_tracks}")
