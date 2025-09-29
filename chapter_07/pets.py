active_assignments = ['legal contract', 'software release notes', 'marketing campaign']
completed_assignments = []

while active_assignments:
    assignment = active_assignments.pop(0)
    print(f"Completing: {assignment.title()}")
    completed_assignments.append(assignment)

print("\nCompleted assignments:")
for assignment in completed_assignments:
    print(f"- {assignment.title()}")
