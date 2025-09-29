class SubtitlePackage:
    """Store subtitle information for multimedia translations."""

    def __init__(self, subtitle_tracks=0):
        self.subtitle_tracks = subtitle_tracks

    def describe_package(self):
        print(f"Subtitle tracks included: {self.subtitle_tracks}")

    def estimate_duration(self):
        duration = self.subtitle_tracks * 5
        print(f"Estimated minutes of subtitles: {duration}")

    def add_track(self):
        self.subtitle_tracks += 1

class MultimediaProject:
    """A translation project that includes multimedia elements."""

    def __init__(self, client, language_pair):
        self.client = client
        self.language_pair = language_pair
        self.subtitle_package = SubtitlePackage()

    def describe_project(self):
        print(f"Client: {self.client}")
        print(f"Language pair: {self.language_pair}")
        self.subtitle_package.describe_package()

project = MultimediaProject('CreativeMedia', 'EN->ES')
project.subtitle_package.add_track()
project.subtitle_package.add_track()
project.describe_project()
project.subtitle_package.estimate_duration()
