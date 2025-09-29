class SubtitlePackage:
    """Store subtitle information for multimedia translations."""

    def __init__(self):
        self.subtitle_tracks = 0

    def describe_package(self):
        print(f"Subtitle tracks included: {self.subtitle_tracks}")

    def add_track(self):
        self.subtitle_tracks += 1

class TranslationProject:
    def __init__(self, client, language_pair):
        self.client = client
        self.language_pair = language_pair
        self.subtitle_package = SubtitlePackage()

project = TranslationProject('CreativeMedia', 'EN->ES')
project.subtitle_package.add_track()
project.subtitle_package.describe_package()
