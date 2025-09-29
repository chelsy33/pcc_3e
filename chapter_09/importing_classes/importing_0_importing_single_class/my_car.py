from car import TranslationProject

project = TranslationProject('GlobalTech', 'EN->ZH')
print(project.describe_project())
project.advance_status('translation')
print(f"Status: {project.status}")
