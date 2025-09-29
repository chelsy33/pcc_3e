team_members = ['project manager', 'lead translator', 'proofreader', 'terminologist']
print("Our core translation team:")
for member in team_members:
    print(f"- {member.title()}")

print("\nTeam roles 2-3:")
for member in team_members[1:3]:
    print(f"- {member.title()}")
