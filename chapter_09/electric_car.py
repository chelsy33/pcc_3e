# 知识点：通过继承扩展父类功能，描述电动车特性。

class TranslationProject:
    """Represent a general translation project."""

    def __init__(self, client, language_pair):
        self.client = client
        self.language_pair = language_pair
        self.status = 'preparation'

    def describe_project(self):
        print(f"Client: {self.client}")
        print(f"Language pair: {self.language_pair}")
        print(f"Status: {self.status}")

    def advance_status(self, new_status):
        self.status = new_status


class MultimediaProject(TranslationProject):
    """A specialized translation project that includes multimedia assets."""

    def __init__(self, client, language_pair):
        super().__init__(client, language_pair)
        self.subtitle_tracks = 0

    def add_subtitle_track(self):
        self.subtitle_tracks += 1

    def describe_project(self):
        super().describe_project()
        print(f"Subtitle tracks: {self.subtitle_tracks}")


project = MultimediaProject('CreativeMedia', 'EN->ES')
project.add_subtitle_track()
project.advance_status('subtitle adaptation')
project.describe_project()
