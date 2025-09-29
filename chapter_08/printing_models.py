def prepare_projects(pending_projects, completed_projects):
    while pending_projects:
        project = pending_projects.pop()
        print(f"Processing translation project: {project}")
        completed_projects.append(project)

def summarize_projects(completed_projects):
    print("\nCompleted translation projects:")
    for project in completed_projects:
        print(f"- {project}")

pending_projects = ['legal contract', 'medical brochure', 'marketing campaign']
completed_projects = []

prepare_projects(pending_projects[:], completed_projects)
summarize_projects(completed_projects)
