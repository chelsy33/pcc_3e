banned_clients = ['late payer', 'unrealistic deadline']
client = 'late payer'

if client not in banned_clients:
    print(f"Scheduling project for {client}.")
else:
    print(f"Cannot accept the project: {client}.")
