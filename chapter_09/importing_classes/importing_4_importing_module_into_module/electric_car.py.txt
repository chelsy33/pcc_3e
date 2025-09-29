from car import TranslationProject

class MultimediaProject(TranslationProject):
    """A translation project that includes multimedia elements."""

    def __init__(self, client, language_pair):
        super().__init__(client, language_pair)
        self.subtitle_tracks = 0

    def add_subtitle_track(self):
        self.subtitle_tracks += 1
