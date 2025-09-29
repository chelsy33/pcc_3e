import car

project = car.TranslationProject('GlobalTech', 'EN->ZH')
video_project = car.MultimediaProject('CreativeMedia', 'EN->ES')
video_project.add_subtitle_track()

print(project.describe_project())
print(video_project.describe_project())
print(f"Subtitle tracks: {video_project.subtitle_tracks}")
