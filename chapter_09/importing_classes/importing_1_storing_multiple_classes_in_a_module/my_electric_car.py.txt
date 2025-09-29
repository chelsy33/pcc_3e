from car import MultimediaProject

project = MultimediaProject('CreativeMedia', 'EN->ES')
project.add_subtitle_track()
print(project.describe_project())
print(f"Subtitle tracks: {project.subtitle_tracks}")
