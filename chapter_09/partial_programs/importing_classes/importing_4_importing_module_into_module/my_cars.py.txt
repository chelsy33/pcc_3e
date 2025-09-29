from car import TranslationProject
from electric_car import MultimediaProject

project = TranslationProject('GlobalTech', 'EN->ZH')
video_project = MultimediaProject('CreativeMedia', 'EN->ES')
video_project.add_subtitle_track()

print(project.describe_project())
print(video_project.describe_project())
print(f"Subtitle tracks: {video_project.subtitle_tracks}")
