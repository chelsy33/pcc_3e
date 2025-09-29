projects = []
for project_number in range(3):
    project = {
        'language_pair': 'EN->FR',
        'word_count': 1500 + project_number * 500,
        'status': 'in progress'
    }
    projects.append(project)

for project in projects[:2]:
    if project['word_count'] > 2000:
        project['status'] = 'requires extra reviewer'

print(projects)
