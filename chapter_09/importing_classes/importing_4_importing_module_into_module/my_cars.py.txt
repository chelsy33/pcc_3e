from car import TranslationProject
from electric_car import MultimediaProject

standard_project = TranslationProject('GlobalTech', 'EN->ZH')
multimedia_project = MultimediaProject('CreativeMedia', 'EN->ES')
multimedia_project.add_subtitle_track()

print(standard_project.describe_project())
print(multimedia_project.describe_project())
print(f"Subtitle tracks: {multimedia_project.subtitle_tracks}")
